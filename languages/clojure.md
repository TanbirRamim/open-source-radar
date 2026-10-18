# Clojure quickstart

How Clojure projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Clojure issues: [Clojure issue list](../issues/by-language/clojure.md)

## Setup

- Install Clojure from [clojure.org](https://clojure.org/guides/install_clojure) (the `clojure` CLI uses `deps.edn` for dependencies) or install [Leiningen](https://leiningen.org/) if the project uses a `project.clj`.
- Check the installation with `clojure -Sdescribe` (Clojure CLI) or `lein version` (Leiningen).
- Prefer the project's build file: `deps.edn` means the Clojure CLI, `project.clj` means Leiningen.

## Common commands

| Task | Usual command |
| --- | --- |
| Run the project's test suite (deps.edn) | `clojure -X:test` |
| Run the project's test suite (Leiningen) | `lein test` |
| Run a single test namespace | `lein test :only my.ns-test` |
| Start a REPL | `clojure` (or `lein repl`) |
| Lint | `clj-kondo --lint src test` |
| Check formatting | `cljfmt check` |
| Apply formatting | `cljfmt fix` |

## Tips

- Check the `deps.edn` or `project.clj` first: it names the test runner and any aliases the project expects you to use.
- Many projects run `clj-kondo` in CI, so run it locally before pushing.
- Some projects pin a Clojure version in `deps.edn`; use the Clojure CLI to resolve it rather than assuming the latest.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
