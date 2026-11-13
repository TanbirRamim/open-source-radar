# 7. Comunicare con i manutentori

I manutentori sono generalmente volontari o sviluppatori impegnati che revisionano i contributi oltre a svolgere il proprio lavoro. Una comunicazione chiara, breve e specifica ti aiuta a ottenere risposte più rapide e cordiali.

## Prendere in carico una issue

Alcuni progetti vogliono che tu lasci un commento prima di iniziare; altri dicono semplicemente di aprire una PR. Controlla la guida alla contribuzione del progetto. Quando lasci un commento, assicurati che sia utile:

> Riesco a riprodurre il problema sulla versione 4.2.1: `tool --flag ""` entra in un ciclo infinito invece di mostrare un errore. Il controllo in `src/prompt.ts` rifiuta l'input vuoto senza indicarne il motivo. Intendo mostrare il messaggio di validazione e chiedere nuovamente l'input, aggiungendo un test in `prompt.test.ts`. Posso procedere?

Questo è molto più utile di un semplice "Posso lavorare su questa issue?", perché dimostra che hai compreso il problema e permette al manutentore di correggere il tuo approccio prima che tu dedichi del tempo al lavoro.

Non prendere in carico più issue contemporaneamente e non prendere in carico una issue se non hai intenzione di iniziare a lavorarci durante la settimana.

## Chiedere aiuto

Quando incontri una difficoltà, chiedi aiuto nella issue (o nella chat del progetto, se disponibile) e includi:

- cosa stai cercando di fare
- cosa hai già provato
- cosa è successo, riportando il messaggio di errore o l'output esatto
- il tuo ambiente di lavoro, quando rilevante (sistema operativo, versione del linguaggio, versione del progetto)

Inserisci un link alla riga di codice a cui ti riferisci. Continua a indagare mentre aspetti una risposta: se trovi la soluzione, condividila nella discussione.

## Scrivere la descrizione di una pull request

I revisori leggono molte pull request. Rendi la tua facile da comprendere in 30 secondi.

**Esempio positivo:**

> Fixes #1234.
>
> `login` richiedeva nuovamente l'input all'infinito quando il nome utente era vuoto, perché `validateUsername` restituiva un errore che il ciclo del prompt ignorava. Ora il ciclo mostra il messaggio di validazione prima di chiedere nuovamente l'input.
>
> Ho aggiunto un test in `prompt.test.ts` che fallisce in assenza della modifica. `npm test` e `npm run lint` vengono eseguiti correttamente in locale.

**Perché funziona:** collega la issue, spiega cosa non funzionava e perché, descrive cosa è stato modificato e indica come è stata verificata la soluzione. Senza informazioni superflue.

**Da evitare:**

- Riepiloghi generati troppo lunghi, elenchi di ogni file modificato o titoli per modifiche di poche righe.
- Linguaggio promozionale ("Questa PR migliora significativamente...").
- Affermazioni che non hai verificato ("risolve tutti i problemi correlati").
- Lasciare il testo segnaposto del modello della PR.

Se c'è qualcosa che i revisori dovrebbero sapere, dichiaralo direttamente: "Non ero sicuro che i nomi utente vuoti dovessero essere consentiti per i registri personalizzati, quindi ho mantenuto il comportamento esistente in quel caso."

## Tono

- Sii educato e presumi sempre buone intenzioni, anche quando qualcuno ti risponde in modo sbrigativo.
- Ringrazia i revisori per il loro tempo, una sola volta. Non è necessario ringraziarli per ogni commento.
- Non menzionare ripetutamente i manutentori con `@` e non contattare persone che non sono coinvolte.
- Mantieni la discussione nella issue o nella pull request, non nei messaggi privati, a meno che non ti venga richiesto.
- Scrivi con parole tue. I manutentori vogliono capire che conosci e comprendi la modifica che stai proponendo.

## Sollecitare una risposta

Se non ricevi risposta dopo circa una settimana, puoi inviare un cortese messaggio di follow-up:

> Un piccolo promemoria: la PR è pronta per la revisione quando qualcuno avrà tempo. Sono disponibile ad apportare eventuali modifiche.

Se il progetto dispone di un canale chat per i collaboratori, puoi anche chiedere lì una volta. Dopodiché, lascia trascorrere del tempo: alcuni progetti sono semplicemente lenti.

## Checklist

- [ ] Il mio commento per prendere in carico la issue (se necessario) dimostra che ho compreso il problema.
- [ ] La descrizione della mia PR spiega cosa non funzionava, cosa ho modificato, come ho eseguito i test e include il collegamento alla issue.
- [ ] Ho rimosso il testo segnaposto del modello.
- [ ] I miei messaggi di follow-up sono educati e sufficientemente distanziati nel tempo.

Successivo: [Revisioni, feedback e rifiuti](../08-reviews.md) (in inglese)
