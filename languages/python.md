# Python quickstart

How Python projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Python issues: [Python issue list](../issues/by-language/python.md)

## Setup

- Install Python with [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`) or pyenv. Check `requires-python` in `pyproject.toml` for the supported versions.
- Create an isolated environment per project: `uv venv && source .venv/bin/activate` (Windows: `.venv\Scripts\activate`).

## Common commands

| Task | Usual command |
| --- | --- |
| Install for development | `uv sync --all-extras`, `uv pip install -e ".[dev]"`, `pip install -e ".[test]"`, or `poetry install` |
| Run tests | `pytest`, or `tox -e py312` / `nox -s tests` when the project uses them |
| Run one test | `pytest tests/test_module.py::test_name -x` |
| Lint and format | `ruff check .` and `ruff format --check .`, or `black --check .` and `flake8` |
| Type check | `mypy src/` or `pyright` |
| Pre-commit hooks | `pre-commit install` then `pre-commit run --all-files` |

## Tips

- Read `pyproject.toml`, `tox.ini`, `noxfile.py` and `.pre-commit-config.yaml`; together they describe exactly what CI runs.
- Many projects need a changelog fragment (towncrier) in a `changes/` or `CHANGES/` folder named after the issue number.
- Use the formatter version the project pins; different Black or Ruff versions reformat code differently.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
