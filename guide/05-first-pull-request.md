# 5. Your first pull request, step by step

This is the full workflow, from fork to open pull request. Replace `OWNER/REPO` with the project and `your-username` with your GitHub username.

## 1. Fork and clone

A **fork** is your own copy of the repository on GitHub. You push to your fork, then ask the original project (called **upstream**) to pull your changes.

```bash
gh repo fork OWNER/REPO --clone
cd REPO
git remote -v
# origin    https://github.com/your-username/REPO.git  (your fork)
# upstream  https://github.com/OWNER/REPO.git          (the original)
```

Without the GitHub CLI: click **Fork** on the repository page, then:

```bash
git clone https://github.com/your-username/REPO.git
cd REPO
git remote add upstream https://github.com/OWNER/REPO.git
```

> Large repository? `git clone --filter=blob:none URL` downloads file contents only when needed, which is much faster.

## 2. Create a branch

Never work on the default branch of your fork. Start each change from the latest upstream code:

```bash
git fetch upstream
git switch -c fix-empty-username upstream/main   # use the project's default branch name
```

Name branches after the change, like `fix-empty-username` or `docs-install-windows`.

## 3. Build it and run the tests before changing anything

Follow the project's `CONTRIBUTING.md` or `DEVELOPMENT.md`. The [language quickstarts](../languages/README.md) show the usual commands. Run the tests on the unmodified code first:

- If they pass, you have a working baseline.
- If some fail already, note which ones. Those failures are not yours, and you should mention them in your PR if they are relevant.

## 4. Reproduce the problem

Before fixing, prove the bug exists on your machine using the steps from the issue. Write down what happens and what should happen instead. If you cannot reproduce it, say so on the issue (with your version and environment) instead of guessing at a fix.

## 5. Write a failing test

Find the test file for the code you are changing and add a test that shows the bug. Run it and watch it fail. This tells you, and the reviewer, that your test really covers the bug.

Not every change needs a test (documentation fixes, for example), but bug fixes almost always do. Many projects will not merge a fix without one.

## 6. Make the smallest change that fixes it

- Change only what the issue needs. No drive-by refactors, renames, or reformatting of unrelated code: they make your pull request harder to review.
- Follow the style of the surrounding code, even if you would write it differently.
- Run the test from step 5 again. It should pass now.

## 7. Run the full checks locally

Run what the project's CI runs, at least for the area you touched:

- the test suite (or the relevant part of it)
- the formatter (for example `prettier`, `black`/`ruff format`, `cargo fmt`, `gofmt`)
- the linter (for example `eslint`, `ruff`, `clippy`, `go vet`)
- type checking if the project uses it (`tsc`, `mypy`)

Some projects also want a changelog entry or a "changeset" file. The contributing guide will say.

## 8. Commit

```bash
git add path/to/changed/files
git commit
```

Write a clear message. Follow the project's convention (look at `git log --oneline -20`). A common shape:

```text
parser: handle empty username in login prompt

An empty username made the prompt loop forever because validation
rejected it without telling the user. Show the validation error and
ask again instead.

Fixes #1234
```

- First line: short summary, often prefixed with the area or a [Conventional Commits](https://www.conventionalcommits.org) type like `fix:` or `docs:`.
- Body: what was wrong and why this change fixes it.
- `Fixes #1234` closes the issue automatically when the PR is merged.
- If the project requires DCO sign-off, use `git commit -s` (see chapter 6).

## 9. Push and open the pull request

```bash
git push -u origin fix-empty-username
gh pr create --repo OWNER/REPO --fill   # or open the link git prints, in your browser
```

Fill in the project's pull request template if it has one. Chapter 7 covers what a good description looks like. In short: what was wrong, what you changed, how you tested it, and the issue it fixes.

## 10. Keep your branch up to date

If the upstream branch moves on before your PR is merged and there are conflicts, update your branch:

```bash
git fetch upstream
git rebase upstream/main
# fix any conflicts, then: git add <files> && git rebase --continue
git push --force-with-lease
```

`--force-with-lease` is the safe way to update a branch you rewrote; it refuses to overwrite commits you do not have locally. Some projects prefer merging `upstream/main` into your branch instead of rebasing; follow their guide.

## Checklist

- [ ] Branch created from the latest upstream default branch.
- [ ] Tests passed before my change (or I noted existing failures).
- [ ] I reproduced the bug and wrote a test that failed before the fix.
- [ ] The diff contains only changes needed for this issue.
- [ ] Tests, formatter and linter pass locally.
- [ ] Commit message follows the project's convention and references the issue.
- [ ] The PR template is filled in.

Next: [Rules to check before you start](06-rules-before-you-start.md)
