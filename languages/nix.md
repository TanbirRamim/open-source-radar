# Nix quickstart

Practical commands for inspecting, entering, building and checking a Nix project. The project's own `CONTRIBUTING.md` always takes priority.

Open Nix issues: [Nix issue list](../issues/by-language/nix.md)

## Setup

- Install Nix using the [official installation guide](https://nix.dev/install-nix), then check it with `nix --version`.
- Read `flake.nix` and the project guide first. A `flake.lock` records pinned inputs; keep it unless the task requires an update.
- Some flake commands are documented as experimental. If they are unavailable, check the project's setup instructions and your Nix version before changing machine-wide configuration.

## Common commands

| Task | Command |
| --- | --- |
| List the outputs a flake provides | `nix flake show .` |
| Enter the project's development environment | `nix develop` |
| Evaluate the flake and build its declared checks | `nix flake check` |
| Build the default package | `nix build` |
| Build a named package | `nix build .#<package>` |
| Format with the formatter configured by the flake | `nix fmt` |

`nix develop`, `nix flake check`, `nix build` and `nix fmt` depend on the outputs and formatter declared by that project. Use `nix flake show .` to find available package and check names; `nix flake check` only runs checks the flake exposes. If the repository does not define a flake formatter, use its pinned formatter (for example, `nixfmt` or Alejandra) rather than choosing a different style.

## Tips

- For a non-flake project, follow its `default.nix`, `shell.nix` or contribution guide instead of assuming flake commands apply.
- Check the exact package and test outputs before building; names and supported systems vary between flakes.
- Avoid `nix flake update` unless dependency updates are part of the task, since it changes the lock file.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Before contributing, run the project's documented checks and formatter, then inspect `git diff --check` and the final diff.

Further reading: the Nix reference for [`nix flake show`](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-flake-show.html), [`nix develop`](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-develop.html), [`nix flake check`](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-flake-check.html), [`nix build`](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-build.html) and [`nix fmt`](https://nix.dev/manual/nix/2.35/command-ref/new-cli/nix3-fmt.html).

Back to [all languages](README.md) · [Guide](../guide/README.md)
