# 6. Regole da verificare prima di iniziare

Ogni progetto ha regole per i contributi. Alcune sono semplici convenzioni; altre determinano se la tua pull request può essere unita o se viene chiusa automaticamente. Verificale **prima** di scrivere codice.

L'[indice delle issue](../../issues/README.md) mostra indicazioni rilevate automaticamente per ogni progetto. Sono indicazioni, non garanzie: leggi sempre i file del progetto stesso.

| Nota nell'indice | Significato |
| --- | --- |
| ⚠️ AI restricted | I file del progetto per i contributi sembrano vietare o limitare fortemente i contributi generati dall'IA |
| 🤖 disclose AI use | Il progetto chiede di dichiarare l'uso dell'IA |
| 📄 AI policy | Il progetto ha una policy sull'IA; leggila |
| ✍️ CLA | Probabilmente devi firmare un Contributor License Agreement |
| 🔏 DCO | Probabilmente i commit richiedono una riga `Signed-off-by` |

## Dove trovare le regole

Controlla tutti questi file e percorsi, non solo il README:

- `CONTRIBUTING.md` (nella root, in `.github/` o in `docs/`)
- `.github/PULL_REQUEST_TEMPLATE.md` e i modelli per le issue
- `CODE_OF_CONDUCT.md`
- `AI_POLICY.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.claude/`, `.cursor/rules`
- `DEVELOPMENT.md`, `docs/development/` o una pagina dedicata ai contributi sul sito del progetto
- `.github/workflows/` (automazioni che assegnano etichette, verificano o chiudono le pull request)

## Contributor License Agreement (CLA)

Un CLA è un accordo legale che concede al progetto (o all'azienda che lo sostiene) diritti sull'uso del tuo contributo. Molti progetti sostenuti da aziende ne richiedono uno.

- Di solito un bot commenta la tua prima pull request con un link. Firmi una sola volta, online, e la firma vale anche per i contributi futuri a quel progetto o a quella organizzazione.
- Alcuni CLA sono legati a un account valido per tutta l'organizzazione, come EasyCLA della Linux Foundation (usato da molti progetti CNCF) o il CLA di Google.
- **Leggi cosa firmi.** Se contribuisci per conto del tuo datore di lavoro, potrebbe essere necessario che firmi un CLA aziendale.

## Developer Certificate of Origin (DCO)

Il DCO è un'alternativa più leggera al CLA: certifichi di avere il diritto di inviare il codice. Per farlo, aggiungi una riga di sign-off a ogni commit:

```bash
git commit -s -m "fix: handle empty username"
# adds: Signed-off-by: Your Name <you@example.com>
```

Un bot DCO controlla ogni commit della pull request. Se hai dimenticato il sign-off, rimedia con:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

Il nome e l'indirizzo email nel sign-off devono corrispondere a quelli dell'autore del commit.

## Contributi assistiti dall'IA

I maintainer hanno visto arrivare molte pull request generate dall'IA e di bassa qualità, e molti progetti ora hanno regole esplicite. Le regole variano molto:

- **Consentiti secondo i consueti standard.** Sei responsabile di ogni riga e devi essere in grado di spiegarla.
- **Consentiti con dichiarazione.** Devi indicare nella descrizione della PR quale strumento hai usato e per cosa, oppure aggiungere ai commit una riga come `Assisted-by:`.
- **Solo comunicazioni scritte da persone.** L'IA può aiutare con il codice, ma i commenti nelle issue e le descrizioni delle PR devono essere scritti da te.
- **Limitati o vietati.** Alcuni progetti non accettano affatto codice o documentazione generati dall'IA, oppure non consentono agli agenti IA di aprire pull request.

Qualunque sia la policy, queste regole valgono ovunque:

- Devi comprendere ed essere in grado di motivare ogni modifica che invii.
- Non lasciare mai che uno strumento apra pull request o pubblichi commenti a tuo nome senza che tu li abbia prima verificati.
- Quando un progetto ha regole sulla dichiarazione dell'uso dell'IA, seguile esattamente. Nascondere l'uso dell'IA quando è richiesta una dichiarazione è un modo rapido per essere esclusi da un progetto.

## Automazioni anti-spam e per chi contribuisce per la prima volta

A causa dello spam, alcuni progetti eseguono workflow che chiudono automaticamente le pull request o assegnano loro etichette. Tra le regole adottate dai progetti ci sono:

- chiudere le pull request di account che hanno aperto PR in molti repository non correlati in poco tempo
- chiudere le PR di autori le cui pull request sono state recentemente respinte altrove
- chiudere le PR provenienti da branch che prendono il nome da strumenti di IA (per esempio `claude/...` o `codex/...`)
- richiedere una issue collegata o un'etichetta come `help wanted` sulla issue prima di accettare una PR
- richiedere un modello della PR compilato, con tutte le caselle selezionate o completate
- mettere la CI in attesa dell'approvazione di un maintainer per chi contribuisce per la prima volta (è normale e non è un problema)

Controlla in `.github/workflows/` i file con nomi come `close-spam`, `first-interaction` o `pr-checks` per capire quali regole si applicano. Il consiglio pratico è contribuire con costanza a pochi progetti invece di aprire pull request in decine di repository in una settimana.

## Dichiarazioni legali e licenze

Alcuni progetti chiedono di includere una dichiarazione nella pull request, per esempio che hai scritto tu il codice e lo concedi in licenza secondo i termini del progetto. Fai solo dichiarazioni veritiere. Inviando un contributo, generalmente lo concedi secondo la licenza del progetto: verifica quindi che la licenza sia accettabile per te (e per il tuo datore di lavoro, se pertinente).

## Checklist

- [ ] Ho letto la guida alla contribuzione, il modello della PR ed eventuali policy sull'IA o istruzioni per gli agenti.
- [ ] So se è richiesto un CLA o un sign-off DCO.
- [ ] Conosco le convenzioni del progetto per i messaggi dei commit e i titoli delle PR.
- [ ] Ho controllato `.github/workflows/` per individuare automazioni che potrebbero chiudere la mia PR.
- [ ] Se l'IA mi ha aiutato, so se e come devo dichiararlo.

Successivo: [Comunicare con i maintainer](../07-communication.md)
