<a id="newcomer-faq"></a>
# Perguntas frequentes para iniciantes

Respostas curtas às dúvidas mais comuns antes e depois do primeiro pull request. Cada resposta aponta para o capítulo que explica o assunto em detalhes.

<a id="before-you-start"></a>
## Antes de começar

<a id="do-i-need-to-ask-before-working-on-an-issue"></a>
### Preciso perguntar antes de trabalhar em uma issue?

Depende do projeto. Consulte o `CONTRIBUTING.md`: alguns pedem um comentário antes, outros atribuem issues com o comando `/claim` ou `/assign`, e outros dizem para simplesmente abrir um PR. Se o guia não disser nada e a issue for pequena, normalmente não há problema em abrir um pull request diretamente. Para algo maior, comente antes para ninguém perder tempo. Veja o [capítulo 7](07-communication.md#reivindicando-uma-issue) (em inglês).

<a id="how-do-i-claim-an-issue-without-sounding-like-everyone-else"></a>
### Como reivindicar uma issue sem repetir o que todo mundo diz?

Em vez de perguntar apenas "Posso trabalhar nisso?", diga em duas ou três frases o que você descobriu e o que pretende mudar. Assim, um mantenedor pode concordar ou sugerir uma abordagem melhor antes de você escrever código. Há um exemplo no [capítulo 7](07-communication.md#reivindicando-uma-issue) (em inglês).

<a id="someone-commented-ill-take-this-weeks-ago-and-never-opened-a-pr-can-i-take-it"></a>
### Alguém disse "eu faço" há semanas e nunca abriu um PR. Posso pegar a issue?

Pergunte primeiro na issue: "Você ainda está trabalhando nisso? Se não estiver, gostaria de assumir." Se não houver resposta depois de alguns dias, peça a um mantenedor para reatribuí-la. Não abra um pull request concorrente sem perguntar. Veja o [capítulo 4](04-find-an-issue.md#alguém-já-está-trabalhando-nisso) (em inglês).

<a id="how-many-issues-should-i-claim-at-once"></a>
### Quantas issues devo reivindicar de uma vez?

Uma. Reivindique a próxima depois de abrir seu primeiro pull request.

<a id="im-not-sure-i-can-finish-it-should-i-still-try"></a>
### Não tenho certeza de que consigo terminar. Devo tentar mesmo assim?

Sim, mas escolha algo cujo tamanho você consiga estimar. Se conseguir reproduzir o problema e encontrar o código envolvido em até uma hora, provavelmente é uma boa escolha. Se ficar sem saber como avançar, não há problema em avisar na issue e remover sua atribuição. Veja o [capítulo 4](04-find-an-issue.md#você-consegue-concluir) (em inglês).

<a id="rules-and-paperwork"></a>
## Regras e formalidades

<a id="a-bot-asked-me-to-sign-a-cla-is-that-normal"></a>
### Um bot pediu que eu assine um CLA. Isso é normal?

Sim. Um Contributor License Agreement concede ao projeto direitos para usar sua alteração. Você assina uma vez pela internet e o acordo cobre contribuições futuras. Leia o documento e, se estiver contribuindo para um empregador, verifique se ele também precisa assinar. Veja o [capítulo 6](06-rules-before-you-start.md#contributor-license-agreements-cla).

<a id="the-dco-check-failed-how-do-i-fix-it"></a>
### A verificação de DCO falhou. Como resolvo?

Todo commit precisa de uma linha `Signed-off-by:` que corresponda ao autor do commit. Adicione-a a todos os commits da sua branch e faça push novamente:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

Daí em diante, use `git commit -s`. Veja o [capítulo 6](06-rules-before-you-start.md#developer-certificate-of-origin-dco).

<a id="can-i-use-ai-tools"></a>
### Posso usar ferramentas de IA?

Confira a política do projeto antes de começar. Alguns proíbem contribuições geradas por IA, outros pedem que você informe o uso e muitos não dizem nada. Seja qual for a regra, você é responsável por cada linha: entenda, teste e saiba explicá-la durante a revisão. Veja o [capítulo 6](06-rules-before-you-start.md#contribuições-com-ajuda-de-ia) (em inglês).

<a id="a-bot-closed-my-pr-or-labeled-it-as-spam-what-now"></a>
### Um bot fechou meu PR ou o marcou como spam. E agora?

Leia a mensagem do bot. Muitos projetos fecham pull requests de quem contribui pela primeira vez quando não estão vinculados a uma issue ou não seguem o modelo. Corrija o que foi pedido ou responda educadamente e peça a um mantenedor para verificar. Veja o [capítulo 6](06-rules-before-you-start.md#automação-antispam-e-de-novatos) (em inglês).

<a id="after-you-open-the-pull-request"></a>
## Depois de abrir o pull request

<a id="nobody-has-replied-how-long-should-i-wait"></a>
### Ninguém respondeu. Quanto tempo devo esperar?

Uma ou duas semanas é normal. Depois, deixe um comentário curto e educado perguntando se precisam de algo de você. Enquanto espera, mantenha a branch sem conflitos. Após um mês, pergunte se a alteração ainda é desejada. Veja o [capítulo 8](08-reviews.md#quando-nada-acontece) (em inglês).

<a id="ci-is-red-and-i-dont-understand-why"></a>
### O CI está vermelho e não entendo por quê.

Abra a tarefa que falhou e procure o primeiro erro, não o último. Execute o mesmo comando localmente. Se a falha estiver em código que você não alterou, informe no pull request; pode ser um teste intermitente ou um problema na branch principal. Veja o [capítulo 8](08-reviews.md#quando-o-ci-falha) (em inglês).

<a id="the-maintainer-asked-for-changes-do-i-open-a-new-pr"></a>
### O mantenedor pediu alterações. Devo abrir outro PR?

Não. Faça push de novos commits para a mesma branch e o pull request será atualizado. Responda a cada comentário para que a pessoa revisora saiba que ele foi atendido. Veja o [capítulo 8](08-reviews.md#quando-você-recebe-pedidos-de-mudança) (em inglês).

<a id="my-pr-has-merge-conflicts"></a>
### Meu PR tem conflitos de merge.

Atualize sua branch com a branch principal do projeto, resolva os conflitos e faça push:

```bash
git fetch upstream
git rebase upstream/main
# fix the files, then: git add <file> && git rebase --continue
git push --force-with-lease
```

Veja o [capítulo 5](05-first-pull-request.md).

<a id="my-pr-was-closed-without-merging-did-i-do-something-wrong"></a>
### Meu PR foi fechado sem ser mesclado. Fiz algo errado?

Nem sempre. Alguém pode ter resolvido o problema antes, ou o projeto pode preferir outra abordagem. Leia o motivo, agradeça e pergunte se uma versão revisada ajudaria. Veja o [capítulo 8](08-reviews.md#quando-seu-pull-request-é-fechado) (em inglês).

<a id="after-the-merge"></a>
## Depois da mesclagem

<a id="does-a-merged-pr-in-a-small-project-count"></a>
### Um PR mesclado em um projeto pequeno conta?

Sim. Um pull request mesclado é trabalho real feito publicamente, seja qual for o tamanho do projeto. Algumas alterações mescladas em um projeto que importa para você valem mais do que muitas correções de uma linha espalhadas por repositórios. Veja o [capítulo 9](09-keep-going.md).

<a id="what-should-i-do-next"></a>
### O que devo fazer em seguida?

Continue no mesmo projeto. Você já sabe como compilá-lo e como os mantenedores fazem revisões. Escolha uma issue um pouco maior, ajude a fazer a triagem de novas issues ou revise o pull request de outra pessoa. Veja o [capítulo 9](09-keep-going.md).
