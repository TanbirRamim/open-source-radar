# Changelog

Notable changes to Open Source Radar. Data refreshes are not listed.

## 2026-09-25

- Issues whose latest comment is a recent request to take them ("can I work on this?", "please assign this to me") are skipped for 21 days (`claim_within_days`). Any later reply, such as a maintainer saying they don't assign issues, lists the issue again.
- The website has a share image, a canonical URL and structured data.

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
