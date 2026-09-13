# C++ quickstart

How C++ projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open C++ issues: [C++ issue list](../issues/by-language/cpp.md)

## Setup

- Install a compiler (Clang, GCC or MSVC), CMake and Ninja. Check the README for required library dependencies; many projects use vcpkg or Conan.

## Common commands

| Task | Usual command |
| --- | --- |
| Configure | `cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Debug` (look for `CMakePresets.json` and use `cmake --preset <name>`) |
| Build | `cmake --build build` |
| Run tests | `ctest --test-dir build --output-on-failure` |
| Format | `clang-format --dry-run --Werror <files>` (uses the project's `.clang-format`) |

## Tips

- Some projects use Meson (`meson setup build && meson test -C build`) or Bazel instead of CMake.
- Build in Debug with sanitizers (`-DCMAKE_CXX_FLAGS=-fsanitize=address,undefined`) when fixing crashes.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
