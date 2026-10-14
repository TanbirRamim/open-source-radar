# 10. Reading a codebase

A common first wall is opening a project with thousands of files and not knowing where to start. You don't need to understand all of it, only the path from the issue to the code you'll change.

## Where to start looking

When you pull down a new repository, do not try to read every file. Use these entry points instead:

- **Read the foundational documentation:**
  - **`README.md`:** Explains what the project actually does, how it is structured, and how to set up and run the app on your computer.
  - **`CONTRIBUTING.md`:** Explains the project's rules for contributors, including code style guidelines, how to open pull requests, and how maintainers expect you to submit changes.
- **Find and run the tests:**
  - **What are tests?** Tests are separate files of code written to automatically check if the app works correctly without requiring manual clicks through every feature.
  - **Where do they live?** Look for a dedicated `tests/` or `test/` folder at the root level, or check next to source files for filenames like `auth.test.js` or `auth_spec.rb`.
  - **How to run them:** Check `README.md` or `CONTRIBUTING.md` for the exact command (such as `npm test`, `pytest`, or `cargo test`). Running them verifies your setup works.
- **Search for the error text or the UI string from the issue:** If your issue mentions a specific error message or button label, use your editor's global search (`Ctrl+Shift+F` or `Cmd+Shift+F`) to find exactly where that text is defined in the code.

## Git archaeology

When you find the file you need to change, Git can tell you its history:

| Command | What it does |
| --- | --- |
| `git log -p path/to/file` | See every change ever made to a file and why |
| `git blame path/to/file` | See who wrote every line and in which commit |

## Tracing execution and history

- **Trace from the entry point:** Find where execution starts (such as `main()`, an API route handler, or the primary UI component) and follow function calls down into the logic.
- **Look at recent merged pull requests:** Search through closed PRs in the repository that touched the same area. They serve as blueprints for how maintainers expect changes to be formatted and tested.

## Checklist

- [ ] I read `README.md` to understand what the project does and how to run it.
- [ ] I read `CONTRIBUTING.md` to learn the project's rules and style guidelines.
- [ ] I found the test suite, ran it, and made sure all tests pass locally.
- [ ] I searched for the error text or UI string from the issue to locate relevant files.
- [ ] I checked recent merged PRs or git history for context on conventions.

Back to the [guide index](README.md) · Find your next issue in the [issue index](../issues/README.md).
