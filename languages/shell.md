# Shell quickstart

How shell-script projects (Bash, POSIX sh, zsh plugins, dotfiles, installers) are usually checked and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Shell issues: [Shell issue list](../issues/by-language/shell.md)

## Setup

- Look at the shebang (`#!/usr/bin/env bash` or `#!/bin/sh`) before you change a script. A `sh` script has to stay POSIX, so no arrays, `[[ ]]` or `local -n`.
- macOS ships Bash 3.2. If the project needs newer Bash, install it with `brew install bash` and check with `bash --version`.
- Install [ShellCheck](https://www.shellcheck.net/) and [shfmt](https://github.com/mvdan/sh) (`brew install shellcheck shfmt`, or your package manager).

## Common commands

| Task | Usual command |
| --- | --- |
| Lint | `shellcheck path/to/script.sh` |
| Check formatting | `shfmt -d .` (run `shfmt -w .` to fix) |
| Syntax check only | `bash -n script.sh` |
| Run tests | `bats test/` when the project uses [bats-core](https://github.com/bats-core/bats-core), or `make test` |
| One test file | `bats test/install.bats` |
| Trace a script | `bash -x script.sh` |

## Tips

- Check CI (`.github/workflows/`) for the exact ShellCheck and shfmt flags; `shfmt -i 2 -ci` style options change the output a lot.
- Quote your variables (`"$file"`) unless the project clearly does otherwise. Most ShellCheck warnings in pull requests are missing quotes.
- Test on both Linux and macOS when you touch `sed -i`, `date`, `readlink` or `grep -P`, because GNU and BSD versions behave differently.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] ShellCheck and the formatter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
