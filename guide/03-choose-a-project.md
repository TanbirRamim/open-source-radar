# 3. Choose a project

The project matters more than the issue. A welcoming, active project will review your pull request in days. An inactive or overloaded one may never look at it, however good it is.

## Start from what you use

The best first project is one you already use: a library in your own code, a tool you run every day, an app you like. You understand what it should do, you can test your change for real, and you care about the result.

If nothing comes to mind, browse the [issue index](../issues/README.md) by the language you know best, and look at which projects keep appearing.

## Signs of a healthy, welcoming project

Check these on the repository page. Five minutes here saves weeks of waiting.

| Check | Where to look | Good sign |
| --- | --- | --- |
| Recent activity | Commits tab, "last commit" date | Commits in the last few weeks |
| Merged outside contributions | **Pull requests → Closed**, filter `is:merged` and look at authors | Pull requests from people who are not maintainers were merged in the last month |
| Review speed | Open a few recently merged PRs from outsiders | First response within days, not months |
| Contributing guide | `CONTRIBUTING.md` in the root, `.github/` or `docs/` | Exists and explains setup and testing |
| Newcomer labels | Issues, filter by `good first issue` or `help wanted` | Labels are used, and labeled issues get picked up |
| Tone | Read a few issue threads | Maintainers are patient and specific, even when saying no |
| Code of conduct | `CODE_OF_CONDUCT.md` | Exists |
| CI | Checks on recent PRs | Tests run automatically on pull requests |

A quick search that shows merged PRs from outside contributors, for any repository (replace `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Look at the authors: if every merged PR is from the same two people, outside contributions may not be a priority there.

## Warning signs

- **Hundreds of open pull requests with no review.** Yours will join the queue.
- **A contributing guide that says the project is not accepting pull requests**, or only accepts them for issues with a specific label. Some popular projects work this way. Respect it.
- **Every recent issue already has several competing pull requests.** Popular projects often get drive-by PRs within hours of a bug being filed. You can still contribute there, but pick less contested work (docs, tests, older confirmed bugs) or a smaller project.
- **Maintainers asking people to stop opening low-effort pull requests.** Read those threads: they tell you exactly what not to do.
- **No commits in months.** The project may be finished, or abandoned.

## Big project or small project?

| | Large, famous project | Smaller, active project |
| --- | --- | --- |
| Competition for easy issues | Very high | Low |
| Review speed | Varies a lot; often slow for outsiders | Often fast and personal |
| Process | Formal: templates, CLAs, strict CI | Lighter |
| Mentorship | Structured programs sometimes exist | Direct contact with the maintainer |
| Signal on your profile | Strong name recognition | Strong if you become a regular |

A good strategy: make your first one or two contributions in a smaller, active project where you get quick feedback, then take what you learned to bigger ones.

## Checklist

- [ ] The project had commits in the last month.
- [ ] It merged pull requests from outside contributors recently.
- [ ] It has a contributing guide, and I have read it.
- [ ] I can build and run it on my machine (chapter 5 covers this).

Next: [Find an issue you can finish](04-find-an-issue.md)
