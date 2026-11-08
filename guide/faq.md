# Newcomer FAQ

Short answers to the questions people ask most before and after their first pull request. Each one links to the chapter with the full story.

## Before you start

### Do I need to ask before working on an issue?

It depends on the project. Look in `CONTRIBUTING.md`: some projects want a comment first, some assign issues with a `/claim` or `/assign` command, and some say "just open a PR". If the guide says nothing and the issue is small, opening a pull request directly is usually fine. For anything bigger, comment first so nobody wastes time. See [chapter 7](07-communication.md#claiming-an-issue).

### How do I claim an issue without sounding like everyone else?

Skip "Can I work on this?". Say what you found and what you plan to change, in two or three sentences. A maintainer can then say yes, or point you to a better approach before you write any code. There is an example in [chapter 7](07-communication.md#claiming-an-issue).

### Someone commented "I'll take this" weeks ago and never opened a PR. Can I take it?

Ask on the issue first: "Are you still working on this? If not I'd like to pick it up." If there is no answer after a few days, ask a maintainer to reassign it. Do not open a competing pull request without asking. See [chapter 4](04-find-an-issue.md#is-anyone-already-working-on-it).

### How many issues should I claim at once?

One. Claim the next one after your first pull request is open.

### I'm not sure I can finish it. Should I still try?

Yes, but pick something you can size. If you can reproduce the problem and find the code involved within an hour, it is probably a good fit. If you get stuck, it is fine to say so on the issue and unassign yourself. See [chapter 4](04-find-an-issue.md#can-you-finish-it).

## Rules and paperwork

### A bot asked me to sign a CLA. Is that normal?

Yes. A Contributor License Agreement gives the project rights to use your change. You sign once online and it covers later contributions. Read it, and if you contribute for an employer, check whether they need to sign too. See [chapter 6](06-rules-before-you-start.md#contributor-license-agreements-cla).

### The DCO check failed. How do I fix it?

Every commit needs a `Signed-off-by:` line that matches your commit author. Add it to all commits on your branch and push again:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

Use `git commit -s` from then on. See [chapter 6](06-rules-before-you-start.md#developer-certificate-of-origin-dco).

### Can I use AI tools?

Check the project's policy before you start. Some ban AI-generated contributions, some ask you to disclose it, and many say nothing. Whatever the rule, you are responsible for every line: understand it, test it, and be able to explain it in review. See [chapter 6](06-rules-before-you-start.md#ai-assisted-contributions).

### A bot closed my PR or labeled it as spam. What now?

Read the bot's message. Many projects close pull requests from first-time contributors that are not linked to an issue, or that skip the template. Fix what it asks for, or reply politely and ask a maintainer to take a look. See [chapter 6](06-rules-before-you-start.md#anti-spam-and-first-time-contributor-automation).

## After you open the pull request

### Nobody has replied. How long should I wait?

A week or two is normal. Then leave one short, polite comment asking whether it needs anything from you. Keep the branch free of conflicts while you wait. After a month, ask if the change is still wanted. See [chapter 8](08-reviews.md#when-nothing-happens).

### CI is red and I don't understand why.

Open the failing job and scroll to the first error, not the last one. Run the same command locally. If the failure is in code you did not touch, say so in the pull request; it may be a flaky test or a problem on the main branch. See [chapter 8](08-reviews.md#when-ci-fails).

### The maintainer asked for changes. Do I open a new PR?

No. Push more commits to the same branch and the pull request updates. Reply to each comment so the reviewer knows it is done. See [chapter 8](08-reviews.md#when-you-get-change-requests).

### My PR has merge conflicts.

Update your branch from the project's main branch, fix the conflicting lines, and push:

```bash
git fetch upstream
git rebase upstream/main
# fix the files, then: git add <file> && git rebase --continue
git push --force-with-lease
```

See [chapter 5](05-first-pull-request.md).

### My PR was closed without merging. Did I do something wrong?

Not always. Someone may have fixed it first, or the project wants a different approach. Read the reason, say thanks, and ask whether a revised version would help. See [chapter 8](08-reviews.md#when-your-pull-request-is-closed).

## After the merge

### Does a merged PR in a small project count?

Yes. A merged pull request is real work in public, whatever the project's size. A few merged changes in one project you care about are worth more than many one-line fixes spread across repositories. See [chapter 9](09-keep-going.md).

### What should I do next?

Stay in the same project. You already know how to build it and how its maintainers review. Pick a slightly bigger issue, help triage new ones, or review someone else's pull request. See [chapter 9](09-keep-going.md).
