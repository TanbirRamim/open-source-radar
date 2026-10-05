# Elixir quickstart

How Elixir projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

## Setup

Install Elixir from [elixir-lang.org](https://elixir-lang.org/install.html) or your package manager.

Verify the installation with `elixir --version`.

## Common commands

- Install dependencies: `mix deps.get`
- Build: `mix compile`
- Run tests: `mix test`
- Check formatting: `mix format --check-formatted`
- Format code: `mix format`
- Lint: `mix credo` when Credo is configured

## Tips

- Check `mix.exs` for project-specific tasks and dependencies.
- Prefer the project's own `README.md` and `CONTRIBUTING.md` when they define different commands.
- Run the formatter before committing changes.

## Before you push

- Tests for the area you changed pass locally.
- Formatter and linter pass with the project's configuration.
- Your diff contains no unrelated formatting or lockfile changes.
