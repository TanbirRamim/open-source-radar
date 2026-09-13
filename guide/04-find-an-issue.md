# 4. Find an issue you can finish

A good first issue is small, clearly described, reproducible, and not already being worked on by someone else. The last point is where most newcomers lose time.

## Where to look

- **This repository's [issue index](../issues/README.md)** and [website](https://tanbirramim.github.io/open-source-radar/): open newcomer-labeled issues, already filtered to exclude ones with an assignee or a linked open pull request.
- **The project's own issue tracker**, filtered by its newcomer labels.
- **GitHub search**, for example:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` hides assigned issues and `-linked:pr` hides issues that already have a pull request connected. Add `updated:>2026-06-01` (use a recent date) to skip stale ones.

## Labels you will see

| Label | Usually means |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | Maintainers think a newcomer can do it, often with guidance |
| `help wanted`, `PR welcome`, `up-for-grabs` | Maintainers want someone else to do it; not always small |
| `bug`, `confirmed`, `has: repro` | A real defect; `confirmed` means a maintainer reproduced it |
| `needs-triage`, `needs-info`, `question` | Not ready: the problem is not understood yet |
| `design`, `rfc`, `discussion`, `blocked` | Not ready for a pull request; a decision is pending |

Each project defines its own labels. Check the label descriptions on the project's **Issues → Labels** page.

## Is anyone already working on it?

Before you write a line of code, check all of these:

1. **Assignees.** If someone is assigned, it is taken.
2. **Linked pull requests.** Look at the right sidebar ("Development") and the timeline for "linked a pull request" or "mentioned this issue" events from PRs. An open PR means it is taken; a closed unmerged one may mean the approach was rejected, so read why.
3. **Comments.** Look for "I'd like to work on this" or "working on it". If the claim is recent (a couple of weeks) and the person has not gone silent, pick something else.
4. **Search open pull requests** for the issue number or keywords from the title. Not every PR links the issue properly.

If a claim is old and the person went silent, it is usually fine to ask politely: "Hi @name, are you still working on this? If not, I'd be happy to pick it up." Then wait a few days.

## Can you finish it?

Estimate honestly. A good first issue for you:

- **Has a clear expected behaviour.** You can say in one sentence what should happen instead.
- **Is reproducible.** The issue has steps, a snippet, or a failing command. If not, reproducing it is your first task, and posting the reproduction is already a contribution.
- **Is local.** You can guess which file or function is involved. Search the codebase for the error message or the function name mentioned in the issue.
- **Does not need a design decision.** If maintainers are still discussing *how* it should work, wait.
- **Runs on your machine.** Avoid Windows-only bugs if you are on macOS, GPU bugs without a GPU, and so on.

## A quick way to size an issue

Spend 20 to 30 minutes before committing to it:

1. Clone the project and run its test suite once (chapter 5).
2. Reproduce the bug, or find the place in the code for the feature.
3. Find the existing test file for that area.

If you got through all three, the issue is probably a good size. If you are still lost after 30 minutes, try a different issue, or ask a specific question on the issue (chapter 7).

## Checklist

- [ ] No assignee, no linked open PR, no recent claim in the comments.
- [ ] I can state the expected behaviour in one sentence.
- [ ] I reproduced the problem, or I know exactly where the change goes.
- [ ] Maintainers are not still debating the approach.

Next: [Your first pull request, step by step](05-first-pull-request.md)
