# JavaScript quickstart

How JavaScript projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open JavaScript issues: [JavaScript issue list](../issues/by-language/javascript.md) · [TypeScript issues](../issues/by-language/typescript.md)

## Setup

- Install Node.js with a version manager such as [fnm](https://github.com/Schniz/fnm) or nvm, using the version in `.nvmrc`, `.node-version` or `engines` in `package.json`.
- Run `corepack enable` so the project's pinned package manager (`packageManager` in `package.json`: npm, pnpm or Yarn) is used automatically.

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `npm ci`, `pnpm install --frozen-lockfile` or `yarn install --immutable` (match the lockfile) |
| Run tests | `npm test`, or the `test` script in `package.json` (Vitest, Jest, Mocha, node:test) |
| Run one test file | `npx vitest run path/to/file.test.js` or `npx jest path/to/file.test.js` |
| Lint and format | `npm run lint`, `npx eslint .`, `npx prettier --check .` |
| Build | `npm run build` |

## Tips

- Look at the `scripts` section of `package.json`: it is the project's real command list.
- Use the package manager the lockfile belongs to (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lock`). Mixing them creates noisy lockfile changes reviewers will reject.
- In monorepos (a `packages/` folder, `pnpm-workspace.yaml`, Nx, Turborepo), run commands for one package, for example `pnpm --filter <name> test`.
- Many projects need a changeset (`npx changeset`) or Conventional Commit titles for releases.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
