# Java quickstart

How Java projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Java issues: [Java issue list](../issues/by-language/java.md)

## Setup

- Install a JDK (for example with [SDKMAN!](https://sdkman.io) or your package manager). Check the project's docs or build file for the required version.
- Use the wrapper scripts in the repository (`./mvnw` or `./gradlew`) instead of a globally installed Maven or Gradle.

## Common commands

| Task | Maven | Gradle |
| --- | --- | --- |
| Build without tests | `./mvnw -DskipTests install` | `./gradlew assemble` |
| Run tests | `./mvnw test` | `./gradlew test` |
| One module | `./mvnw -pl module -am test` | `./gradlew :module:test` |
| One test class | `./mvnw test -Dtest=MyTest` | `./gradlew test --tests MyTest` |
| Style checks | `./mvnw checkstyle:check` or `spotless:check` | `./gradlew spotlessCheck` or `checkstyleMain` |

## Tips

- Multi-module builds are slow the first time. Build only the module you need with its dependencies.
- If builds run out of memory, set `MAVEN_OPTS=-Xmx2g` or `org.gradle.jvmargs` in `gradle.properties`.
- Formatting is often enforced by Spotless; run `spotlessApply` before committing.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
