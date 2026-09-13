# PHP quickstart

How PHP projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open PHP issues: [PHP issue list](../issues/by-language/php.md)

## Setup

- Install PHP (Homebrew, your package manager, or [Laravel Herd](https://herd.laravel.com)) and [Composer](https://getcomposer.org).

## Common commands

| Task | Usual command |
| --- | --- |
| Install dependencies | `composer install` |
| Run tests | `vendor/bin/phpunit` or `vendor/bin/pest`, or `composer test` |
| Static analysis | `vendor/bin/phpstan analyse` or `vendor/bin/psalm` |
| Code style | `vendor/bin/php-cs-fixer fix --dry-run` or `vendor/bin/pint --test` |

## Tips

- Check the `scripts` section of `composer.json` for the project's own commands.
- Frameworks may need extensions such as `intl`, `mbstring` or `pdo_sqlite`.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
