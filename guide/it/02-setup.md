# 2. Configura i tuoi strumenti

Ti servono Git, un account GitHub, un metodo di autenticazione, un editor e gli strumenti necessari per il linguaggio del progetto che hai scelto. Configurare tutto una volta sola richiede circa un'ora.

## Git

Installa Git:

- **macOS:** `xcode-select --install` (installa Git insieme ai Command Line Tools) oppure `brew install git` con [Homebrew](https://brew.sh).
- **Windows:** [Git for Windows](https://git-scm.com/download/win). Include Git Bash, un terminale che permette di eseguire i comandi presenti in questa guida.
- **Linux:** utilizza il tuo gestore di pacchetti, ad esempio `sudo apt install git` oppure `sudo dnf install git`.

Comunica a Git chi sei. Utilizza lo stesso indirizzo email del tuo account GitHub (oppure l'indirizzo noreply privato di GitHub, illustrato di seguito), in modo che i tuoi commit siano associati al tuo profilo:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Mantieni privato il tuo indirizzo email (facoltativo)

GitHub assegna a ogni account un indirizzo noreply, ad esempio `12345678+username@users.noreply.github.com`. Puoi trovare il tuo in **Settings → Emails**. Attiva **Keep my email addresses private** e utilizza quell'indirizzo come valore di `user.email`. I commit continueranno a essere conteggiati nel tuo profilo.

> **Errore comune:** effettuare commit utilizzando un indirizzo email che non è associato al tuo account GitHub. I commit appariranno senza il tuo avatar e non verranno conteggiati nel tuo profilo. Controlla con `git config user.email` e confronta il risultato con **Settings → Emails**.

## Un account GitHub e l'autenticazione

1. Crea un account su [github.com](https://github.com). Scegli un nome utente professionale: apparirà in ogni tuo contributo.
2. Attiva l'autenticazione a due fattori da **Settings → Password and authentication**. Molte organizzazioni la richiedono.
3. Configura un metodo di autenticazione per Git. L'opzione più semplice è GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: see cli.github.com
gh auth login          # choose GitHub.com, HTTPS, and log in with a browser
gh auth setup-git      # lets git push over HTTPS using that login
```

In alternativa, [aggiungi una chiave SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) e clona i repository utilizzando URL nel formato `git@github.com:`.

## Un editor

Scegli l'editor con cui ti trovi più a tuo agio. [VS Code](https://code.visualstudio.com) è una scelta comune: offre una buona integrazione con Git e le estensioni ufficiali dei linguaggi forniscono strumenti di formattazione e controllo degli errori. Vanno bene anche gli IDE JetBrains, Neovim, Zed ed Emacs.

Due impostazioni possono evitarti commenti durante la code review:

- **Format on save:** utilizza il formatter del progetto (Prettier, Black, rustfmt, gofmt e così via).
- **Rispetta `.editorconfig`:** molti progetti includono questo file per definire l'indentazione e le terminazioni di riga.

## I comandi Git che utilizzerai davvero

| Comando | A cosa serve |
| --- | --- |
| `git clone URL` | Scarica un repository |
| `git status` | Mostra le modifiche |
| `git switch -c fix-typo` | Crea un nuovo branch e passa a quel branch |
| `git add path/to/file` | Aggiunge una modifica all'area di staging per il prossimo commit |
| `git commit -m "message"` | Registra le modifiche messe in staging |
| `git push -u origin fix-typo` | Pubblica il tuo branch |
| `git fetch upstream` | Scarica gli ultimi aggiornamenti dal progetto originale |
| `git rebase upstream/main` | Riapplica i tuoi commit sopra quegli aggiornamenti |
| `git log --oneline -10` | Mostra gli ultimi commit |
| `git diff` | Mostra le modifiche non ancora messe in staging (`git diff --staged` mostra quelle già in staging) |

Se non hai mai utilizzato Git, dedica prima 30 minuti a [Learn Git Branching](https://learngitbranching.js.org). È interattivo e tratta esattamente gli argomenti di cui hai bisogno.

## Gli strumenti per il linguaggio

Installa gli strumenti necessari per il progetto che hai scelto, utilizzando la versione richiesta dal progetto (cerca file come `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod` e `.tool-versions`). Le [guide rapide ai linguaggi](../../languages/README.md) elencano i comandi più comuni per ciascun linguaggio.

I version manager semplificano questa operazione:

- **Diversi linguaggi:** [mise](https://mise.jdx.dev) oppure [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) oppure nvm, insieme a `corepack enable` per pnpm e Yarn
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** il programma di installazione ufficiale oppure il gestore di pacchetti; Go scarica automaticamente le versioni più recenti degli strumenti quando `go.mod` ne richiede una.

## Checklist

- [ ] `git --version` funziona e `git config user.email` corrisponde a un indirizzo associato al mio account GitHub.
- [ ] L'autenticazione a due fattori è attiva.
- [ ] `gh auth status` (oppure `ssh -T git@github.com`) conferma che posso autenticarmi.
- [ ] Il mio editor formatta il codice al salvataggio.

Prossimo capitolo: [Scegliere un progetto](03-choose-a-project.md)
