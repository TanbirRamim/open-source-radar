# Kotlin quickstart

How Kotlin projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Kotlin issues: [Kotlin issue list](../issues/by-language/kotlin.md)

## Setup

- Install a JDK (SDKMAN! or your package manager) and use the repository's `./gradlew`.

## Common commands

| Task | Usual command |
| --- | --- |
| Build | `./gradlew assemble` |
| Run tests | `./gradlew test` (Android: `./gradlew testDebugUnitTest`) |
| One module | `./gradlew :module:test` |
| Lint and format | `./gradlew ktlintCheck`, `./gradlew detekt`, or `./gradlew spotlessCheck` |

## Tips

- Android projects need the Android SDK; the project's docs say which version.
- Kotlin Multiplatform projects may need Xcode for iOS targets. Build only the JVM or Android targets if you do not have it.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
