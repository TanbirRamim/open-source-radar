# Vue quickstart

How Vue projects are usually set up, built, tested and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Vue issues: [Vue issue list](../issues/by-language/vue.md)

## Setup

- Install Node.js using the version in `.nvmrc`, `.node-version` or `engines` in `package.json`. If the project does not pin a version, check the current [Vue Quick Start](https://vuejs.org/guide/quick-start.html) for its supported Node.js versions.
- For a new Vue 3 app, run `npm create vue@latest` and choose optional features such as TypeScript, Vitest and ESLint as needed. This uses Vue's official `create-vue` scaffolder and Vite. Do not scaffold over an existing project.
- In an existing project, enable Corepack when its `package.json` has a `packageManager` field so you use the pinned npm, pnpm or Yarn version.
- Install dependencies with the package manager and lockfile the project already uses.

## Common commands

| Task | Usual command |
| --- | --- |
| Create a new Vue app | `npm create vue@latest` |
| Install dependencies | `npm ci`, `pnpm install --frozen-lockfile` or `yarn install --immutable` (match the lockfile) |
| Start the dev server | `npm run dev` |
| Run unit tests | `npm run test:unit` when defined, or `npx vitest run` when Vitest is installed |
| Type-check Vue SFCs | The project's type-check script; `npx vue-tsc --noEmit` for a single configured TypeScript project |
| Lint | `npm run lint` if defined, or `npx eslint .` when ESLint is configured for `.vue` files |
| Build for production | `npm run build` |

## Tips

- Check `package.json`'s `scripts` and the lockfile before running commands; script names and enabled tools depend on the scaffold and project.
- Vite does not type-check TypeScript by itself. For TypeScript projects with Vue single-file components, use the project's `vue-tsc` check or type-check script; projects with TypeScript project references may use a build-mode command such as `vue-tsc -b`.
- Vue's [testing guide](https://vuejs.org/guide/scaling-up/testing.html) recommends Vitest for Vite-based unit and component tests. Component tests commonly use [Vue Test Utils](https://test-utils.vuejs.org/guide/).
- For linting `.vue` files, use the project's ESLint configuration with [`eslint-plugin-vue`](https://eslint.vuejs.org/user-guide/); do not assume a plain JavaScript ESLint setup checks Vue templates.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Type checks, formatter and linter pass when the project provides them.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
