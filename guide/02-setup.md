# 2. Set up your tools

You need Git, a GitHub account, a way to authenticate, an editor, and the toolchain for the language of the project you pick. Setting this up once takes about an hour.

## Git

Install Git:

- **macOS:** `xcode-select --install` (installs Git with the Command Line Tools), or `brew install git` with [Homebrew](https://brew.sh).
- **Windows:** [Git for Windows](https://git-scm.com/download/win). It includes Git Bash, a terminal that runs the commands in this guide.
- **Linux:** your package manager, for example `sudo apt install git` or `sudo dnf install git`.

Tell Git who you are. Use the same email as your GitHub account (or GitHub's private noreply address, see below) so your commits are linked to your profile:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Keep your email private (optional)

GitHub gives every account a noreply address like `12345678+username@users.noreply.github.com`. Find yours under **Settings → Emails**, enable **Keep my email addresses private**, and use that address as `user.email`. Commits still count on your profile.

> **Common mistake:** committing with an email that is not added to your GitHub account. The commits show up without your avatar and do not count on your profile. Check with `git config user.email` and compare it with **Settings → Emails**.

## A GitHub account and authentication

1. Create an account at [github.com](https://github.com). Pick a professional username; it appears on every contribution.
2. Enable two-factor authentication under **Settings → Password and authentication**. Many organizations require it.
3. Set up a way for Git to authenticate. The easiest is the GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: see cli.github.com
gh auth login          # choose GitHub.com, HTTPS, and log in with a browser
gh auth setup-git      # lets git push over HTTPS using that login
```

Alternatively, [add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and clone with `git@github.com:` URLs.

## An editor

Use whatever you are comfortable with. [VS Code](https://code.visualstudio.com) is a common choice: it has good Git integration, and the official language extensions give you formatting and error checking. JetBrains IDEs, Neovim, Zed and Emacs are all fine.

Two settings save you from review comments:

- **Format on save** with the project's formatter (Prettier, Black, rustfmt, gofmt, and so on).
- **Respect `.editorconfig`**. Many projects ship one to set indentation and line endings.

## The Git commands you will actually use

| Command | What it does |
| --- | --- |
| `git clone URL` | Download a repository |
| `git status` | See what changed |
| `git switch -c fix-typo` | Create and switch to a new branch |
| `git add path/to/file` | Stage a change for the next commit |
| `git commit -m "message"` | Record staged changes |
| `git push -u origin fix-typo` | Upload your branch |
| `git fetch upstream` | Download the latest changes from the original project |
| `git rebase upstream/main` | Replay your commits on top of those changes |
| `git log --oneline -10` | See recent commits |
| `git diff` | See unstaged changes (`git diff --staged` for staged) |

If you have never used Git, spend 30 minutes on [Learn Git Branching](https://learngitbranching.js.org) first. It is interactive and covers exactly what you need.

## Language toolchains

Install the toolchain for the project you choose, using the version the project asks for (look for files like `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod`, `.tool-versions`). The [language quickstarts](../languages/README.md) list the usual commands per language.

Version managers make this painless:

- **Several languages:** [mise](https://mise.jdx.dev) or [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) or nvm, plus `corepack enable` for pnpm and Yarn
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** the official installer, or your package manager; Go downloads newer toolchains itself when `go.mod` asks for one

## Checklist

- [ ] `git --version` works and `git config user.email` matches an email on my GitHub account.
- [ ] Two-factor authentication is on.
- [ ] `gh auth status` (or `ssh -T git@github.com`) shows I can authenticate.
- [ ] My editor formats on save.

Next: [Choose a project](03-choose-a-project.md)
