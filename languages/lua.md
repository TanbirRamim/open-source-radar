# Lua quickstart

How Lua projects are usually set up and checked. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Lua issues: [Lua issue list](../issues/by-language/lua.md)

## Setup

- Install the Lua version used by the project and [LuaRocks](https://luarocks.org/), using your package manager or the official install instructions.
- Check the project's README and `.rockspec` for its Lua version and dependencies.

## Common commands

| Task | Usual command |
| --- | --- |
| Check installed versions | `lua -v` and `luarocks --version` |
| Run a script | `lua path/to/script.lua` |
| Install dependencies | `luarocks install --only-deps <name>.rockspec` |
| Install Busted | `luarocks install busted` |
| Install Luacheck | `luarocks install luacheck` |
| Run tests | `busted` (when the project uses Busted) |
| Run one test file | `busted spec/path_spec.lua` |
| Tests via the rockspec | `luarocks test` |
| Lint | `luacheck .` |
| Check formatting | `stylua --check .` |
| Format | `stylua .` |

## Tips

- Check the project configuration and CI for its Lua version, test command and lint rules; projects may use LuaJIT instead of the standard interpreter.
- Install and run Busted, Luacheck and StyLua the way the project documents. StyLua is a formatter; Luacheck is a linter.
- A lot of open Lua issues are in Neovim plugins. Those usually run tests inside Neovim (plenary.nvim, mini.test or busted through `nlua`), so look for a `make test` target or a `scripts/` folder instead of calling `busted` directly.
- Install StyLua from its GitHub releases or `cargo install stylua`; it isn't a LuaRocks package. Settings live in `stylua.toml` or `.stylua.toml`.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
