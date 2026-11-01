"""Keep a few good first issues open at all times.

Run daily by .github/workflows/task-autopilot.yml. When fewer than MIN_FREE unassigned good first
issues are open, it opens the next missing guide translations (lowest chapter first, taking turns
between languages) until there are enough again, at most MAX_NEW per run. Issues that already cover
a file, open or claimed, are never duplicated.

    GITHUB_TOKEN=... python3 scripts/task_autopilot.py [--dry-run]
"""

from __future__ import annotations

import argparse
import os
import urllib.parse
from itertools import zip_longest
from pathlib import Path

from radar import API, ROOT, GitHub

REPO = "TanbirRamim/open-source-radar"
MIN_FREE = 6
MAX_NEW = 3
LABEL = "good first issue"

# Guide folders and the name used in issue titles. A folder only gets issues once it exists, so a new
# language starts with a hand-written "start the guide" issue.
LANGUAGES = {
    "bn": "Bengali",
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "hi": "Hindi",
    "id": "Indonesian",
    "ja": "Japanese",
    "ko": "Korean",
    "pl": "Polish",
    "pt-BR": "Portuguese",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh": "Chinese",
}


def chapters(root: Path = ROOT) -> list[str]:
    """English guide pages that can be translated, in reading order."""
    pages = sorted(p.name for p in (root / "guide").glob("[0-9][0-9]-*.md"))
    return [*pages, "glossary.md"]


def title_for(page: str, language: str) -> str:
    if page == "glossary.md":
        return f"Translate the glossary to {language}"
    number, _, rest = page.removesuffix(".md").partition("-")
    return f"Translate chapter {int(number)} ({rest.replace('-', ' ')}) to {language}"


def missing_translations(root: Path = ROOT) -> list[tuple[str, str]]:
    """(folder, page) pairs with no translation yet, lowest chapter first, alternating languages."""
    per_language = []
    for folder in sorted(LANGUAGES):
        if not (root / "guide" / folder).is_dir():
            continue
        per_language.append(
            [(folder, page) for page in chapters(root) if not (root / "guide" / folder / page).exists()]
        )
    return [task for round_ in zip_longest(*per_language) for task in round_ if task]


def body_for(folder: str, page: str, language: str) -> str:
    target = f"guide/{folder}/{page}"
    return (
        f"Translate `guide/{page}` to {language} as `{target}`.\n\n"
        "What to do:\n"
        f"- Keep the headings, code, commands and link targets. Links to pages that aren't translated yet "
        f"point to the English files (`../05-first-pull-request.md` and so on), links to the repo root need "
        f"`../../`\n"
        f"- Add the page to the table in `guide/{folder}/README.md`\n"
        f"- Natural {language} is better than word-for-word. Technical words people actually say in English "
        "can stay English\n\n"
        "To test: open the file on your branch on GitHub and click every link. The Markdown link check in CI "
        "covers it too.\n\n"
        "Comment `/claim` to take it (you get assigned right away)."
    )


def already_covered(folder: str, page: str, language: str, issues: list[dict]) -> bool:
    target = f"guide/{folder}/{page}"
    title = title_for(page, language).lower()
    return any(issue["title"].lower() == title or target in (issue.get("body") or "") for issue in issues)


def plan(issues: list[dict], root: Path = ROOT) -> list[tuple[str, str]]:
    """Which translations to open now, given the repository's open issues."""
    free = sum(
        1
        for issue in issues
        if not issue.get("assignees") and any(label["name"] == LABEL for label in issue.get("labels", []))
    )
    wanted = min(MAX_NEW, max(0, MIN_FREE - free))
    todo = [
        (folder, page)
        for folder, page in missing_translations(root)
        if not already_covered(folder, page, LANGUAGES[folder], issues)
    ]
    return todo[:wanted]


def open_issues(github: GitHub) -> list[dict]:
    issues, page = [], 1
    while True:
        query = urllib.parse.urlencode({"state": "open", "per_page": 100, "page": page})
        batch = github._request("GET", f"{API}/repos/{REPO}/issues?{query}")
        issues += [issue for issue in batch if "pull_request" not in issue]
        if len(batch) < 100:
            return issues
        page += 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="print what would be opened")
    args = parser.parse_args(argv)
    github = GitHub(os.environ.get("GITHUB_TOKEN", ""))
    for folder, page in plan(open_issues(github)):
        language = LANGUAGES[folder]
        title = title_for(page, language)
        if args.dry_run:
            print(f"would open: {title}")
            continue
        body = {"title": title, "body": body_for(folder, page, language), "labels": [LABEL, "translation"]}
        created = github._request("POST", f"{API}/repos/{REPO}/issues", body)
        print(f"opened #{created['number']}: {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
