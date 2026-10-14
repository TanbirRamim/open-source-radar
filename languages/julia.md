# Julia quickstart

How Julia projects are usually set up, tested and formatted. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Julia issues: [Julia issue list](../issues/by-language/julia.md)

## Setup

- Install Julia with [juliaup](https://julialang.org/install/), the official installer. Check the project's `Project.toml` `[compat]` section for the Julia versions it supports.
- Check the installation with `julia --version`.
- Work inside the project's own environment: run Julia with `--project` from the repository root so packages come from its `Project.toml` and `Manifest.toml`.

## Common commands

| Task | Usual command |
| --- | --- |
| Install the project's dependencies | `julia --project -e 'using Pkg; Pkg.instantiate()'` |
| Run the test suite | `julia --project -e 'using Pkg; Pkg.test()'` |
| Open a REPL in the project environment | `julia --project` |
| Format the source (if the project uses JuliaFormatter) | `julia -e 'using JuliaFormatter; format(".")'` |

## Tips

- Tests live in `test/runtests.jl`; `Pkg.test()` runs that file in a clean environment.
- Look for a `.JuliaFormatter.toml` file before formatting. If there isn't one, don't reformat code you didn't touch.
- [Revise.jl](https://github.com/timholy/Revise.jl) reloads your changes in a running REPL, so you don't pay the startup cost after every edit.
- In the REPL, press `]` for package mode (`st` lists packages) and Backspace to go back.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or `Manifest.toml` changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
