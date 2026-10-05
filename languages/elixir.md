# Elixir quickstart

How Elixir projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Elixir issues: [Elixir issue list](../issues/by-language/elixir.md)

## Setup

- Elixir runs on Erlang/OTP, so you need both. Install them from [elixir-lang.org](https://elixir-lang.org/install.html) or with a version manager such as mise or asdf, using the versions in `.tool-versions` when the project has one.
- Check the installation with `elixir --version`, which prints both the Erlang/OTP and Elixir versions.

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `mix deps.get` |
| Build | `mix compile` |
| Run tests | `mix test` |
| One test file or line | `mix test test/my_app/user_test.exs` or `mix test test/my_app/user_test.exs:42` |
| Check formatting | `mix format --check-formatted` (run `mix format` to fix) |
| Lint | `mix credo` when Credo is in `mix.exs` |

## Tips

- Check `mix.exs` for the project's dependencies and its `aliases`, which often define the real setup and test steps.
- Phoenix apps usually have a `mix setup` alias and need a running PostgreSQL for `mix test`; check `config/test.exs` for the connection settings.
- Run the formatter before committing changes.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
