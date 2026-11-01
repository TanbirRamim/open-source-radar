"""Post the week's freshest beginner issues as a Discussion.

Run every Monday by .github/workflows/weekly-digest.yml, after the morning refresh. Picks up to PICKS
beginner issues opened in the last week, at most one per project, from projects that merge outside
pull requests, and posts them in the Announcements category so people watching the repository get them.

    GITHUB_TOKEN=... python3 scripts/weekly_digest.py [--dry-run]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re

from radar import ISSUES_PATH, GitHub

PICKS = 10
MAX_COMMENTS = 2
MIN_MERGE_RATE = 0.3
REPOSITORY_ID = "R_kgDOUYgCkQ"
CATEGORY_ID = "DIC_kwDOUYgCkc4DFgJx"  # Announcements
SITE = "https://tanbirramim.github.io/open-source-radar/"
# Titles bots and empty templates leave behind; they make a poor first impression in a digest.
BOT_TITLES = re.compile(r"link checker report|dependency dashboard|renovate|broken links?", re.IGNORECASE)


def readable_title(title: str) -> bool:
    words = re.sub(r"\[[^\]]*\]", "", title).strip()
    return len(words) >= 12 and not BOT_TITLES.search(title)


def escape(title: str) -> str:
    return re.sub(r"([\[\]])", r"\\\1", title)


def merges_outside_prs(repo: dict) -> bool:
    stats = repo.get("external_prs") or {}
    rate = stats.get("merge_rate")
    # Unknown (search failed or no data) is fine; a project that merges almost none is not.
    return rate is None or rate >= MIN_MERGE_RATE


def pick(payload: dict, today: dt.date) -> list[dict]:
    since = (today - dt.timedelta(days=7)).isoformat()
    repositories = payload["repositories"]
    candidates = [
        issue
        for issue in payload["issues"]
        if issue["level"] == "beginner"
        and issue["created"] >= since
        and issue["comments"] <= MAX_COMMENTS
        and not issue.get("closed_pr")
        and readable_title(issue["title"])
        and merges_outside_prs(repositories[issue["repo"]])
    ]
    candidates.sort(key=lambda issue: (-repositories[issue["repo"]]["stars"], issue["repo"], issue["number"]))
    picks, seen = [], set()
    for issue in candidates:
        if issue["repo"] in seen:
            continue
        seen.add(issue["repo"])
        picks.append(issue)
        if len(picks) == PICKS:
            break
    return picks


def render(picks: list[dict], payload: dict, today: dt.date) -> tuple[str, str]:
    title = f"Fresh beginner issues, week of {today.isoformat()}"
    lines = [
        "New this week, labeled for beginners, few comments so far, from projects that merge pull requests "
        "from outside contributors:",
        "",
    ]
    for issue in picks:
        repo = payload["repositories"][issue["repo"]]
        lines.append(
            f"- [{escape(issue['title'])}]({issue['url']}) in **{issue['repo']}** ({repo['language'] or 'mixed'}, "
            f"{repo['stars']:,} stars)"
        )
    lines += [
        "",
        f"Check the issue is still free before you start. More on the [website]({SITE}), filtered by "
        "language and topic. Watch this repository (Custom → Discussions) to get this list every Monday.",
    ]
    return title, "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="print the post instead of creating it")
    args = parser.parse_args(argv)
    payload = json.loads(ISSUES_PATH.read_text(encoding="utf-8"))
    today = dt.date.today()
    picks = pick(payload, today)
    if not picks:
        print("no fresh beginner issues this week, nothing posted")
        return 0
    title, body = render(picks, payload, today)
    if args.dry_run:
        print(f"{title}\n\n{body}")
        return 0
    github = GitHub(os.environ.get("GITHUB_TOKEN", ""))
    mutation = (
        "mutation($repo: ID!, $category: ID!, $title: String!, $body: String!) {"
        " createDiscussion(input: {repositoryId: $repo, categoryId: $category, title: $title, body: $body})"
        " { discussion { url } } }"
    )
    variables = {"repo": REPOSITORY_ID, "category": CATEGORY_ID, "title": title, "body": body}
    result = github._request("POST", "https://api.github.com/graphql", {"query": mutation, "variables": variables})
    print(result["data"]["createDiscussion"]["discussion"]["url"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
