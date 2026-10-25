# 7. Conversando com os mantenedores

Mantenedores costumam ser voluntários ou engenheiros ocupados que revisam contribuições além do próprio trabalho. Uma comunicação clara, curta e específica gera respostas mais rápidas e amigáveis.

## Reivindicando uma issue

Alguns projetos querem que você comente antes de começar; outros dizem "basta abrir um PR". Verifique o guia de contribuição. Quando for comentar, seja útil:

> Consigo reproduzir isso na 4.2.1: `tool --flag ""` entra em loop em vez de mostrar um erro. A verificação em `src/prompt.ts` rejeita entrada vazia sem imprimir o motivo. Pretendo imprimir a mensagem de validação e perguntar novamente, com um teste em `prompt.test.ts`. Posso seguir em frente?

Isso é melhor do que "Posso trabalhar nisso?" porque mostra que você entendeu o problema e permite que o mantenedor corrija sua abordagem antes de você gastar tempo nela.

Não reivindique várias issues de uma vez e não reivindique uma issue que você não vai começar esta semana.

## Pedindo ajuda

Quando você travar, pergunte na issue (ou no chat do projeto, se houver) e inclua:

- o que você está tentando fazer
- o que você tentou
- o que aconteceu, com a mensagem de erro ou a saída exata
- seu ambiente quando fizer diferença (SO, versão da linguagem, versão do projeto)

Link para a linha de código sobre a qual você pergunta. Continue investigando enquanto espera: se achar a resposta, publique-a.

## Escrevendo a descrição de um pull request

Revisores leem muitos pull requests. Facilite o entendimento em 30 segundos.

**Bom:**

> Corrige #1234.
>
> `login` perguntava de novo para sempre quando o nome de usuário estava vazio, porque `validateUsername` retornava um erro que o loop de prompt ignorava. O loop agora imprime a mensagem de validação antes de perguntar de novo.
>
> Adicionei um teste em `prompt.test.ts` que falha sem a mudança. `npm test` e `npm run lint` passam localmente.

**Por que funciona:** vincula a issue, diz o que estava errado e por quê, diz o que mudou e como foi verificado. Sem enrolação.

Evite:

- Resumos longos gerados, listas com marcadores de cada arquivo alterado ou cabeçalhos para uma mudança de dez linhas.
- Linguagem de marketing ("Este PR melhora significativamente...").
- Afirmações que você não verificou ("corrige todas as issues relacionadas").
- Deixar o texto de espaço reservado do modelo no lugar.

Se houver algo que os revisores devam saber, diga diretamente: "Não tinha certeza se nomes de usuário vazios deveriam ser permitidos para registries personalizados, então mantive o comportamento existente ali."

## Tom

- Seja educado e presuma boa intenção, inclusive quando alguém for seco com você.
- Agradeça uma vez pelo tempo dos revisores. Não precisa agradecer por cada comentário.
- Não use @ com mantenedores repetidamente, nem marque pessoas que não estão envolvidas.
- Mantenha a discussão na issue ou no pull request, não em mensagens privadas, a menos que convidado.
- Escreva com suas palavras. Mantenedores querem saber que uma pessoa entende a mudança.

## Acompanhamento

Se não houver resposta depois de cerca de uma semana, um acompanhamento educado é suficiente:

> Ping amigável: isso está pronto para revisão quando alguém tiver tempo. Estou aberto a mudanças.

Se o projeto tem um canal de chat para contribuidores, perguntar lá uma vez também é ok. Depois disso, deixe: alguns projetos são simplesmente lentos.

## Lista de verificação

- [ ] Meu comentário de reivindicação (se necessário) mostra que entendi o problema.
- [ ] Minha descrição do PR diz o que estava errado, o que mudou, como testei e vincula a issue.
- [ ] Removi o texto de espaço reservado do modelo.
- [ ] Meus acompanhamentos são espaçados e educados.

Próximo: [Reviews, feedback e rejeição](08-reviews.md)
