# Haskell quickstart

How Haskell projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Haskell issues: [Haskell issue list](../issues/by-language/haskell.md)

## Setup

- Install GHC and Cabal via [GHCup](https://www.haskell.org/ghcup/) (recommended) or your package manager. Stack is an alternative that pins its own GHC.
- If the project ships a `cabal.project` or `stack.yaml`, use the toolchain it expects.

## Common commands

| Task | Usual command |
| --- | --- |
| Build | `cabal build` (or `stack build`) |
| Run tests | `cabal test` (or `stack test`) |
| Run one test | `cabal test --test-show-details=direct -t 'TestName'` |
| Format | `ormolu -m inplace $(git ls-files '*.hs')` or `fourmolu` |
| Lint | `hlint .` |
| REPL | `cabal repl` (or `stack ghci`) |

## Tips

- Check the `Makefile` or `justfile`: many projects wrap build, test and docs there.
- Cabal and Stack both cache dependencies; first builds can be slow.
- If the project uses Nix, `nix develop` then run the Cabal/Stack commands inside.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
EOF