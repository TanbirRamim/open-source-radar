# Erlang quickstart

How Erlang projects are usually set up and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Erlang issues: [Erlang issue list](../issues/by-language/erlang.md)

## Setup

- Install Erlang/OTP and Rebar3 using the official installation instructions.
- Check `.tool-versions`, the project README, and CI configuration for the required Erlang/OTP version.
- Check `rebar.config` for dependencies, plugins, and project-specific settings.

## Common commands

| Task | Usual command |
| --- | --- |
| Check Erlang/OTP version | `erl -noshell -eval 'io:format("~s~n", [erlang:system_info(otp_release)]), halt().'` |
| Check Rebar3 version | `rebar3 version` |
| Compile the project | `rebar3 compile` |
| Run EUnit tests | `rebar3 eunit` (one module: `rebar3 eunit --module=my_mod`) |
| Run Common Test suites | `rebar3 ct` (one suite: `rebar3 ct --suite=test/my_SUITE`) |
| Cross-reference check | `rebar3 xref` |
| Check formatting | `rebar3 fmt --check` (when configured) |
| Format the project | `rebar3 fmt` (when configured) |
| Run Dialyzer checks | `rebar3 dialyzer` (when configured) |

## Tips

- Use the Erlang/OTP version specified by the project, especially when `.tool-versions` is present.
- Rebar3 commands depend on the project's configuration and installed plugins. Check `rebar.config` and CI before running them.
- Formatting commands require a configured formatter plugin. Follow the project's own instructions if it uses `erlfmt` or another formatter.
- The first `rebar3 dialyzer` run builds a PLT and can take several minutes; later runs reuse it and are fast.
- `erl -version` prints the emulator (ERTS) version, not the OTP release, which is why the table uses `otp_release`.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
