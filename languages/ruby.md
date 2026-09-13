# Ruby quickstart

How Ruby projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Ruby issues: [Ruby issue list](../issues/by-language/ruby.md)

## Setup

- Install Ruby with a version manager such as rbenv, chruby or mise, using the version in `.ruby-version`.

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `bundle install` |
| Run tests | `bundle exec rake`, `bundle exec rspec`, or `bin/rails test` |
| One test file | `bundle exec rspec spec/models/user_spec.rb` |
| Lint | `bundle exec rubocop` (or `bundle exec standardrb`) |

## Tips

- Rails apps often need a database; many can run tests with SQLite, check `config/database.yml`.
- Add a `CHANGELOG.md` entry when the project keeps one.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
