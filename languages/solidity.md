# Solidity quickstart

How Solidity projects are usually set up and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Browse open issues: [issue index](../issues/README.md)

## Setup

- Choose the toolchain used by the project: [Foundry](https://getfoundry.sh/) or [Hardhat](https://hardhat.org/docs/getting-started). Follow its official installation instructions.
- For Foundry, check `foundry.toml` and install dependencies as the project documents. For Hardhat, use the project's required Node.js version and install its npm dependencies.
- Check the required Solidity compiler version and the project's configuration before building or testing.

## Common commands

| Task | Usual command |
| --- | --- |
| Check Foundry version | `forge --version` |
| Build with Foundry | `forge build` |
| Run Foundry tests | `forge test` |
| Run a Foundry test by name | `forge test --match-test testName` |
| Check Foundry formatting | `forge fmt --check` |
| Format with Foundry | `forge fmt` |
| Install Hardhat dependencies | `npm ci` (if the project has a `package-lock.json`) |
| Compile with Hardhat | `npx hardhat compile` |
| Run Hardhat tests | `npx hardhat test` |
| Lint with Solhint | `npx solhint 'contracts/**/*.sol'` (when configured) |
| Run Slither static analysis | `slither .` (when installed) |

## Tips

- Foundry projects usually use `foundry.toml`; Hardhat projects use a `hardhat.config.*` file. Follow their own scripts and CI commands when they differ from this list.
- Smart contracts can manage real funds. Review test failures, compiler warnings and static-analysis findings before deployment; run fuzz or invariant tests when the project provides them.
- Keep private keys, RPC credentials and deployment secrets out of commits. Review generated build artifacts before staging files.

## Before you push

- [ ] Relevant build and tests pass with the project's chosen toolchain.
- [ ] Formatting, lint and security checks pass where configured.
- [ ] No unrelated generated artifacts, dependencies or secrets are included in the diff.

Back to [all languages](README.md) · [Guide](../guide/README.md)
