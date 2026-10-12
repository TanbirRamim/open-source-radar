# Zig quickstart

How Zig projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Zig issues: [Zig issue list](../issues/by-language/zig.md)

## Setup

- Install Zig from [ziglang.org](https://ziglang.org/download/). Check the project's `build.zig.zon` for `minimum_zig_version` when present, and use a compatible compiler.
- Check the installation with `zig version`.
- To create a starter project with the installed Zig version, run `zig init` in a new, empty project directory.

## Common commands

| Task | Usual command |
| --- | --- |
| Show compiler version | `zig version` |
| Show build options | `zig build --help` |
| Build | `zig build` |
| Run tests defined by the build script | `zig build test` |
| Format Zig source files | `zig fmt src/` (if the project uses `src/`) |
| Check formatting without changing files | `zig fmt --check src/` (if the project uses `src/`) |

## Tips

- Check `build.zig` and `build.zig.zon` before building; available build steps and the required Zig version vary by project.
- `zig build test` works when the project's build script defines a `test` step.
- Use the Zig documentation for the version installed by the project, rather than assuming the latest version is compatible.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
