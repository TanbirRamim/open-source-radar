# Dart and Flutter quickstart

How Dart and Flutter projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Dart and Flutter issues: [Dart and Flutter issue list](../issues/by-language/dart.md)

## Setup

- Install [Flutter](https://docs.flutter.dev/get-started/install) (includes Dart) or the [Dart SDK](https://dart.dev/get-dart). Tools like fvm pin the Flutter version per project.

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `dart pub get` or `flutter pub get` |
| Run tests | `dart test` or `flutter test` |
| Analyze | `dart analyze` or `flutter analyze` |
| Format | `dart format --output=none --set-exit-if-changed .` |

## Tips

- Monorepos often use Melos: `melos bootstrap`, then `melos run test`.
- Golden image tests may need updating with `flutter test --update-goldens`; only update goldens your change affects.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
