# PowerShell quickstart

How PowerShell projects are usually set up and checked. Always follow the project's own CONTRIBUTING.md and CI configuration when they differ.

Open PowerShell issues: [PowerShell issue list](../issues/by-language/powershell.md)

## Setup

- Install PowerShell 7 (the pwsh command) using the [official installation guide](https://learn.microsoft.com/powershell/scripting/install/installing-powershell).
- Check the project's .psd1, .psm1, .ps1, and workflow files for the supported PowerShell version and required modules.
- Install project dependencies from the repository's documented setup instructions.

## Common commands

| Task | Usual command |
| --- | --- |
| Check the installed version | `pwsh --version` |
| Start an interactive shell | `pwsh` |
| Run a script | `pwsh -File path/to/script.ps1` |
| Run a command | `pwsh -Command "Get-Process"` |
| Install Pester | `Install-Module Pester -Scope CurrentUser` |
| Run all Pester tests | `Invoke-Pester` |
| Run tests in a directory | `Invoke-Pester -Path ./tests` |
| Install PSScriptAnalyzer | `Install-Module PSScriptAnalyzer -Scope CurrentUser` |
| Analyze a script | `Invoke-ScriptAnalyzer -Path ./path/to/script.ps1` |
| Analyze the repository | `Invoke-ScriptAnalyzer -Path . -Recurse` |
| Format a script (prints the result, doesn't save it) | `Invoke-Formatter -ScriptDefinition (Get-Content ./path/to/script.ps1 -Raw)` |

## Tips

- Prefer PowerShell 7 (pwsh) for cross-platform work unless the project explicitly targets Windows PowerShell 5.1.
- Pester is the standard PowerShell testing framework. Check the project's configuration for its required Pester version and test discovery rules.
- PSScriptAnalyzer checks scripts for common problems and style issues. Repositories may provide a PSScriptAnalyzerSettings.psd1 file with project-specific rules.
- Run commands from the repository root so relative paths and module imports resolve as expected.
- Avoid changing execution policy globally just to run a project script. Follow the project's setup instructions instead.

## Before you push

- [ ] Tests for the area you changed pass locally.
- [ ] PSScriptAnalyzer passes with the project's settings.
- [ ] Formatting follows the project's conventions.
- [ ] Your diff contains no unrelated generated files or changes.

Useful references: [PowerShell documentation](https://learn.microsoft.com/powershell/), [Pester](https://pester.dev/), and [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer).

Back to [all languages](README.md) · [Guide](../guide/README.md)
