# 3. Scegliere un progetto

Il progetto è più importante del singolo issue. Un progetto attivo e accogliente può esaminare la tua pull request in pochi giorni. Un progetto inattivo o con troppe richieste in sospeso potrebbe non prenderla mai in considerazione, per quanto valido sia il tuo contributo.

## Parti da ciò che utilizzi

Il progetto migliore da cui iniziare è uno che già utilizzi: una libreria presente nel tuo codice, uno strumento che usi ogni giorno o un'app che ti piace. Sai come dovrebbe funzionare, puoi testare concretamente le tue modifiche e hai interesse per il risultato.

Se non ti viene in mente nessun progetto, consulta l'[indice degli issue](../../issues/README.md) in base al linguaggio che conosci meglio e osserva quali progetti compaiono più spesso.

## Segnali di un progetto sano e accogliente

Controlla questi aspetti nella pagina del repository. Cinque minuti di verifica possono risparmiarti settimane di attesa.

| Verifica | Dove guardare | Segnale positivo |
| --- | --- | --- |
| Attività recente | Scheda Commits, data dell'ultimo commit | Sono stati effettuati commit nelle ultime settimane |
| Pull request di contributori esterni unite | **Pull requests → Closed**, applica il filtro `is:merged` e controlla gli autori | Nell'ultimo mese sono state unite pull request inviate da persone che non fanno parte dei maintainer |
| Velocità delle revisioni | Apri alcune pull request di contributori esterni unite di recente | Prima risposta entro pochi giorni, non mesi |
| Guida alla contribuzione | `CONTRIBUTING.md` nella root, in `.github/` o in `docs/` | Esiste e spiega come configurare l'ambiente e come eseguire i test |
| Etichette per i nuovi contributori | Issues, filtra per `good first issue` o `help wanted` | Le etichette vengono utilizzate e gli issue contrassegnati ricevono attenzione |
| Tono delle conversazioni | Leggi alcune discussioni negli issue | I maintainer sono pazienti e precisi, anche quando rifiutano una proposta |
| Codice di condotta | `CODE_OF_CONDUCT.md` | Esiste |
| CI | Controlli sulle pull request recenti | I test vengono eseguiti automaticamente sulle pull request |

Una ricerca rapida per trovare le pull request unite provenienti da contributori esterni, valida per qualsiasi repository (sostituisci `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Controlla gli autori: se tutte le pull request unite provengono sempre dalle stesse due persone, è possibile che il progetto non dia priorità ai contributi esterni.

## Segnali di allarme

- **Centinaia di pull request aperte senza revisione.** La tua si aggiungerà alla coda.
- **Una guida alla contribuzione che dichiara che il progetto non accetta pull request**, oppure le accetta solo per issue contrassegnati con una specifica etichetta. Alcuni progetti popolari funzionano così. Rispetta questa regola.
- **Ogni issue recente ha già diverse pull request in competizione.** I progetti popolari spesso ricevono pull request spontanee poche ore dopo la segnalazione di un bug. Puoi comunque contribuire, ma scegli attività meno contese (documentazione, test, bug già verificati da tempo) oppure un progetto più piccolo.
- **I maintainer chiedono agli utenti di non aprire pull request con contributi di scarso valore.** Leggi queste discussioni: ti indicano chiaramente cosa evitare.
- **Nessun commit da mesi.** Il progetto potrebbe essere terminato oppure abbandonato.

## Progetto grande o progetto piccolo?

| | Progetto grande e famoso | Progetto più piccolo e attivo |
| --- | --- | --- |
| Concorrenza per gli issue semplici | Molto alta | Bassa |
| Velocità delle revisioni | Molto variabile; spesso lenta per i contributori esterni | Spesso rapida e personalizzata |
| Processo | Formale: template, CLA, CI rigorosa | Più snello |
| Mentorship | A volte sono disponibili programmi strutturati | Contatto diretto con il maintainer |
| Visibilità sul tuo profilo | Forte riconoscibilità del nome | Maggiore se diventi un contributore abituale |

Una buona strategia: realizza i tuoi primi uno o due contributi in un progetto più piccolo e attivo, dove puoi ricevere feedback rapidamente. In seguito, applica ciò che hai imparato a progetti più grandi.

## Checklist

- [ ] Il progetto ha registrato commit nell'ultimo mese.
- [ ] Di recente ha unito pull request di contributori esterni.
- [ ] Ha una guida alla contribuzione e l'ho letta.
- [ ] Riesco a compilare ed eseguire il progetto sul mio computer (il capitolo 5 tratta questo argomento).

Prossimo capitolo: [Trovare un issue che puoi completare](../04-find-an-issue.md) (in inglese)
