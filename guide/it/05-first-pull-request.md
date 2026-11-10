# 5. La tua prima pull request, passo dopo passo

Questo è il flusso di lavoro completo, dal fork all'apertura di una pull request. Sostituisci `OWNER/REPO` con il progetto e `your-username` con il tuo nome utente GitHub.

## 1. Crea un fork e clona il repository

Un **fork** è una tua copia del repository su GitHub. Effettui il push delle modifiche sul tuo fork e poi chiedi al progetto originale (chiamato **upstream**) di integrarle.

```bash
gh repo fork OWNER/REPO --clone
cd REPO
git remote -v
# origin    https://github.com/your-username/REPO.git  (il tuo fork)
# upstream  https://github.com/OWNER/REPO.git          (l'originale)
```

Senza GitHub CLI: fai clic su **Fork** nella pagina del repository, quindi:

```bash
git clone https://github.com/your-username/REPO.git
cd REPO
git remote add upstream https://github.com/OWNER/REPO.git
```

> Repository di grandi dimensioni? `git clone --filter=blob:none URL` scarica i contenuti dei file solo quando necessario, rendendo il processo molto più veloce.

## 2. Crea un branch

Non lavorare mai sul branch predefinito del tuo fork. Inizia ogni modifica partendo dal codice più recente del repository upstream:

```bash
git fetch upstream
git switch -c fix-empty-username upstream/main   # usa il nome del branch predefinito del progetto
```

Assegna ai branch nomi che descrivano la modifica, come `fix-empty-username` o `docs-install-windows`.

## 3. Compila il progetto ed esegui i test prima di modificare qualsiasi cosa

Segui le indicazioni contenute nel file `CONTRIBUTING.md` o `DEVELOPMENT.md` del progetto. Le [guide rapide per i linguaggi](../../languages/README.md) mostrano i comandi più comuni. Esegui prima i test sul codice originale, senza modifiche:

- Se vengono superati, hai una base di partenza funzionante.
- Se alcuni test falliscono già, annota quali sono. Quei problemi non dipendono da te e dovresti segnalarli nella tua PR, se pertinenti.

## 4. Riproduci il problema

Prima di correggere un problema, verifica che si presenti realmente sul tuo computer seguendo i passaggi descritti nella issue. Annota cosa succede e cosa dovrebbe succedere invece. Se non riesci a riprodurlo, dichiaralo nella issue (indicando la tua versione e il tuo ambiente) invece di ipotizzare una soluzione.

## 5. Scrivi un test che fallisca

Individua il file di test relativo al codice che stai modificando e aggiungi un test che dimostri il problema. Eseguilo e verifica che fallisca. In questo modo puoi dimostrare a te stesso e a chi revisiona il codice che il test individua effettivamente il problema.

Non tutte le modifiche richiedono un test (ad esempio, le correzioni alla documentazione), ma quasi tutte le correzioni di bug sì. Molti progetti non accettano una correzione senza un test.

## 6. Apporta la modifica più piccola possibile per risolvere il problema

- Modifica solo ciò che è necessario per risolvere la issue. Evita refactoring non richiesti, rinominazioni o riformattazioni di codice non correlato: rendono la tua pull request più difficile da revisionare.
- Segui lo stile del codice circostante, anche se lo scriveresti diversamente.
- Esegui nuovamente il test del passaggio 5. Questa volta dovrebbe essere superato.

## 7. Esegui tutti i controlli in locale

Esegui gli stessi controlli previsti dalla CI del progetto, almeno per l'area che hai modificato:

- la suite di test (o la parte pertinente)
- il formatter (ad esempio `prettier`, `black`/`ruff format`, `cargo fmt`, `gofmt`)
- il linter (ad esempio `eslint`, `ruff`, `clippy`, `go vet`)
- il controllo dei tipi, se il progetto lo utilizza (`tsc`, `mypy`)

Alcuni progetti richiedono anche una voce nel changelog o un file "changeset". Troverai queste indicazioni nella guida alla contribuzione.

## 8. Crea un commit

```bash
git add path/to/changed/files
git commit
```

Scrivi un messaggio chiaro. Segui le convenzioni del progetto (controlla `git log --oneline -20`). Un formato comune è:

```text
parser: handle empty username in login prompt

An empty username made the prompt loop forever because validation
rejected it without telling the user. Show the validation error and
ask again instead.

Fixes #1234
```

- Prima riga: un breve riepilogo, spesso preceduto dall'area interessata o da un tipo secondo le convenzioni di [Conventional Commits](https://www.conventionalcommits.org), come `fix:` o `docs:`.
- Corpo: descrivi cosa non funzionava e perché questa modifica risolve il problema.
- `Fixes #1234` chiude automaticamente la issue quando la PR viene unita.
- Se il progetto richiede la firma DCO, utilizza `git commit -s` (vedi il [capitolo 6](06-rules-before-you-start.md)).

## 9. Esegui il push e apri la pull request

```bash
git push -u origin fix-empty-username
gh pr create --repo OWNER/REPO --fill   # oppure apri nel browser il link stampato da git
```

Compila il modello della pull request del progetto, se disponibile. Il [capitolo 7](../07-communication.md) (in inglese) spiega come scrivere una buona descrizione. In breve: indica cosa non funzionava, cosa hai modificato, come hai eseguito i test e quale issue viene risolta.

## 10. Mantieni aggiornato il tuo branch

Se il branch upstream avanza prima che la tua PR venga unita e si verificano conflitti, aggiorna il tuo branch:

```bash
git fetch upstream
git rebase upstream/main
# risolvi eventuali conflitti, poi: git add <file> && git rebase --continue
git push --force-with-lease
```

`--force-with-lease` è il modo sicuro per aggiornare un branch la cui cronologia è stata riscritta: impedisce di sovrascrivere commit che non possiedi in locale. Alcuni progetti preferiscono che tu unisca `upstream/main` nel tuo branch invece di utilizzare il rebase; segui le indicazioni del progetto.

## Piccole correzioni alla documentazione senza Git

Per correggere un refuso o un link non funzionante, puoi saltare completamente la clonazione e apportare la modifica direttamente dal browser:

1. Apri il file su GitHub nel repository originale e fai clic sull'icona della matita. Se non puoi effettuare il push direttamente lì, GitHub creerà automaticamente un fork del repository.
2. Apporta la modifica e controlla la scheda Preview.
3. Fai clic su "Commit changes...", seleziona "Create a new branch" e assegna un nome breve, come `fix-readme-typo`.
4. Fai clic su "Propose changes", poi su "Create pull request" e compila il modello.

Questo metodo è adatto solo a piccole modifiche testuali. Qualsiasi modifica che richieda una compilazione o dei test dovrebbe seguire i passaggi precedenti, così potrai eseguire i controlli prima di effettuare il push.

## Checklist

- [ ] Ho creato il branch partendo dall'ultima versione del branch predefinito di upstream.
- [ ] I test sono stati superati prima delle mie modifiche (oppure ho annotato i problemi già esistenti).
- [ ] Ho riprodotto il bug e scritto un test che falliva prima della correzione.
- [ ] Le modifiche riguardano esclusivamente ciò che è necessario per risolvere questa issue.
- [ ] I test, il formatter e il linter sono stati superati in locale.
- [ ] Il messaggio del commit segue le convenzioni del progetto e fa riferimento alla issue.
- [ ] Ho compilato il modello della PR.

Successivo: [Regole da verificare prima di iniziare](06-rules-before-you-start.md)
