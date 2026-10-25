# Scala quickstart

How Scala projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Scala issues: [Scala issue list](../issues/by-language/scala.md)

## Setup

- Install Java (JDK) from [Adoptium](https://adoptium.net/) or your package manager.
- Install Scala using [Scala's official installation guide](https://www.scala-lang.org/download/).
- For sbt projects, install [sbt](https://www.scala-sbt.org/1.x/docs/Setup.html).
- For Scala CLI projects, follow the [Scala CLI installation guide](https://scala-cli.virtuslab.org/install/).

## Common commands

Task | Usual command
--- | ---
Compile | `sbt compile`
Run tests | `sbt test`
Format check | `sbt scalafmtCheckAll`
Format code | `sbt scalafmtAll`
Check and fix common issues | `sbt scalafix`
Run a Scala CLI project | `scala run .`
Compile with Scala CLI | `scala compile .`
Run tests with Scala CLI | `scala test .`

## Tips

- Check `build.sbt` to see the Scala version and dependencies used by the project.
- Check `project/plugins.sbt` for sbt plugins such as scalafmt and scalafix.
- Some projects use Scala 2 while others use Scala 3. Follow the version specified by the project.
- Scala CLI commands are useful for small projects, while sbt is common in larger projects.
- Check the project's `README.md` and `CONTRIBUTING.md` for project-specific commands.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
