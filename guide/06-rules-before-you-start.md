# 6. Rules to check before you start

Every project has rules for contributions. Some are just conventions; others decide whether your pull request can be merged at all, or whether it gets closed automatically. Check them **before** you write code.

The [issue index](../issues/README.md) shows automatically detected hints for each project. They are hints, not guarantees: always read the project's own files.

| Note in the index | Meaning |
| --- | --- |
| ⚠️ AI restricted | The project's contribution files appear to ban or heavily restrict AI-generated contributions |
| 🤖 disclose AI use | The project asks you to disclose AI assistance |
| 📄 AI policy | The project has an AI policy; read it |
| ✍️ CLA | You probably need to sign a Contributor License Agreement |
| 🔏 DCO | Commits probably need a `Signed-off-by` line |

## Where the rules live

Look in all of these, not just the README:

- `CONTRIBUTING.md` (root, `.github/`, or `docs/`)
- `.github/PULL_REQUEST_TEMPLATE.md` and issue templates
- `CODE_OF_CONDUCT.md`
- `AI_POLICY.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.claude/`, `.cursor/rules`
- `DEVELOPMENT.md`, `docs/development/`, or a contributing page on the project website
- `.github/workflows/` (automation that labels, checks or closes pull requests)

## Contributor License Agreements (CLA)

A CLA is a legal agreement that gives the project (or the company behind it) rights to use your contribution. Many company-backed projects require one.

- Usually a bot comments on your first pull request with a link. You sign once, online, and it covers future contributions to that project or organization.
- Some CLAs are tied to an organization-wide account, such as the Linux Foundation's EasyCLA (used by many CNCF projects) or Google's CLA.
- **Read what you sign.** If you contribute on behalf of an employer, your employer may need to sign a corporate CLA.

## Developer Certificate of Origin (DCO)

The DCO is a lighter alternative to a CLA: you certify that you have the right to submit the code. You do it by adding a sign-off line to every commit:

```bash
git commit -s -m "fix: handle empty username"
# adds: Signed-off-by: Your Name <you@example.com>
```

A DCO bot checks every commit in the pull request. If you forgot, fix it with:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

The name and email in the sign-off must match your commit author.

## AI-assisted contributions

Maintainers have seen a flood of low-quality, AI-generated pull requests, and many projects now have explicit rules. They vary a lot:

- **Allowed with the usual standards.** You are responsible for every line and must be able to explain it.
- **Allowed with disclosure.** You must say in the PR description which tool you used and for what, or add a trailer such as `Assisted-by:` to commits.
- **Human-written communication only.** AI may help with code, but issue comments and PR descriptions must be written by you.
- **Restricted or banned.** Some projects do not accept AI-generated code or documentation at all, or do not allow AI agents to open pull requests.

Whatever the policy, these hold everywhere:

- You must understand and be able to defend every change you submit.
- Never let a tool open pull requests or post comments in your name without reviewing them yourself.
- Follow the disclosure rules exactly when a project has them. Hiding AI use where disclosure is required is a fast way to get banned from a project.

## Anti-spam and first-time-contributor automation

Because of spam, some projects run workflows that automatically close or label pull requests. Rules seen in real projects include:

- closing pull requests from accounts that opened PRs to many unrelated repositories in a short time
- closing PRs from authors with recently rejected pull requests elsewhere
- closing PRs from branches named after AI tools (for example `claude/...` or `codex/...`)
- requiring a linked issue, or an issue label like `help wanted`, before a PR is accepted
- requiring a filled-in PR template with every checkbox answered
- holding CI until a maintainer approves it for first-time contributors (this one is normal and harmless)

Look at `.github/workflows/` for files with names like `close-spam`, `first-interaction`, or `pr-checks` to see what applies. The practical advice: contribute steadily to a few projects rather than opening pull requests across dozens of repositories in one week.

## Legal statements and licensing

A few projects ask you to include a statement in your pull request, for example that you wrote the code and license it under the project's terms. Only make statements that are true. By submitting a contribution you generally license it under the project's license, so check that license is acceptable to you (and to your employer, if relevant).

## Checklist

- [ ] I read the contributing guide, PR template, and any AI policy or agent instructions.
- [ ] I know whether a CLA or DCO sign-off is needed.
- [ ] I know the project's commit message and PR title conventions.
- [ ] I checked `.github/workflows/` for automation that could close my PR.
- [ ] If AI helped me, I know whether and how I must disclose it.

Next: [Talking to maintainers](07-communication.md)
