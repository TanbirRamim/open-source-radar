# 8. Revisioni, feedback e rifiuti

Aprire la pull request è la metà del processo, non la fine. Il modo in cui gestisci la revisione decide se verrà integrata (merged).

## Quando la CI fallisce

1. Apri il controllo fallito e leggi il log dal primo errore, non dall'ultima riga.
2. Decidi se la tua modifica lo ha causato:
   - **Errore di formattazione o lint:** esegui il formatter o il linter localmente, fai il commit del risultato.
   - **Un test che hai toccato fallisce:** sistemalo localmente, fai di nuovo push.
   - **Un test non correlato fallisce** e fallisce anche sul branch predefinito, oppure un job sembra instabile (timeout, errori di rete): segnalalo in un commento con un link allo stesso errore altrove. Non cercare di correggere errori non correlati nella tua PR a meno che non ti venga chiesto.
3. Invia le correzioni tramite push come nuovi commit, a meno che il progetto non ti chieda di fare squash.

Molti progetti richiedono che un maintainer approvi l'esecuzione della CI per chi contribuisce per la prima volta. Se i controlli dicono "awaiting approval", è normale: aspetta.

## Quando ricevi richieste di modifica

- **Leggi ogni commento prima di rispondere.** Alcuni dipendono l'uno dall'altro.
- **Apporta le modifiche richieste o spiega perché non lo fai.** Essere in disaccordo va bene se fornisci una motivazione; ignorare un commento no.
- **Rispondi a ogni commento** indicando cosa hai fatto ("Fatto in abc123" o "Modificato per usare l'helper esistente"). Lascia che sia il revisore a risolvere le conversazioni, a meno che il progetto non ti chieda di farlo.
- **Fai push, poi richiedi nuovamente la revisione** usando il pulsante sulla pull request, oppure lascia un breve commento dicendo che è di nuovo pronta.
- **Mantieni l'ambito (scope).** Se un revisore chiede qualcosa di molto più grande, suggerisci una issue di follow-up invece di ingrandire la pull request.

I commenti di revisione riguardano il codice, non te. Anche i contributori esperti ricevono molti giri di feedback in un nuovo progetto.

## Revisori automatici

Alcuni progetti usano bot che pubblicano revisioni automatiche. Tratta i loro commenti come suggerimenti: correggi i problemi reali che trovano e fai notare educatamente quando un suggerimento non è applicabile. Sono i maintainer umani a prendere la decisione finale.

## Quando non succede nulla

Il silenzio è comune e di solito significa "occupato", non "no".

- Dopo una o due settimane, fai un sollecito educato (capitolo 7).
- Controlla se il progetto ha una coda di revisione o etichette come `waiting-on-review`.
- Mantieni il tuo branch integrabile (mergeable): risolvi i conflitti quando compaiono.
- Dopo un mese o più, puoi chiedere se la modifica è ancora desiderata. In caso contrario, chiuderla tu stesso va bene ed è apprezzato.

## Quando la tua pull request viene chiusa

Succede a tutti. Motivi comuni:

| Motivo | Cosa fare |
| --- | --- |
| Qualcun altro l'ha risolto per primo | Chiudi la tua, ringraziali, la prossima volta scegli un'altra issue prima dopo che è stata aperta |
| I maintainer vogliono un approccio diverso | Chiedi se accetterebbero una versione rivista, oppure lascia che facciano a modo loro |
| Fuori dall'ambito del progetto | Accettalo; chiedi se ha senso creare un plugin o un pacchetto separato |
| Bassa qualità o poco chiara | Leggi attentamente il feedback; la tua prossima PR in quel progetto dovrà essere chiaramente migliore |
| Chiusa dall'automazione | Leggi il messaggio del bot e il file del workflow; correggi ciò che chiede o contatta i maintainer |
| Nessuna risposta, chiusa come inattiva (stale) | Chiedi educatamente se vorrebbero riaprirla; in caso contrario, vai avanti |

Una pull request chiusa con una risposta educata e costruttiva lascia comunque una buona impressione.

## Dopo il merge

- Elimina il tuo branch (GitHub offre un pulsante).
- Aggiorna il branch predefinito del tuo fork: `git fetch upstream && git switch main && git rebase upstream/main && git push`.
- Prendi nota di ciò che hai imparato sul processo del progetto. La tua seconda pull request lì sarà molto più veloce.

## Checklist

- [ ] Ho letto i log della CI dal primo errore e ho separato i miei errori da quelli preesistenti.
- [ ] Ho risposto a ogni commento di revisione e ho richiesto nuovamente la revisione.
- [ ] Ho mantenuto ridotto l'ambito della pull request.
- [ ] Ho fatto follow-up educatamente, al massimo una volta a settimana.

Successivo: [Continuare il percorso](../09-keep-going.md) (in inglese)
