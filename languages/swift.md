# Swift quickstart

How Swift projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Swift issues: [Swift issue list](../issues/by-language/swift.md)

## Setup

- On macOS install Xcode or the Command Line Tools; on Linux and Windows use the [swift.org](https://www.swift.org/install/) toolchain.

## Common commands

| Task | Usual command |
| --- | --- |
| Build a package | `swift build` |
| Run tests | `swift test` |
| One test | `swift test --filter MyTests/testName` |
| Format | `swift format lint -r Sources Tests` or `swiftformat --lint .` |
| Xcode project | `xcodebuild test -scheme <Scheme> -destination 'platform=macOS'` |

## Tips

- Swift packages (`Package.swift`) work without Xcode; iOS app projects need it.
- SwiftLint (`swiftlint`) is common in app projects.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
