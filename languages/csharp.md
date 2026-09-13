# C# quickstart

How C# projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open C# issues: [C# issue list](../issues/by-language/csharp.md)

## Setup

- Install the [.NET SDK](https://dotnet.microsoft.com/download). A `global.json` in the repository pins the SDK version.

## Common commands

| Task | Usual command |
| --- | --- |
| Restore and build | `dotnet build` |
| Run tests | `dotnet test` |
| One test project | `dotnet test tests/MyProject.Tests` |
| Filter tests | `dotnet test --filter FullyQualifiedName~ParserTests` |
| Format | `dotnet format --verify-no-changes` |

## Tips

- Solutions (`.sln`/`.slnx`) can contain many projects; build the one you change.
- Check `Directory.Build.props` for warnings treated as errors.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
