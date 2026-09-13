# Rust quickstart

How Rust projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Rust issues: [Rust issue list](../issues/by-language/rust.md)

## Setup

- Install [rustup](https://rustup.rs). A `rust-toolchain.toml` in the repository selects the right toolchain automatically.

## Common commands

| Task | Usual command |
| --- | --- |
| Build | `cargo build` |
| Run tests | `cargo test` (in a workspace, prefer `cargo test -p <crate>`) |
| Run one test | `cargo test -p <crate> test_name` |
| Format | `cargo fmt --all -- --check` |
| Lint | `cargo clippy --all-targets -- -D warnings` |
| Docs | `cargo doc --no-deps` |

## Tips

- Large workspaces take a long time to build. Build and test only the crate you change.
- Clippy warnings usually fail CI. Run clippy with the same flags as the CI workflow.
- Some projects want changelog entries or `insta` snapshot updates (`cargo insta review`).

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
