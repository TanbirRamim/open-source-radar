# 8. Reviews, feedback and rejection

Opening the pull request is the middle of the process, not the end. How you handle review decides whether it gets merged.

## When CI fails

1. Open the failing check and read the log from the first error, not the last line.
2. Decide whether your change caused it:
   - **Formatting or lint failure:** run the formatter or linter locally, commit the result.
   - **A test you touched fails:** fix it locally, push again.
   - **An unrelated test fails** that also fails on the default branch, or a job that looks flaky (timeouts, network errors): say so in a comment with a link to the same failure elsewhere. Do not try to fix unrelated failures in your PR unless asked.
3. Push fixes as new commits unless the project asks you to squash.

Many projects require a maintainer to approve CI runs for first-time contributors. If checks say "awaiting approval", that is normal: wait.

## When you get change requests

- **Read every comment before replying.** Some depend on each other.
- **Make the requested changes, or explain why not.** Disagreeing is fine if you give a reason; ignoring a comment is not.
- **Reply to each comment** with what you did ("Done in abc123" or "Changed to use the existing helper"). Let the reviewer resolve conversations unless the project asks you to.
- **Push, then re-request review** using the button on the pull request, or leave a short comment saying it is ready again.
- **Keep the scope.** If a reviewer asks for something much larger, suggest a follow-up issue instead of growing the pull request.

Review comments are about the code, not about you. Even experienced contributors get many rounds of feedback in a new project.

## Automated reviewers

Some projects use bots that post automated reviews. Treat their comments as suggestions: fix real problems they find, and politely note when a suggestion does not apply. Human maintainers make the final call.

## When nothing happens

Silence is common and usually means "busy", not "no".

- After a week or two, one polite ping (chapter 7).
- Check whether the project has a review queue or labels like `waiting-on-review`.
- Keep your branch mergeable: resolve conflicts when they appear.
- After a month or more, you can ask whether the change is still wanted. If not, closing it yourself is fine and appreciated.

## When your pull request is closed

It happens to everyone. Common reasons:

| Reason | What to do |
| --- | --- |
| Someone else fixed it first | Close yours, thank them, pick another issue sooner after it is filed next time |
| The maintainers want a different approach | Ask if they would accept a revised version, or let them do it their way |
| Out of scope for the project | Accept it; ask whether a plugin or separate package makes sense |
| Low quality or unclear | Read the feedback carefully; your next PR in that project needs to be clearly better |
| Closed by automation | Read the bot's message and the workflow file; fix what it asks for or contact maintainers |
| No response, closed as stale | Ask politely whether they would like it reopened; if not, move on |

A closed pull request with a polite, constructive reply still leaves a good impression.

## After the merge

- Delete your branch (GitHub offers a button).
- Update your fork's default branch: `git fetch upstream && git switch main && git rebase upstream/main && git push`.
- Note what you learned about the project's process. Your second pull request there will be much faster.

## Checklist

- [ ] I read CI logs from the first error, and separated my failures from pre-existing ones.
- [ ] I replied to every review comment and re-requested review.
- [ ] I kept the scope of the pull request small.
- [ ] I followed up politely, at most once a week.

Next: [Keep going](09-keep-going.md)
