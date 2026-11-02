# Perl quickstart

How Perl projects are usually set up and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Perl issues: [Perl issue list](../issues/by-language/perl.md)

## Setup

- Install the Perl version used by the project. See the [Perl installation instructions](https://www.perl.org/get.html); Windows users can use [Strawberry Perl](https://strawberryperl.com/).
- Check the README, CI, `cpanfile`, `Makefile.PL` or `Build.PL` for version and dependency requirements.
- Install [cpanminus](https://metacpan.org/pod/App::cpanminus) using its documented setup. If the project uses [Carton](https://metacpan.org/pod/Carton), install it with `cpanm Carton`.
- Install development tools as the project documents. Common tools are [Perl::Tidy](https://metacpan.org/pod/Perl::Tidy) and [Perl::Critic](https://metacpan.org/pod/Perl::Critic), available with `cpanm Perl::Tidy Perl::Critic`.

## Common commands

| Task | Usual command |
| --- | --- |
| Check installed versions | `perl -v` and `cpanm --version` |
| Run a script | `perl path/to/script.pl` |
| Install dependencies | `cpanm --installdeps .` |
| Install Carton dependencies | `carton install` (when the project uses Carton) |
| Run tests | `prove -lr t` |
| Run one test file | `prove -lv t/example.t` |
| Run tests with Carton dependencies | `carton exec prove -lr t` |
| Format a file with a backup | `perltidy -b path/to/script.pl` |
| Lint | `perlcritic lib t` (adjust paths to the project) |

## Tips

- Perl modules usually live in `lib/` and tests in `t/`. The `-l` option adds `lib/` to the test library path; `-r` searches test directories recursively.
- Use `carton exec` for commands that need dependencies installed by Carton. Follow the project's policy for `cpanfile.snapshot`; avoid unrelated dependency updates.
- Some distributions require a build before testing. Follow their documented `Makefile.PL` or `Build.PL` workflow, especially when native extensions need compilation.
- Respect `.perltidyrc` and `.perlcriticrc`. Perl::Tidy formats code; Perl::Critic checks coding policies. Formatting with `-b` creates `.bak` files; keep those out of your commit.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting, backup files or dependency changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
