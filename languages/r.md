# R quickstart

How R projects are usually set up, tested and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open R issues: [R issue list](../issues/by-language/r.md)

## Setup

- Install R from [CRAN](https://cran.r-project.org/). RStudio is an optional IDE; it is not required to run R commands.
- Check the project's `DESCRIPTION`, `renv.lock` and README for its dependencies and setup instructions.
- If the project uses `renv` and has a `renv.lock` file, restore its recorded dependencies by running `renv::restore()` in the R console.

## Common commands

| Task | Usual command |
| --- | --- |
| Check the installed R version | `R --version` |
| Install a package | `install.packages("package_name")` (R console) |
| Restore project dependencies | `renv::restore()` (R console, when the project uses renv) |
| Run tests | `devtools::test()` (R console, when devtools is used) |
| Run one test file | `testthat::test_file("tests/testthat/test-example.R")` (R console) |
| Check an R package | `R CMD check .` (terminal, from the package directory) |
| Lint a package | `lintr::lint_package()` (R console) |
| Format a package | `styler::style_pkg()` (R console; formats files) |

## Tips

- `R CMD check` checks an R package, including its structure, metadata and tests. Run it from the package directory and follow any reported errors or warnings.
- `renv::restore()` restores dependencies recorded in `renv.lock`; it is useful for projects that manage dependencies with renv.
- `devtools::test()` runs a package's tests. Projects may use other test commands, so check their README and configuration first.
- `lintr` checks R code against configured style rules. `styler` formats R code; review the resulting changes before committing.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass when the project uses them.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
