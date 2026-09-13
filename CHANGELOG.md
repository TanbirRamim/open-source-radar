# Changelog

Notable changes to Open Source Radar. Data refreshes are not listed.

## 2026-09-13

- Maintainers can ask for their projects to be excluded (`[exclude]` in `scripts/config.toml`).
- The pipeline refuses to publish a run that lost most issues, which protects the lists from API outages.
- CI: tests on Python 3.11 to 3.13, Ruff, website script check, and Markdown link checking.
- Published the data format in [docs/data.md](docs/data.md).
- Projects directory: every tracked project with open newcomer issues, grouped by language.

## 2026-09-13 (initial release)

- Issue index for 30 languages and 12 topics, refreshed twice a day.
- Searchable website with filters for language, topic, label level and project rules.
- Nine-chapter contribution guide, glossary, and quickstarts for 14 languages.
