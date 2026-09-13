#!/usr/bin/env python3
"""Open Source Radar data pipeline.

Finds open, unclaimed, newcomer-friendly issues in popular and active GitHub
repositories, then renders them as Markdown pages (by language and by topic)
and as a JSON file for the website.

Only the Python standard library is used, so it runs anywhere Python 3.11+ is
available. Set GITHUB_TOKEN to a token with public read access.

    python scripts/radar.py discover   # find qualifying repositories
    python scripts/radar.py fetch      # collect issues and contribution policies
    python scripts/radar.py render     # write Markdown pages and site data
    python scripts/radar.py all        # all three, in order
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterable
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "scripts" / "config.toml"
DATA_DIR = ROOT / "data"
REPOS_PATH = DATA_DIR / "repos.json"
POLICY_PATH = DATA_DIR / "policies.json"
ISSUES_PATH = DATA_DIR / "issues.json"
SITE_DATA_PATH = ROOT / "site" / "data" / "issues.json"
API = "https://api.github.com"
USER_AGENT = "open-source-radar (+https://github.com/TanbirRamim/open-source-radar)"

# Files that describe how a project accepts contributions, in lookup order.
POLICY_FILES = [
    "CONTRIBUTING.md",
    ".github/CONTRIBUTING.md",
    "docs/CONTRIBUTING.md",
    "CONTRIBUTING.rst",
    "AI_POLICY.md",
    ".github/AI_POLICY.md",
    "AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/pull_request_template.md",
]


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def log(message: str) -> None:
    print(f"[radar] {message}", file=sys.stderr, flush=True)


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


def iso_to_datetime(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        if compact:
            json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        else:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def chunked(items: list[Any], size: int) -> Iterable[list[Any]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


# --------------------------------------------------------------------------- #
# GitHub client with rate-limit handling
# --------------------------------------------------------------------------- #


class GitHub:
    def __init__(self, token: str) -> None:
        if not token:
            raise SystemExit("GITHUB_TOKEN is not set.")
        self.token = token
        self.last_search = 0.0

    def _request(self, method: str, url: str, body: dict[str, Any] | None = None) -> Any:
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(6):
            request = urllib.request.Request(url, data=data, method=method)
            request.add_header("Authorization", f"Bearer {self.token}")
            request.add_header("Accept", "application/vnd.github+json")
            request.add_header("User-Agent", USER_AGENT)
            request.add_header("X-GitHub-Api-Version", "2022-11-28")
            if data is not None:
                request.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    return json.load(response)
            except urllib.error.HTTPError as error:
                wait = self._rate_limit_wait(error)
                if wait is not None and attempt < 5:
                    log(f"rate limited, waiting {wait:.0f}s")
                    time.sleep(wait)
                    continue
                if error.code >= 500 and attempt < 5:
                    time.sleep(2**attempt)
                    continue
                detail = error.read().decode(errors="replace")[:300]
                raise RuntimeError(f"{method} {url} failed: {error.code} {detail}") from error
            except (urllib.error.URLError, TimeoutError) as error:
                if attempt < 5:
                    time.sleep(2**attempt)
                    continue
                raise RuntimeError(f"{method} {url} failed: {error}") from error
        raise RuntimeError(f"{method} {url} failed after retries")

    @staticmethod
    def _rate_limit_wait(error: urllib.error.HTTPError) -> float | None:
        if error.code not in (403, 429):
            return None
        headers = error.headers
        if headers.get("Retry-After"):
            return float(headers["Retry-After"]) + 1
        if headers.get("X-RateLimit-Remaining") == "0" and headers.get("X-RateLimit-Reset"):
            return max(1.0, float(headers["X-RateLimit-Reset"]) - time.time() + 2)
        # Secondary rate limits come without reset headers.
        return 60.0

    def search_repositories(self, query: str, page: int) -> dict[str, Any]:
        # The search API allows 30 requests per minute for authenticated users.
        elapsed = time.time() - self.last_search
        if elapsed < 2.2:
            time.sleep(2.2 - elapsed)
        self.last_search = time.time()
        params = urllib.parse.urlencode({"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page})
        return self._request("GET", f"{API}/search/repositories?{params}")

    def graphql(self, query: str) -> dict[str, Any]:
        payload = self._request("POST", f"{API}/graphql", {"query": query})
        return payload


# --------------------------------------------------------------------------- #
# Safety checks
# --------------------------------------------------------------------------- #


def is_excluded(full_name: str, config: dict[str, Any]) -> bool:
    """Maintainers can ask for their projects to be left out. Entries are `owner/repo` or `owner/*`."""
    name = full_name.lower()
    owner = name.split("/", 1)[0]
    for entry in config.get("exclude", {}).get("repositories", []):
        entry = entry.strip().lower()
        if entry == name or entry == f"{owner}/*":
            return True
    return False


def check_not_shrunk(previous_count: int, new_count: int, min_ratio: float) -> None:
    """Refuse to replace good data with a result that lost most issues, which usually means API
    errors or rate limiting rather than a real change."""
    if previous_count and new_count < previous_count * min_ratio:
        raise SystemExit(
            f"Refusing to overwrite data: {new_count} issues collected, previously {previous_count} "
            f"(below {min_ratio:.0%}). Re-run later, or pass --force if the drop is expected."
        )


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #


def discovery_queries(language: str, config: dict[str, Any], today: dt.date) -> list[str]:
    discovery = config["discovery"]
    pushed_since = today - dt.timedelta(days=discovery["pushed_within_days"])
    base = (
        f'language:"{language}" stars:>={discovery["min_stars"]} '
        f"pushed:>={pushed_since.isoformat()} archived:false fork:false is:public"
    )
    return [f"{base} good-first-issues:>=1", f"{base} help-wanted-issues:>=1"]


def discover(github: GitHub, config: dict[str, Any]) -> dict[str, Any]:
    today = now_utc().date()
    cap = config["discovery"]["repos_per_language"]
    pages = config["discovery"]["pages_per_query"]
    repos: dict[str, dict[str, Any]] = {}
    for language in config["languages"]:
        found: dict[str, dict[str, Any]] = {}
        for query in discovery_queries(language, config, today):
            for page in range(1, pages + 1):
                result = github.search_repositories(query, page)
                items = result.get("items", [])
                for item in items:
                    found.setdefault(item["full_name"], {"stars": item["stargazers_count"]})
                if len(items) < 100:
                    break
        ranked = sorted(found.items(), key=lambda entry: entry[1]["stars"], reverse=True)[: cap * 2]
        for full_name, info in ranked:
            if is_excluded(full_name, config):
                continue
            repos.setdefault(full_name, {"language": language, "stars": info["stars"]})
        log(f"{language}: {len(ranked)} repositories")
    payload = {"discovered_at": now_utc().isoformat(timespec="seconds"), "repos": repos}
    write_json(REPOS_PATH, payload)
    log(f"discovered {len(repos)} repositories")
    return payload


# --------------------------------------------------------------------------- #
# Fetching issues and contribution policies
# --------------------------------------------------------------------------- #


def gql_string(value: str) -> str:
    return json.dumps(value)


def build_repo_query(repos: list[str], labels: list[str], per_repo: int, include_policy: bool) -> str:
    label_list = "[" + ",".join(gql_string(label) for label in labels) + "]"
    parts = []
    for index, full_name in enumerate(repos):
        owner, name = full_name.split("/", 1)
        policy = ""
        if include_policy:
            policy = "\n".join(
                f"    p{file_index}: object(expression: {gql_string('HEAD:' + path)}) {{ ... on Blob {{ text }} }}"
                for file_index, path in enumerate(POLICY_FILES)
            )
        parts.append(
            f"""  r{index}: repository(owner: {gql_string(owner)}, name: {gql_string(name)}) {{
    nameWithOwner url description stargazerCount forkCount isArchived pushedAt
    primaryLanguage {{ name }}
    licenseInfo {{ spdxId }}
    repositoryTopics(first: 20) {{ nodes {{ topic {{ name }} }} }}
    issues(states: OPEN, first: {per_repo}, orderBy: {{field: UPDATED_AT, direction: DESC}},
           filterBy: {{labels: {label_list}}}) {{
      nodes {{
        number title url createdAt updatedAt locked
        comments {{ totalCount }}
        assignees {{ totalCount }}
        labels(first: 10) {{ nodes {{ name color }} }}
        timelineItems(itemTypes: [CONNECTED_EVENT, CROSS_REFERENCED_EVENT], last: 20) {{
          nodes {{
            ... on ConnectedEvent {{ subject {{ ... on PullRequest {{ state }} }} }}
            ... on CrossReferencedEvent {{ source {{ ... on PullRequest {{ state }} }} }}
          }}
        }}
      }}
    }}
{policy}
  }}"""
        )
    return "query {\n" + "\n".join(parts) + "\n  rateLimit { cost remaining resetAt }\n}"


def linked_pr_states(issue: dict[str, Any]) -> list[str]:
    states = []
    for node in (issue.get("timelineItems") or {}).get("nodes") or []:
        if not node:
            continue
        pull = node.get("subject") or node.get("source") or {}
        if pull.get("state"):
            states.append(pull["state"])
    return states


def issue_is_available(issue: dict[str, Any], updated_since: dt.datetime) -> bool:
    """An issue is worth listing when nobody is assigned, no open or merged PR is linked,
    it is not locked, and it saw activity recently."""
    if issue.get("locked"):
        return False
    if (issue.get("assignees") or {}).get("totalCount", 0) > 0:
        return False
    if any(state in ("OPEN", "MERGED") for state in linked_pr_states(issue)):
        return False
    return iso_to_datetime(issue["updatedAt"]) >= updated_since


AI_TERMS = re.compile(
    r"\b(ai|llms?|large language models?|generative|genai|chatgpt|copilot|claude|codex|gemini|"
    r"machine[- ]generated|ai[- ](assisted|generated)|coding agents?|ai agents?|vibe[- ]?cod\w*)\b",
    re.IGNORECASE,
)
AI_BAN_TERMS = re.compile(
    r"(not|never|n't)\s+(accept|allow|permit|welcome)\w*[^.\n]{0,80}\b(ai|llm|generat)|"
    r"\b(forbid|prohibit|ban)\w*[^.\n]{0,60}\b(ai|llm|generative)|"
    r"\b(ai|llm)[- ]generated[^.\n]{0,60}\b(rejected|closed|not accepted|not allowed|banned)|"
    r"\b(ai agents?|agents?|llms?)\s+(are|is)\s+not\s+allowed|"
    r"\bnever\s+(create|open|submit)\s+(a\s+)?(pr|pull request)|"
    r"\b(do not|don't)\s+(vibe[- ]?code|use (ai|llms?) to (write|generate))",
    re.IGNORECASE,
)
AI_DISCLOSE_TERMS = re.compile(
    r"\b(disclos\w*|assisted-by|co-authored-by:?\s*\w*\s*(ai|agent)|mention\w*[^.\n]{0,40}\b(ai|llm)|"
    r"identify themselves|must (state|indicate|note)[^.\n]{0,40}\b(ai|llm))",
    re.IGNORECASE,
)
CLA_TERMS = re.compile(r"\bCLA\b|contributor license agreement|cla-assistant|easycla", re.IGNORECASE)
DCO_TERMS = re.compile(r"\bDCO\b|developer certificate of origin|signed-off-by|git commit -s\b", re.IGNORECASE)


def detect_policy(files: dict[str, str]) -> dict[str, Any]:
    """Summarise contribution requirements from the text of a project's contribution files.

    The result is a hint for contributors, not a legal reading: the website always links to
    the source files and tells people to read them.
    """
    ai = "none"
    ai_file = None
    cla = dco = False
    for path, text in files.items():
        if not text:
            continue
        if CLA_TERMS.search(text):
            cla = True
        if DCO_TERMS.search(text):
            dco = True
        # AI_POLICY.md and AGENTS.md exist only to address AI use, so they need no keyword match.
        is_ai_file = path.endswith(("AI_POLICY.md", "AGENTS.md"))
        if not (is_ai_file or AI_TERMS.search(text)):
            continue
        if AI_BAN_TERMS.search(text):
            level = "restricted"
        elif AI_DISCLOSE_TERMS.search(text):
            level = "disclose"
        elif path.endswith("AI_POLICY.md") or re.search(
            r"\b(ai|llm)s?\b[^.\n]{0,80}\b(policy|guideline|rule)", text, re.IGNORECASE
        ):
            level = "policy"
        else:
            continue
        rank = {"none": 0, "policy": 1, "disclose": 2, "restricted": 3}
        if rank[level] > rank[ai]:
            ai, ai_file = level, path
    return {"ai": ai, "ai_file": ai_file, "cla": cla, "dco": dco, "files": sorted(p for p, t in files.items() if t)}


def topic_buckets(topics: list[str], config: dict[str, Any]) -> list[str]:
    buckets = []
    lowered = [topic.lower() for topic in topics]
    for slug, bucket in config["topics"].items():
        for keyword in bucket["keywords"]:
            if keyword.endswith("*"):
                stem = keyword[:-1]
                matched = any(stem in topic for topic in lowered)
            else:
                matched = keyword in lowered
            if matched:
                buckets.append(slug)
                break
    return buckets


def difficulty(labels: list[str]) -> str:
    joined = " ".join(labels).lower()
    if re.search(r"first[- ]timers|good[- ]first|beginner|easy|starter", joined):
        return "beginner"
    return "help-wanted"


def fetch(github: GitHub, config: dict[str, Any], *, force: bool = False) -> dict[str, Any]:
    repos_payload = read_json(REPOS_PATH, None)
    if not repos_payload:
        raise SystemExit("data/repos.json is missing; run `radar.py discover` first.")
    tracked = repos_payload["repos"]
    policies = read_json(POLICY_PATH, {})
    refresh_before = now_utc() - dt.timedelta(days=config["policy"]["refresh_days"])
    updated_since = now_utc() - dt.timedelta(days=config["issues"]["updated_within_days"])
    labels = config["issues"]["labels"]
    per_repo = config["issues"]["per_repo"]

    repositories: dict[str, Any] = {}
    issues: list[dict[str, Any]] = []
    names = sorted(name for name in tracked if not is_excluded(name, config))
    for batch_index, batch in enumerate(chunked(names, 6)):
        needs_policy = any(
            name not in policies or iso_to_datetime(policies[name]["scanned_at"]) < refresh_before for name in batch
        )
        query = build_repo_query(batch, labels, per_repo, include_policy=needs_policy)
        try:
            response = github.graphql(query)
        except RuntimeError as error:
            log(f"batch {batch_index} failed, retrying one repository at a time: {error}")
            response = {"data": {}}
            for single_index, name in enumerate(batch):
                try:
                    single = github.graphql(build_repo_query([name], labels, per_repo, include_policy=needs_policy))
                    response["data"][f"r{single_index}"] = (single.get("data") or {}).get("r0")
                except RuntimeError as single_error:
                    log(f"skipping {name}: {single_error}")
        data = response.get("data") or {}
        for index, name in enumerate(batch):
            repo = data.get(f"r{index}")
            if not repo or repo.get("isArchived"):
                continue
            full_name = repo["nameWithOwner"]
            if needs_policy:
                texts = {path: (repo.get(f"p{i}") or {}).get("text") or "" for i, path in enumerate(POLICY_FILES)}
                policies[full_name] = {**detect_policy(texts), "scanned_at": now_utc().isoformat(timespec="seconds")}
            topics = [node["topic"]["name"] for node in repo["repositoryTopics"]["nodes"]]
            available = []
            for issue in repo["issues"]["nodes"]:
                if not issue_is_available(issue, updated_since):
                    continue
                label_names = [label["name"] for label in issue["labels"]["nodes"]]
                available.append(
                    {
                        "repo": full_name,
                        "number": issue["number"],
                        "title": issue["title"],
                        "url": issue["url"],
                        "labels": label_names,
                        "level": difficulty(label_names),
                        "created": issue["createdAt"][:10],
                        "updated": issue["updatedAt"][:10],
                        "comments": issue["comments"]["totalCount"],
                        "closed_pr": "CLOSED" in linked_pr_states(issue),
                    }
                )
            if not available:
                continue
            issues.extend(available)
            policy = policies.get(full_name, {})
            repositories[full_name] = {
                "url": repo["url"],
                "description": (repo.get("description") or "").strip(),
                "stars": repo["stargazerCount"],
                "forks": repo["forkCount"],
                "language": (repo.get("primaryLanguage") or {}).get("name") or tracked.get(name, {}).get("language"),
                "license": (repo.get("licenseInfo") or {}).get("spdxId"),
                "pushed": repo["pushedAt"][:10],
                "topics": topics,
                "buckets": topic_buckets(topics, config),
                "policy": {key: policy.get(key) for key in ("ai", "ai_file", "cla", "dco")},
                "open_count": len(available),
            }
        rate = data.get("rateLimit") or {}
        if batch_index % 20 == 0:
            log(f"batch {batch_index}: {len(issues)} issues so far, graphql remaining {rate.get('remaining')}")

    issues.sort(key=lambda item: (item["updated"], repositories[item["repo"]]["stars"]), reverse=True)
    if not force:
        previous = read_json(ISSUES_PATH, {}) or {}
        check_not_shrunk(len(previous.get("issues", [])), len(issues), config["safety"]["min_ratio"])
    payload = {
        "generated_at": now_utc().isoformat(timespec="seconds"),
        "repositories": repositories,
        "issues": issues,
    }
    write_json(POLICY_PATH, policies)
    write_json(ISSUES_PATH, payload, compact=True)
    log(f"collected {len(issues)} issues from {len(repositories)} repositories")
    return payload


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

LEVEL_BADGE = {"beginner": "🟢 beginner", "help-wanted": "🟡 help wanted"}
AI_NOTE = {
    "restricted": "⚠️ AI restricted",
    "disclose": "🤖 disclose AI use",
    "policy": "📄 AI policy",
}


def md_escape(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("`", "'")


def format_stars(stars: int) -> str:
    if stars >= 1000:
        return f"{stars / 1000:.1f}k".replace(".0k", "k")
    return str(stars)


def notes_for(repo: dict[str, Any]) -> str:
    policy = repo.get("policy") or {}
    notes = []
    if policy.get("ai") in AI_NOTE:
        notes.append(AI_NOTE[policy["ai"]])
    if policy.get("cla"):
        notes.append("✍️ CLA")
    if policy.get("dco"):
        notes.append("🔏 DCO")
    return " · ".join(notes)


def issue_table(issues: list[dict[str, Any]], repositories: dict[str, Any], limit: int) -> str:
    lines = [
        "| Issue | Repository | Stars | Level | Updated | Notes |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for issue in issues[:limit]:
        repo = repositories[issue["repo"]]
        title = md_escape(issue["title"])[:110]
        comments = f" 💬 {issue['comments']}" if issue["comments"] else ""
        lines.append(
            f"| [{title}]({issue['url']}){comments} "
            f"| [{issue['repo']}]({repo['url']}) "
            f"| {format_stars(repo['stars'])} "
            f"| {LEVEL_BADGE[issue['level']]} "
            f"| {issue['updated']} "
            f"| {notes_for(repo)} |"
        )
    return "\n".join(lines)


def page_header(title: str, subtitle: str, generated_at: str) -> str:
    return (
        f"# {title}\n\n"
        f"{subtitle}\n\n"
        f"> Updated automatically on **{generated_at[:16].replace('T', ' ')} UTC**. "
        "Every issue listed here was open, unassigned and without an open or merged pull request when it was "
        "collected. Always read the issue and the project's contributing guide before you start.\n>\n"
        "> Prefer filters and search? Use the [website](https://tanbirramim.github.io/open-source-radar/). "
        "New here? Start with the [guide](../../guide/README.md).\n\n"
        "**Legend:** 🟢 beginner label · 🟡 help wanted · 💬 comments · ⚠️ AI restricted · 🤖 disclose AI use · "
        "📄 AI policy · ✍️ CLA required · 🔏 DCO sign-off. Notes are detected automatically; "
        "[how to read them](../../guide/06-rules-before-you-start.md).\n\n"
    )


def render(config: dict[str, Any]) -> None:
    payload = read_json(ISSUES_PATH, None)
    if not payload:
        raise SystemExit("data/issues.json is missing; run `radar.py fetch` first.")
    repositories = payload["repositories"]
    issues = payload["issues"]
    generated_at = payload["generated_at"]
    limit = config["issues"]["max_per_page"]
    languages: dict[str, str] = config["languages"]

    by_language_dir = ROOT / "issues" / "by-language"
    by_topic_dir = ROOT / "issues" / "by-topic"
    for directory in (by_language_dir, by_topic_dir):
        directory.mkdir(parents=True, exist_ok=True)
        for old in directory.glob("*.md"):
            old.unlink()

    language_rows = []
    for language, slug in languages.items():
        subset = [issue for issue in issues if repositories[issue["repo"]]["language"] == language]
        if not subset:
            continue
        repo_count = len({issue["repo"] for issue in subset})
        beginner = sum(1 for issue in subset if issue["level"] == "beginner")
        body = page_header(
            f"{language} issues",
            f"**{len(subset)}** open issues ({beginner} labeled for beginners) across **{repo_count}** "
            f"active {language} projects.",
            generated_at,
        ) + issue_table(subset, repositories, limit)
        if len(subset) > limit:
            body += f"\n\nShowing the {limit} most recently updated. See all {len(subset)} on the website."
        (by_language_dir / f"{slug}.md").write_text(body + "\n", encoding="utf-8")
        language_rows.append((language, slug, len(subset), beginner, repo_count))

    topic_rows = []
    for slug, bucket in config["topics"].items():
        subset = [issue for issue in issues if slug in repositories[issue["repo"]]["buckets"]]
        if not subset:
            continue
        repo_count = len({issue["repo"] for issue in subset})
        beginner = sum(1 for issue in subset if issue["level"] == "beginner")
        body = page_header(
            f"{bucket['title']} issues",
            f"**{len(subset)}** open issues ({beginner} labeled for beginners) across **{repo_count}** projects "
            f"tagged with topics like {', '.join('`' + k.rstrip('*') + '`' for k in bucket['keywords'][:6])}.",
            generated_at,
        ) + issue_table(subset, repositories, limit)
        if len(subset) > limit:
            body += f"\n\nShowing the {limit} most recently updated. See all {len(subset)} on the website."
        (by_topic_dir / f"{slug}.md").write_text(body + "\n", encoding="utf-8")
        topic_rows.append((bucket["title"], slug, len(subset), beginner, repo_count))

    language_rows.sort(key=lambda row: row[2], reverse=True)
    topic_rows.sort(key=lambda row: row[2], reverse=True)
    beginner_total = sum(1 for issue in issues if issue["level"] == "beginner")
    index = [
        "# Issue index",
        "",
        f"**{len(issues)}** open, unclaimed issues from **{len(repositories)}** active projects "
        f"({beginner_total} labeled for beginners). Updated {generated_at[:16].replace('T', ' ')} UTC.",
        "",
        "Looking for a project rather than an issue? See the [projects directory](../projects/README.md).",
        "",
        "## By language",
        "",
        "| Language | Issues | Beginner | Projects |",
        "| --- | ---: | ---: | ---: |",
        *[
            f"| [{name}](by-language/{slug}.md) | {count} | {beg} | {projects} |"
            for name, slug, count, beg, projects in language_rows
        ],
        "",
        "## By topic",
        "",
        "| Topic | Issues | Beginner | Projects |",
        "| --- | ---: | ---: | ---: |",
        *[
            f"| [{name}](by-topic/{slug}.md) | {count} | {beg} | {projects} |"
            for name, slug, count, beg, projects in topic_rows
        ],
        "",
    ]
    (ROOT / "issues" / "README.md").write_text("\n".join(index), encoding="utf-8")

    render_projects(repositories, issues, config, generated_at)
    update_readme_stats(len(issues), len(repositories), beginner_total, language_rows, topic_rows, generated_at)
    site_payload = {**payload, "topic_titles": {slug: bucket["title"] for slug, bucket in config["topics"].items()}}
    write_json(SITE_DATA_PATH, site_payload, compact=True)
    log(f"rendered {len(language_rows)} language pages and {len(topic_rows)} topic pages")


def render_projects(
    repositories: dict[str, Any], issues: list[dict[str, Any]], config: dict[str, Any], generated_at: str
) -> None:
    """Write projects/README.md: every tracked project with open newcomer issues, grouped by language."""
    beginner_counts: dict[str, int] = {}
    for issue in issues:
        if issue["level"] == "beginner":
            beginner_counts[issue["repo"]] = beginner_counts.get(issue["repo"], 0) + 1
    by_language: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for full_name, repo in repositories.items():
        by_language.setdefault(repo.get("language") or "Other", []).append((full_name, repo))
    ordered = sorted(by_language.items(), key=lambda entry: len(entry[1]), reverse=True)
    slugs: dict[str, str] = config["languages"]

    lines = [
        "# Projects welcoming contributors",
        "",
        f"**{len(repositories):,}** active open source projects that currently have open, unclaimed issues labeled for "
        f"newcomers or help wanted, grouped by language. Updated {generated_at[:16].replace('T', ' ')} UTC.",
        "",
        "Use this page to find a project first, then pick an issue in it. Before contributing, check that the project "
        "merged pull requests from outside contributors recently ([how](../guide/03-choose-a-project.md)).",
        "",
        "**Rules column:** ⚠️ AI restricted · 🤖 disclose AI use · 📄 AI policy · ✍️ CLA · 🔏 DCO, "
        "detected automatically "
        "from contribution files. [What these mean](../guide/06-rules-before-you-start.md).",
        "",
        "## Languages",
        "",
        " · ".join(
            f"[{language} ({len(entries)})](#{re.sub(r'[^a-z0-9 -]', '', language.lower()).replace(' ', '-')})"
            for language, entries in ordered
        ),
        "",
    ]
    for language, entries in ordered:
        entries.sort(key=lambda entry: entry[1]["stars"], reverse=True)
        issues_link = f" · [open issues](../issues/by-language/{slugs[language]}.md)" if language in slugs else ""
        lines += [
            f"## {language}",
            "",
            f"{len(entries)} projects{issues_link}",
            "",
            "| Project | Stars | Open issues | Beginner | Rules | What it is |",
            "| --- | ---: | ---: | ---: | --- | --- |",
        ]
        for full_name, repo in entries:
            description = md_escape(repo.get("description") or "")[:120]
            lines.append(
                f"| [{full_name}]({repo['url']}/issues) | {format_stars(repo['stars'])} | {repo['open_count']} "
                f"| {beginner_counts.get(full_name, 0)} | {notes_for(repo)} | {description} |"
            )
        lines.append("")
    target = ROOT / "projects" / "README.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")


def update_readme_stats(
    issue_count: int,
    repo_count: int,
    beginner_count: int,
    language_rows: list[tuple[str, str, int, int, int]],
    topic_rows: list[tuple[str, str, int, int, int]],
    generated_at: str,
) -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    top_languages = " · ".join(
        f"[{name}](issues/by-language/{slug}.md) ({count})" for name, slug, count, _, _ in language_rows[:12]
    )
    top_topics = " · ".join(f"[{name}](issues/by-topic/{slug}.md) ({count})" for name, slug, count, _, _ in topic_rows)
    block = (
        "<!-- RADAR:STATS:START -->\n"
        f"**{issue_count:,}** open issues · **{beginner_count:,}** labeled for beginners · "
        f"**{repo_count:,}** active projects · updated {generated_at[:16].replace('T', ' ')} UTC\n\n"
        f"**Languages:** {top_languages} · [all languages](issues/README.md#by-language)\n\n"
        f"**Topics:** {top_topics}\n"
        "<!-- RADAR:STATS:END -->"
    )
    text = readme.read_text(encoding="utf-8")
    updated = re.sub(r"<!-- RADAR:STATS:START -->.*?<!-- RADAR:STATS:END -->", block, text, flags=re.DOTALL)
    readme.write_text(updated, encoding="utf-8")


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["discover", "fetch", "render", "all"])
    parser.add_argument("--languages", help="comma-separated subset of configured languages (for local testing)")
    parser.add_argument(
        "--force", action="store_true", help="write results even if far fewer issues were found than last time"
    )
    args = parser.parse_args(argv)

    config = load_config()
    if args.languages:
        wanted = {name.strip() for name in args.languages.split(",")}
        config["languages"] = {name: slug for name, slug in config["languages"].items() if name in wanted}
    token = os.environ.get("GITHUB_TOKEN", "")

    if args.command in ("discover", "all"):
        discover(GitHub(token), config)
    if args.command in ("fetch", "all"):
        # A language subset is an explicit test run, so a smaller result is expected.
        fetch(GitHub(token), config, force=args.force or bool(args.languages))
    if args.command in ("render", "all"):
        render(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
