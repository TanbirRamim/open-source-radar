# 2. Konfiguracja narzędzi

Potrzebujesz Gita, konta GitHub, sposobu uwierzytelniania, edytora oraz zestawu narzędzi dla języka używanego w wybranym projekcie. Jednorazowa konfiguracja zajmuje około godziny.

## Git

Zainstaluj Git:

- **macOS:** `xcode-select --install` (instaluje Git wraz z Command Line Tools) lub `brew install git` za pomocą [Homebrew](https://brew.sh).
- **Windows:** [Git for Windows](https://git-scm.com/download/win). Zawiera Git Bash, terminal, w którym uruchomisz polecenia z tego przewodnika.
- **Linux:** menedżer pakietów, na przykład `sudo apt install git` lub `sudo dnf install git`.

Podaj Gitowi swoje dane. Użyj tego samego adresu e-mail co na koncie GitHub (lub prywatnego adresu noreply GitHuba, patrz niżej), aby Twoje commity były powiązane z Twoim profilem:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Zachowaj prywatność adresu e-mail (opcjonalnie)

GitHub udostępnia każdemu kontu adres noreply w postaci `12345678+username@users.noreply.github.com`. Znajdziesz go w sekcji **Settings → Emails**. Włącz opcję **Keep my email addresses private** i użyj tego adresu jako wartości `user.email`. Commity nadal będą liczyć się na Twoim profilu.

> **Częsty błąd:** tworzenie commitów z adresem e-mail, który nie jest dodany do konta GitHub. Commity pojawiają się wtedy bez Twojego awatara i nie liczą się na Twoim profilu. Sprawdź adres poleceniem `git config user.email` i porównaj go z adresem w sekcji **Settings → Emails**.

## Konto GitHub i uwierzytelnianie

1. Załóż konto na [github.com](https://github.com). Wybierz profesjonalną nazwę użytkownika; będzie widoczna przy każdym Twoim wkładzie.
2. Włącz uwierzytelnianie dwuskładnikowe w sekcji **Settings → Password and authentication**. Wiele organizacji tego wymaga.
3. Skonfiguruj sposób uwierzytelniania Gita. Najłatwiej zrobić to za pomocą GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: see cli.github.com
gh auth login          # choose GitHub.com, HTTPS, and log in with a browser
gh auth setup-git      # lets git push over HTTPS using that login
```

Możesz też [dodać klucz SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) i klonować repozytoria przy użyciu adresów `git@github.com:`.

## Edytor

Korzystaj z tego, w czym pracuje Ci się wygodnie. [VS Code](https://code.visualstudio.com) to popularny wybór: dobrze integruje się z Gitem, a oficjalne rozszerzenia językowe zapewniają formatowanie i sprawdzanie błędów. JetBrains IDE, Neovim, Zed i Emacs również się sprawdzą.

Dwa ustawienia pomogą Ci uniknąć uwag podczas przeglądu kodu:

- **Formatowanie przy zapisie** przy użyciu formatera projektu (Prettier, Black, rustfmt, gofmt itd.).
- **Uwzględnianie `.editorconfig`**. Wiele projektów zawiera ten plik, aby ustawić wcięcia i zakończenia wierszy.

## Polecenia Gita, których naprawdę będziesz używać

| Polecenie | Co robi |
| --- | --- |
| `git clone URL` | Pobiera repozytorium |
| `git status` | Pokazuje, co się zmieniło |
| `git switch -c fix-typo` | Tworzy nową gałąź i przełącza na nią |
| `git add path/to/file` | Dodaje zmianę do następnego commita |
| `git commit -m "message"` | Zapisuje przygotowane zmiany w commicie |
| `git push -u origin fix-typo` | Wysyła gałąź do zdalnego repozytorium |
| `git fetch upstream` | Pobiera najnowsze zmiany z oryginalnego projektu |
| `git rebase upstream/main` | Nakłada Twoje commity na te zmiany |
| `git log --oneline -10` | Pokazuje ostatnie commity |
| `git diff` | Pokazuje nieprzygotowane zmiany (`git diff --staged` pokazuje przygotowane) |

Jeśli nigdy nie korzystałeś z Gita, poświęć najpierw 30 minut na [Learn Git Branching](https://learngitbranching.js.org). To interaktywna nauka, która obejmuje dokładnie to, czego potrzebujesz.

## Zestawy narzędzi dla języków

Zainstaluj zestaw narzędzi dla wybranego projektu w wymaganej przez niego wersji (szukaj plików takich jak `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod`, `.tool-versions`). [Szybkie instrukcje dla poszczególnych języków](../../languages/README.md) zawierają najczęściej używane polecenia.

Menedżery wersji ułatwiają tę konfigurację:

- **Kilka języków:** [mise](https://mise.jdx.dev) lub [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) lub nvm, a także `corepack enable` dla pnpm i Yarn
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** oficjalny instalator lub menedżer pakietów; Go sam pobiera nowsze wersje narzędzi, gdy wymaga tego `go.mod`

## Lista kontrolna

- [ ] `git --version` działa, a `git config user.email` odpowiada adresowi e-mail na moim koncie GitHub.
- [ ] Uwierzytelnianie dwuskładnikowe jest włączone.
- [ ] `gh auth status` (lub `ssh -T git@github.com`) pokazuje, że mogę się uwierzytelnić.
- [ ] Mój edytor formatuje kod przy zapisie.

Dalej: [Wybór projektu](../03-choose-a-project.md)
