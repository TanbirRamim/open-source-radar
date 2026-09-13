# Contributing to Open Source Radar

Thanks for helping people find their first open source contribution. Every kind of improvement is welcome.

## Ways to help

- **Guide and quickstarts.** Fix mistakes, clarify steps, add missing tips, or add a quickstart for a language in [`languages/`](languages/README.md).
- **Data quality.** Add label variants, languages or topic keywords in [`scripts/config.toml`](scripts/config.toml), or report a project whose AI policy, CLA or DCO requirement was detected incorrectly.
- **Website.** Improve accessibility, performance or usability of [`site/`](site/).
- **Pipeline.** Improve [`scripts/radar.py`](scripts/radar.py). Pure logic changes need a test in [`scripts/test_radar.py`](scripts/test_radar.py).

## Do not edit generated files

These are rebuilt by the scheduled workflow, and manual edits are overwritten:

- everything in `issues/by-language/` and `issues/by-topic/`, and `issues/README.md`
- `projects/README.md`
- `data/*.json` (and `site/data/`, which is built at deploy time and not committed)
- the block between `RADAR:STATS:START` and `RADAR:STATS:END` in `README.md`

To change what they contain, change `scripts/config.toml` or `scripts/radar.py`.

## Suggesting that a project be excluded

Maintainers who would rather not have their project listed can open an issue, and it will be added to `[exclude]` in `scripts/config.toml`. It disappears from the lists on the next refresh.

## Making a change

1. Fork the repository and create a branch.
2. For pipeline changes, run the tests and linter: `python3 -m unittest discover scripts` (Python 3.11+) and `ruff check scripts && ruff format --check scripts`.
3. To try the pipeline on a small scale: `GITHUB_TOKEN=$(gh auth token) python3 scripts/radar.py all --languages "Rust"`, then `python3 -m http.server -d site 8000`. Do not commit the generated data from a partial run.
4. Keep pull requests focused on one change, and describe what changed and why in a few sentences.

## Style

- Plain, direct English. Short sentences. Explain things for someone doing this for the first time.
- Commands in fenced code blocks, and commands that actually work.
- Link to official documentation rather than copying long passages from it.

By contributing you agree that your contribution is licensed under the [MIT License](LICENSE), and you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
