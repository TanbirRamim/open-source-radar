# 7. Talking to maintainers

Maintainers are usually volunteers or busy engineers reviewing contributions on top of their own work. Clear, short, specific communication gets you faster and friendlier responses.

## Claiming an issue

Some projects want you to comment before starting; others say "just open a PR". Check the contributing guide. When you do comment, make it useful:

> I can reproduce this on 4.2.1: `tool --flag ""` loops forever instead of showing an error. The check in `src/prompt.ts` rejects empty input without printing the reason. I plan to print the validation message and re-prompt, with a test in `prompt.test.ts`. OK to go ahead?

That beats "Can I work on this?" because it shows you understood the problem, and it lets the maintainer correct your approach before you spend time on it.

Do not claim several issues at once, and do not claim an issue you will not start this week.

## Asking for help

When you are stuck, ask on the issue (or the project's chat, if it has one), and include:

- what you are trying to do
- what you tried
- what happened, with the exact error message or output
- your environment when it matters (OS, language version, project version)

Link to the line of code you are asking about. Then keep investigating while you wait: if you find the answer, post it.

## Writing a pull request description

Reviewers read many pull requests. Make yours easy to understand in 30 seconds.

**Good:**

> Fixes #1234.
>
> `login` re-prompted forever when the username was empty, because `validateUsername` returned an error that the prompt loop ignored. The loop now prints the validation message before asking again.
>
> Added a test in `prompt.test.ts` that fails without the change. `npm test` and `npm run lint` pass locally.

**Why it works:** it links the issue, says what was wrong and why, says what changed, and says how it was verified. No filler.

Avoid:

- Long generated summaries, bullet lists of every file changed, or headings for a ten-line change.
- Marketing language ("This PR significantly improves...").
- Claims you did not verify ("fixes all related issues").
- Leaving the template's placeholder text in place.

If there is something reviewers should know, say it directly: "I wasn't sure whether empty usernames should be allowed for custom registries, so I kept the existing behaviour there."

## Tone

- Be polite and assume good intent, including when someone is short with you.
- Thank reviewers for their time, once. You do not need to thank them for every comment.
- Do not @-mention maintainers repeatedly, or ping people who are not involved.
- Keep discussion on the issue or pull request, not in private messages, unless invited.
- Write in your own words. Maintainers want to know that a person understands the change.

## Following up

If there is no response after about a week, one polite follow-up is fine:

> Friendly ping: this is ready for review whenever someone has time. Happy to make changes.

If a project has a chat channel for contributors, asking there once is also fine. After that, leave it: some projects are simply slow.

## Checklist

- [ ] My claim comment (if needed) shows I understood the problem.
- [ ] My PR description says what was wrong, what changed, how I tested, and links the issue.
- [ ] I removed template placeholder text.
- [ ] My follow-ups are spaced out and polite.

Next: [Reviews, feedback and rejection](08-reviews.md)
