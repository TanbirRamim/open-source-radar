# 4. Encontre uma issue que você consegue concluir

Uma boa primeira issue é pequena, bem descrita, reproduzível e ainda não está sendo feita por outra pessoa. É nesse último ponto que a maioria dos iniciantes perde tempo.

## Onde procurar

- **[O índice de issues deste repositório](../../issues/README.md)** e o [site](https://tanbirramim.github.io/open-source-radar/): issues abertas com etiqueta de iniciante, já filtradas para excluir as que têm responsável ou pull request aberto vinculado.
- **O próprio rastreador de issues do projeto**, filtrado pelas etiquetas de iniciante dele.
- **A busca do GitHub**, por exemplo:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` esconde issues com responsável e `-linked:pr` esconde issues que já têm um pull request conectado. Adicione `updated:>2026-06-01` (use uma data recente) para pular as abandonadas.

## Etiquetas que você vai ver

| Etiqueta | Geralmente significa |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | Os mantenedores acham que um iniciante consegue fazer, muitas vezes com orientação |
| `help wanted`, `PR welcome`, `up-for-grabs` | Os mantenedores querem que outra pessoa faça; nem sempre é algo pequeno |
| `bug`, `confirmed`, `has: repro` | Um defeito real; `confirmed` significa que um mantenedor reproduziu |
| `needs-triage`, `needs-info`, `question` | Ainda não está pronto: o problema ainda não foi entendido |
| `design`, `rfc`, `discussion`, `blocked` | Ainda não está pronto para um pull request; falta uma decisão |

Cada projeto define suas próprias etiquetas. Confira as descrições na página **Issues → Labels** do projeto.

## Alguém já está trabalhando nisso?

Antes de escrever uma linha de código, verifique tudo isto:

1. **Responsáveis (assignees).** Se alguém foi designado, a issue já tem dono.
2. **Pull requests vinculados.** Olhe a barra lateral direita ("Development") e a linha do tempo em busca de eventos "linked a pull request" ou "mentioned this issue" vindos de PRs. Um PR aberto significa que alguém já está cuidando; um PR fechado sem merge pode significar que a abordagem foi rejeitada — leia o porquê.
3. **Comentários.** Procure por "I'd like to work on this" ou "working on it". Se a reivindicação é recente (há poucas semanas) e a pessoa não sumiu, escolha outra issue.
4. **Busque nos pull requests abertos** pelo número da issue ou por palavras-chave do título. Nem todo PR vincula a issue corretamente.

Se a reivindicação é antiga e a pessoa sumiu, geralmente não há problema em perguntar com educação: "Hi @name, are you still working on this? If not, I'd be happy to pick it up." Depois aguarde alguns dias.

## Você consegue concluir?

Estime com honestidade. Uma boa primeira issue para você:

- **Tem um comportamento esperado claro.** Você consegue dizer em uma frase o que deveria acontecer.
- **É reproduzível.** A issue tem passos, um trecho de código ou um comando que falha. Se não tiver, reproduzi-la é sua primeira tarefa — e publicar a reprodução já é uma contribuição.
- **É local.** Dá para adivinhar qual arquivo ou função está envolvido. Busque no código pela mensagem de erro ou pelo nome da função mencionada na issue.
- **Não precisa de decisão de design.** Se os mantenedores ainda estão discutindo *como* deveria funcionar, aguarde.
- **Roda na sua máquina.** Evite bugs só de Windows se você usa macOS, bugs de GPU sem ter GPU, e assim por diante.

## Um jeito rápido de estimar o tamanho de uma issue

Passe 20 a 30 minutos antes de se comprometer:

1. Clone o projeto e rode a suíte de testes uma vez (capítulo 5).
2. Reproduza o bug, ou encontre no código o lugar da funcionalidade.
3. Encontre o arquivo de teste existente daquela área.

Se você passou pelas três etapas, a issue provavelmente tem um bom tamanho. Se depois de 30 minutos você continua perdido, tente outra issue — ou faça uma pergunta específica na issue (capítulo 7).

## Lista de verificação

- [ ] Sem responsável, sem PR aberto vinculado, sem reivindicação recente nos comentários.
- [ ] Consigo dizer em uma frase qual é o comportamento esperado.
- [ ] Reproduzi o problema, ou sei exatamente onde a mudança entra.
- [ ] Os mantenedores não estão debatendo a abordagem.

Próximo: [Seu primeiro pull request, passo a passo](05-first-pull-request.md)
