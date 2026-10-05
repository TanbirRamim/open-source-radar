<div align="center">

# Open Source Radar

**Find an open source issue you can start today, and learn how to turn it into a merged pull request.**

Open, unclaimed, newcomer-friendly issues from active open source projects, sorted by language and topic and refreshed every 12 hours, plus a complete, practical contribution guide.

[**Browse issues on the website**](https://tanbirramim.github.io/open-source-radar/) &nbsp;|&nbsp; [**Read the guide**](guide/README.md) &nbsp;|&nbsp; [**Issues by language**](issues/README.md#by-language) &nbsp;|&nbsp; [**Issues by topic**](issues/README.md#by-topic) &nbsp;|&nbsp; [**Projects directory**](projects/README.md) &nbsp;|&nbsp; [**Dataset on Hugging Face**](https://huggingface.co/datasets/TanbirRamim/open-source-radar)

[![Refresh issue data](https://github.com/TanbirRamim/open-source-radar/actions/workflows/refresh.yml/badge.svg)](https://github.com/TanbirRamim/open-source-radar/actions/workflows/refresh.yml)
[![CI](https://github.com/TanbirRamim/open-source-radar/actions/workflows/ci.yml/badge.svg)](https://github.com/TanbirRamim/open-source-radar/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-0E7C72.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-C2710C.svg)](CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/TanbirRamim/open-source-radar?style=social)](https://github.com/TanbirRamim/open-source-radar/stargazers)

Found it useful? A star helps other newcomers find the radar.

</div>

## Right now on the radar

<!-- RADAR:STATS:START -->
**3,349** open issues · **1,289** labeled for beginners · **1,176** active projects · updated 2026-10-04 21:09 UTC

**Languages:** [C++](issues/by-language/cpp.md) (348) · [Go](issues/by-language/go.md) (316) · [C#](issues/by-language/csharp.md) (308) · [Rust](issues/by-language/rust.md) (286) · [TypeScript](issues/by-language/typescript.md) (271) · [Java](issues/by-language/java.md) (247) · [Python](issues/by-language/python.md) (242) · [PHP](issues/by-language/php.md) (160) · [JavaScript](issues/by-language/javascript.md) (158) · [Kotlin](issues/by-language/kotlin.md) (156) · [C](issues/by-language/c.md) (154) · [Shell](issues/by-language/shell.md) (126) · [all languages](issues/README.md#by-language)

**Topics:** [Mobile and desktop apps](issues/by-topic/mobile.md) (600) · [Cloud, DevOps and infrastructure](issues/by-topic/cloud-devops.md) (497) · [AI and machine learning](issues/by-topic/ai-ml.md) (404) · [Developer tools](issues/by-topic/devtools.md) (398) · [Data and databases](issues/by-topic/data.md) (309) · [Web development](issues/by-topic/web.md) (253) · [Security and privacy](issues/by-topic/security.md) (215) · [Systems and embedded](issues/by-topic/systems.md) (188) · [Games and graphics](issues/by-topic/games-graphics.md) (151) · [Documentation and education](issues/by-topic/docs-education.md) (82) · [Science and research](issues/by-topic/science.md) (61) · [Finance and Web3](issues/by-topic/finance-web3.md) (54) · [Robotics](issues/by-topic/robotics.md) (8)
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

Prefer a feed reader? Every language has an RSS feed of its 50 newest beginner issues, for example [Python](https://tanbirramim.github.io/open-source-radar/feeds/python.xml). All feeds are listed on the [feed index](https://tanbirramim.github.io/open-source-radar/feeds/index.html).

## Contributing

This project is itself a good first contribution. The [good first issues](https://github.com/TanbirRamim/open-source-radar/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are scoped so you can finish one in an evening, and every pull request gets a review. Ideas:

- Improve a guide chapter or a [language quickstart](languages/README.md), or add a new one.
- Add a label variant, language or topic keyword to [`scripts/config.toml`](scripts/config.toml).
- Report a project whose rules were detected incorrectly.
- Build something with [the data](docs/data.md) and tell us about it.
- Improve the [website](site/) or the [pipeline](scripts/radar.py), with a test in [`scripts/test_radar.py`](scripts/test_radar.py).

Read [CONTRIBUTING.md](CONTRIBUTING.md) first, and see the [Code of Conduct](CODE_OF_CONDUCT.md). Maintainers who prefer their project not to be listed can [open an issue](https://github.com/TanbirRamim/open-source-radar/issues/new/choose) and it will be excluded.

### Contributors

Thank you to everyone who has made the radar better:

- [@Nomee-123](https://github.com/Nomee-123): the `/` shortcut that focuses the website search ([#10](https://github.com/TanbirRamim/open-source-radar/pull/10))
- [@yyashikasharmaa](https://github.com/yyashikasharmaa): the Robotics topic ([#11](https://github.com/TanbirRamim/open-source-radar/pull/11))
- [@dharma0009](https://github.com/dharma0009): RSS feeds for every language ([#16](https://github.com/TanbirRamim/open-source-radar/pull/16))
- [@PandaHUN777](https://github.com/PandaHUN777): Atom self links in the RSS feeds ([#30](https://github.com/TanbirRamim/open-source-radar/pull/30))
- [@nightcityblade](https://github.com/nightcityblade): an end-to-end smoke test for the render pipeline ([#34](https://github.com/TanbirRamim/open-source-radar/pull/34))
- [@Shivani2965](https://github.com/Shivani2965): a styled RSS feed index page ([#36](https://github.com/TanbirRamim/open-source-radar/pull/36))
- [@AkashGowdaNC](https://github.com/AkashGowdaNC): issue counts on the feed index, with empty feeds hidden, and RSS feeds per topic ([#42](https://github.com/TanbirRamim/open-source-radar/pull/42), [#52](https://github.com/TanbirRamim/open-source-radar/pull/52))
- [@JiyaSinghal0604](https://github.com/JiyaSinghal0604): the Hindi and Spanish translations of the guide ([#44](https://github.com/TanbirRamim/open-source-radar/pull/44), [#46](https://github.com/TanbirRamim/open-source-radar/pull/46))
- [@nayan45633](https://github.com/nayan45633): `lastBuildDate` in the language feeds ([#50](https://github.com/TanbirRamim/open-source-radar/pull/50))
- [@Harshil-1603](https://github.com/Harshil-1603): feed item descriptions and categories, and the per-language RSS link on the website ([#48](https://github.com/TanbirRamim/open-source-radar/pull/48), [#49](https://github.com/TanbirRamim/open-source-radar/pull/49))
- [@vamsikrishnaavasarala88-png](https://github.com/vamsikrishnaavasarala88-png): the Elixir quickstart ([#51](https://github.com/TanbirRamim/open-source-radar/pull/51))

Your name goes here with your first merged pull request. And if the radar helped you, please give it a star: it's the simplest way to help other newcomers find it.

## Please, be a good citizen

Maintainers are people with limited time. When you use this list:

- Comment on or claim an issue only when you are really going to work on it.
- Do not open pull requests to many projects at once just to collect contributions.
- Follow each project's rules, including its policy on AI-generated contributions.
- If you stop working on something, say so, so someone else can pick it up.

If you found your first issue here, starring the repository helps other newcomers find it too.

## License

[MIT](LICENSE). Issue titles, descriptions and project metadata belong to their respective projects and are shown with links back to GitHub.
