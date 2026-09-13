# Go quickstart

How Go projects are usually set up, built and tested. Always prefer the project's own `CONTRIBUTING.md` when it says something different.

Open Go issues: [Go issue list](../issues/by-language/go.md)

## Setup

- Install Go from [go.dev/dl](https://go.dev/dl) or your package manager. If `go.mod` asks for a newer version, Go downloads it automatically.

## Common commands

| Task | Usual command |
| --- | --- |
| Build | `go build ./...` |
| Run tests | `go test ./...` |
| Run tests for one package | `go test ./internal/parser/ -run TestName -v` |
| Format | `gofmt -l .` (or `goimports`) |
| Vet and lint | `go vet ./...`, `golangci-lint run` when `.golangci.yml` exists |
| Generate code | `go generate ./...` or `make generate` |

## Tips

- Check the `Makefile`: many Go projects wrap tests, linting and code generation there.
- If the project commits generated code, regenerate it and include only the relevant changes.
- Table-driven tests are the norm; add a case to the existing table instead of writing a new test function.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] Formatter and linter pass with the project's configuration.
- [ ] Your diff contains no unrelated formatting or lockfile changes.

Back to [all languages](README.md) · [Guide](../guide/README.md)
