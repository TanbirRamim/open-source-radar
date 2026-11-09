# 4. Trova una issue che puoi completare

Una buona issue da affrontare per la prima volta è piccola, descritta chiaramente, riproducibile e non è già stata presa in carico da un altro contributore. È proprio quest'ultimo aspetto che fa perdere più tempo a chi inizia.

## Dove cercare

- **L'[indice delle issue](../../issues/README.md)** e il [sito web](https://tanbirramim.github.io/open-source-radar/) di questo repository: apri le issue contrassegnate come adatte ai nuovi contributori, già filtrate per escludere quelle assegnate a qualcuno o collegate a una pull request aperta.
- **Il sistema di gestione delle issue del progetto**, filtrando per le etichette dedicate ai nuovi contributori.
- **La ricerca di GitHub**, ad esempio:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` nasconde le issue assegnate e `-linked:pr` nasconde quelle che hanno già una pull request collegata. Aggiungi `updated:>2026-06-01` (utilizzando una data recente) per escludere quelle non aggiornate da molto tempo.

## Etichette che incontrerai

| Etichetta | Di solito significa |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | I manutentori ritengono che un nuovo contributore possa occuparsene, spesso con una guida |
| `help wanted`, `PR welcome`, `up-for-grabs` | I manutentori vogliono che qualcun altro se ne occupi; non si tratta necessariamente di attività semplici |
| `bug`, `confirmed`, `has: repro` | Un difetto reale; `confirmed` significa che un manutentore è riuscito a riprodurlo |
| `needs-triage`, `needs-info`, `question` | Non è ancora pronto: il problema non è stato compreso a sufficienza |
| `design`, `rfc`, `discussion`, `blocked` | Non è ancora pronto per una pull request; è in attesa di una decisione |

Ogni progetto definisce le proprie etichette. Controlla le descrizioni nella pagina **Issues → Labels** del progetto.

## Qualcun altro ci sta già lavorando?

Prima di scrivere anche una sola riga di codice, controlla tutti questi aspetti:

1. **Persone assegnate.** Se qualcuno è già assegnato alla issue, significa che è già stata presa in carico.
2. **Pull request collegate.** Controlla la barra laterale destra ("Development") e la cronologia delle attività per trovare eventi come "linked a pull request" o "mentioned this issue" provenienti dalle PR. Una PR aperta significa che la issue è già in lavorazione; una PR chiusa senza essere stata unita potrebbe indicare che l'approccio è stato rifiutato, quindi leggi le motivazioni.
3. **Commenti.** Cerca messaggi come "Mi piacerebbe occuparmene" oppure "Ci sto lavorando". Se la dichiarazione di interesse è recente (qualche settimana) e la persona è ancora attiva, scegli un'altra issue.
4. **Ricerca delle pull request aperte.** Cerca il numero della issue o alcune parole chiave del titolo. Non tutte le PR sono correttamente collegate alla relativa issue.

Se il commento in cui qualcuno si propone di lavorarci è vecchio e la persona non dà più notizie, di solito puoi chiedere gentilmente: "Ciao @nome, stai ancora lavorando a questa issue? In caso contrario, mi piacerebbe occuparmene." Poi attendi qualche giorno.

## Riesci a completarla?

Fai una valutazione onesta delle tue capacità. Una buona prima issue da affrontare:

- **Ha un comportamento atteso chiaro.** Sai spiegare in una frase cosa dovrebbe succedere.
- **È riproducibile.** La issue contiene dei passaggi, uno snippet di codice o un comando che genera un errore. In caso contrario, riprodurre il problema sarà il tuo primo compito, e condividere i passaggi per riprodurlo sarà già un contributo.
- **Ha un ambito limitato.** Puoi individuare quale file o funzione potrebbe essere coinvolto. Cerca nel codice il messaggio di errore o il nome della funzione menzionata nella issue.
- **Non richiede una decisione progettuale.** Se i manutentori stanno ancora discutendo su *come* dovrebbe funzionare, aspetta.
- **Funziona sul tuo computer.** Evita bug che si verificano solo su Windows se usi macOS, bug legati alla GPU se non ne hai una e situazioni simili.

## Un metodo rapido per valutare le dimensioni di una issue

Dedica dai 20 ai 30 minuti a questa valutazione prima di decidere di occupartene:

1. Clona il progetto ed esegui una volta la suite di test (capitolo 5).
2. Riproduci il bug oppure individua nel codice il punto in cui implementare la funzionalità.
3. Trova il test esistente relativo a quell'area del progetto.

Se sei riuscito a completare tutte e tre le attività, probabilmente la issue ha dimensioni adeguate. Se dopo 30 minuti sei ancora in difficoltà, prova a scegliere un'altra issue oppure poni una domanda specifica nella issue (capitolo 7).

## Lista di controllo

- [ ] Nessun assegnatario, nessuna PR aperta collegata e nessuna dichiarazione recente di interesse nei commenti.
- [ ] So descrivere in una frase il comportamento atteso.
- [ ] Ho riprodotto il problema oppure so esattamente dove apportare la modifica.
- [ ] I manutentori non stanno ancora discutendo sull'approccio da seguire.

Successivo: [La tua prima pull request, passo dopo passo](05-first-pull-request.md)
