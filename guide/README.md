# The Open Source Contribution Guide

A practical path from "I want to contribute" to "my pull request got merged", written for people doing it for the first time and useful for everyone after that.

Read it in order the first time. Each chapter ends with a short checklist you can come back to.

| # | Chapter | You will learn |
| --- | --- | --- |
| 1 | [Why contribute, and what counts](01-why-contribute.md) | What you get out of it, and the many kinds of contribution besides code |
| 2 | [Set up your tools](02-setup.md) | Git, a GitHub account, SSH keys, an editor, and the command-line basics you will actually use |
| 3 | [Choose a project](03-choose-a-project.md) | How to tell a healthy, welcoming project from one that will ignore you |
| 4 | [Find an issue you can finish](04-find-an-issue.md) | Reading labels, checking whether someone already claimed it, sizing the work |
| 5 | [Your first pull request, step by step](05-first-pull-request.md) | Fork, clone, branch, build, test, commit, push, and open the PR |
| 6 | [Rules to check before you start](06-rules-before-you-start.md) | Contributing guides, CLAs, DCO sign-off, AI policies, and anti-spam bots |
| 7 | [Talking to maintainers](07-communication.md) | Claiming an issue, asking good questions, writing PR descriptions people want to review |
| 8 | [Reviews, feedback and rejection](08-reviews.md) | Handling change requests, CI failures, silence, and "no" |
| 9 | [Keep going](09-keep-going.md) | From one PR to a track record: becoming a regular, a reviewer, a maintainer |

Also useful:

- [Glossary](glossary.md): fork, upstream, rebase, squash, CI, DCO and the rest, in one line each.
- [Language quickstarts](../languages/README.md): how projects in each language are usually built and tested.
- [Issue index](../issues/README.md): open, unclaimed issues sorted by language and topic, refreshed automatically.

## The short version

1. Pick a project you use or care about, that merged pull requests from outsiders in the last month.
2. Pick an issue labeled for newcomers that nobody is assigned to and that has no linked pull request.
3. Read the contributing guide. Follow it exactly.
4. Reproduce the problem before you change anything.
5. Make the smallest change that fixes it, with a test.
6. Run the project's own tests, formatter and linter locally.
7. Open a pull request that says what was wrong, what you changed and how you checked it.
8. Respond to review politely and quickly. Repeat.
