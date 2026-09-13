# C quickstart

How C projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open C issues: [C issue list](../issues/by-language/c.md)

## Setup

- Install a compiler and the build system the project uses (look for `Makefile`, `CMakeLists.txt`, `meson.build` or `configure.ac`).

## Common commands

| Task | Usual command |
| --- | --- |
| Autotools | `./autogen.sh && ./configure && make && make check` |
| CMake | `cmake -S . -B build && cmake --build build && ctest --test-dir build` |
| Meson | `meson setup build && meson compile -C build && meson test -C build` |

## Tips

- Many C projects review by mailing list or have strict commit message rules; read the contributing guide first.
- Use AddressSanitizer (`-fsanitize=address`) to find memory bugs quickly.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
