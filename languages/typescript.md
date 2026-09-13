# TypeScript quickstart

How TypeScript projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open TypeScript issues: [TypeScript issue list](../issues/by-language/typescript.md)

## Setup

- Same setup as [JavaScript](javascript.md): Node.js from the version file, then `corepack enable`.

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `npm ci`, `pnpm install --frozen-lockfile` or `yarn install --immutable` |
| Type check | `npx tsc --noEmit`, or a `typecheck` script |
| Run tests | `npm test` (Vitest and Jest are most common) |
| Lint and format | `npm run lint`, `npx eslint .`, `npx prettier --check .`, or `npx biome check .` |
| Build | `npm run build` |

## Tips

- Type errors fail CI in most TypeScript projects, so run the type check before pushing.
- Avoid `any` and non-null assertions (`!`) as shortcuts in fixes; reviewers usually ask for proper types.
- Generated files (`dist/`, `*.d.ts` outputs) are usually not committed. Check `.gitignore`.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
