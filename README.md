<div align="center">

# Open Source Radar

**Find an open source issue you can start today, and learn how to turn it into a merged pull request.**

Open, unclaimed, newcomer-friendly issues from active open source projects, sorted by language and topic and refreshed every 12 hours, plus a complete, practical contribution guide.

[**Browse issues on the website**](https://tanbirramim.github.io/open-source-radar/) &nbsp;|&nbsp; [**Read the guide**](guide/README.md) &nbsp;|&nbsp; [**Issues by language**](issues/README.md#by-language) &nbsp;|&nbsp; [**Issues by topic**](issues/README.md#by-topic) &nbsp;|&nbsp; [**Projects directory**](projects/README.md)

[![Refresh issue data](https://github.com/TanbirRamim/open-source-radar/actions/workflows/refresh.yml/badge.svg)](https://github.com/TanbirRamim/open-source-radar/actions/workflows/refresh.yml)
[![CI](https://github.com/TanbirRamim/open-source-radar/actions/workflows/ci.yml/badge.svg)](https://github.com/TanbirRamim/open-source-radar/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-0E7C72.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-C2710C.svg)](CONTRIBUTING.md)

</div>

## Right now on the radar

<!-- RADAR:STATS:START -->
**3,526** open issues · **1,403** labeled for beginners · **1,203** active projects · updated 2026-09-20 20:19 UTC

**Languages:** [C++](issues/by-language/cpp.md) (359) · [Go](issues/by-language/go.md) (338) · [Rust](issues/by-language/rust.md) (324) · [TypeScript](issues/by-language/typescript.md) (310) · [Java](issues/by-language/java.md) (281) · [C#](issues/by-language/csharp.md) (269) · [Python](issues/by-language/python.md) (260) · [PHP](issues/by-language/php.md) (169) · [JavaScript](issues/by-language/javascript.md) (162) · [Kotlin](issues/by-language/kotlin.md) (160) · [C](issues/by-language/c.md) (160) · [Shell](issues/by-language/shell.md) (136) · [all languages](issues/README.md#by-language)

**Topics:** [Mobile and desktop apps](issues/by-topic/mobile.md) (603) · [Cloud, DevOps and infrastructure](issues/by-topic/cloud-devops.md) (531) · [AI and machine learning](issues/by-topic/ai-ml.md) (411) · [Developer tools](issues/by-topic/devtools.md) (410) · [Data and databases](issues/by-topic/data.md) (327) · [Web development](issues/by-topic/web.md) (274) · [Security and privacy](issues/by-topic/security.md) (227) · [Systems and embedded](issues/by-topic/systems.md) (179) · [Games and graphics](issues/by-topic/games-graphics.md) (144) · [Documentation and education](issues/by-topic/docs-education.md) (80) · [Science and research](issues/by-topic/science.md) (61) · [Finance and Web3](issues/by-topic/finance-web3.md) (57) · [Robotics](issues/by-topic/robotics.md) (10)
<!-- RADAR:STATS:END -->

## Why this exists

Finding a first issue is harder than it should be. Popular "good first issue" lists go stale, half the issues are already taken, and nobody tells you that a project requires a CLA, bans AI-generated code, or auto-closes pull requests from new accounts until after you have done the work.

Open Source Radar fixes the first part with data and the second part with a guide:

- **Only issues you can actually pick up.** Every listed issue is open, has no assignee, has no open or merged pull request linked to it, was updated in the last six months, and belongs to a project with recent commits.
- **A directory of welcoming projects.** Every active project with open newcomer issues, grouped by language, with stars and rules: [projects directory](projects/README.md).
- **Organized the way you search.** By [language](issues/README.md#by-language), by [topic](issues/README.md#by-topic) (web, developer tools, AI, data, DevOps, security, mobile, games, systems, docs, science, finance), by label level, and by project rules.
- **Project rules up front.** Each project is scanned for AI policies, Contributor License Agreements and DCO sign-off requirements, so you know what you are signing up for before you start.
- **Always fresh.** A GitHub Actions workflow rebuilds everything every 12 hours.
- **A guide that covers the parts people skip.** Not just "fork and clone": how to tell whether a project will review you, how to check an issue is really free, how to handle CLAs, DCO, AI policies and anti-spam bots, and what to do when your pull request is ignored or closed.

## Start here

| If you are... | Go to |
| --- | --- |
| Brand new to open source | [Guide, chapter 1: why contribute and what counts](guide/01-why-contribute.md) |
| Ready to set up Git and GitHub | [Chapter 2: set up your tools](guide/02-setup.md) |
| Looking for a project | [Projects directory](projects/README.md) and [chapter 3: choose a project](guide/03-choose-a-project.md) |
| Looking for an issue | [The website](https://tanbirramim.github.io/open-source-radar/) or the [issue index](issues/README.md) |
| About to open your first pull request | [Chapter 5: your first pull request, step by step](guide/05-first-pull-request.md) |
| Unsure about CLAs, DCO or AI rules | [Chapter 6: rules to check before you start](guide/06-rules-before-you-start.md) |
| Waiting on a review | [Chapter 8: reviews, feedback and rejection](guide/08-reviews.md) |
| Setting up a project in a new language | [Language quickstarts](languages/README.md) |

## The guide

1. [Why contribute, and what counts](guide/01-why-contribute.md)
2. [Set up your tools](guide/02-setup.md)
3. [Choose a project](guide/03-choose-a-project.md)
4. [Find an issue you can finish](guide/04-find-an-issue.md)
5. [Your first pull request, step by step](guide/05-first-pull-request.md)
6. [Rules to check before you start](guide/06-rules-before-you-start.md)
7. [Talking to maintainers](guide/07-communication.md)
8. [Reviews, feedback and rejection](guide/08-reviews.md)
9. [Keep going](guide/09-keep-going.md)

Plus a [glossary](guide/glossary.md) and [quickstarts for 14 languages](languages/README.md).

## How issues are selected

The [data pipeline](scripts/radar.py) is a single Python script with no dependencies. On each run it:

1. **Discovers projects** through GitHub search: public, non-archived, non-fork repositories in 30 languages with at least 500 stars, commits in the last 60 days, and at least one open issue labeled `good first issue` or `help wanted`.
2. **Collects issues** carrying common newcomer labels (`good first issue`, `help wanted`, `beginner`, `easy`, `E-easy`, `up-for-grabs` and variants) through the GraphQL API.
3. **Drops issues that are not available:** assigned, locked, linked to an open or merged pull request, or not updated in 180 days.
4. **Scans contribution files** (`CONTRIBUTING.md`, `AI_POLICY.md`, `AGENTS.md`, pull request templates) for AI policies, CLA and DCO requirements, weekly.
5. **Renders** the Markdown pages in [`issues/`](issues/README.md) and the JSON behind the website.

All thresholds and label lists live in [`scripts/config.toml`](scripts/config.toml). The badges are detected automatically and can be wrong, so always read the project's own contributing guide. If you spot a mistake, [open an issue](https://github.com/TanbirRamim/open-source-radar/issues/new/choose).

### Run it yourself

```bash
git clone https://github.com/TanbirRamim/open-source-radar.git
cd open-source-radar
export GITHUB_TOKEN=$(gh auth token)                  # any token with public read access
python3 scripts/radar.py all --languages "Rust,Go"    # Python 3.11+, no packages needed
python3 -m http.server -d site 8000                   # then open http://localhost:8000
```

## Use the data

The full dataset behind the website is one JSON file, refreshed twice a day and free to use in your own bots, newsletters, dashboards or Discord servers:

```bash
curl -s https://tanbirramim.github.io/open-source-radar/data/issues.json | jq '.issues | length'
```

The format, with examples, is documented in [docs/data.md](docs/data.md).

## Contributing

This project is itself a good first contribution. Ideas:

- Improve a guide chapter or a [language quickstart](languages/README.md), or add a new one.
- Add a label variant, language or topic keyword to [`scripts/config.toml`](scripts/config.toml).
- Report a project whose rules were detected incorrectly.
- Build something with [the data](docs/data.md) and tell us about it.
- Improve the [website](site/) or the [pipeline](scripts/radar.py), with a test in [`scripts/test_radar.py`](scripts/test_radar.py).

Read [CONTRIBUTING.md](CONTRIBUTING.md) first, and see the [Code of Conduct](CODE_OF_CONDUCT.md). Maintainers who prefer their project not to be listed can [open an issue](https://github.com/TanbirRamim/open-source-radar/issues/new/choose) and it will be excluded.

## Please, be a good citizen

Maintainers are people with limited time. When you use this list:

- Comment on or claim an issue only when you are really going to work on it.
- Do not open pull requests to many projects at once just to collect contributions.
- Follow each project's rules, including its policy on AI-generated contributions.
- If you stop working on something, say so, so someone else can pick it up.

If you found your first issue here, starring the repository helps other newcomers find it too.

## License

[MIT](LICENSE). Issue titles, descriptions and project metadata belong to their respective projects and are shown with links back to GitHub.
