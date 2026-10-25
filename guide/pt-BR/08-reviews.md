# 8. Revisões, feedback e rejeição

Abrir o pull request é o meio do processo, não o fim. A forma como você lida com a revisão decide se ele será mesclado.

## Quando o CI falha

1. Abra a verificação que falhou e leia o log a partir do primeiro erro, não da última linha.
2. Decida se a sua mudança causou o problema:
   - **Falha de formatação ou lint:** rode o formatador ou o linter localmente e confirme o resultado.
   - **Um teste que você mexeu falha:** corrija localmente e faça push novamente.
   - **Um teste não relacionado falha** e também falha no branch padrão, ou um job parece instável (timeouts, erros de rede): diga isso em um comentário com um link para a mesma falha em outro lugar. Não tente corrigir falhas não relacionadas no seu PR, a menos que peçam.
3. Envie correções como novos commits, a menos que o projeto peça squash.

Muitos projetos exigem que um mantenedor aprove a execução do CI para contribuidores de primeira viagem. Se os checks disserem "aguardando aprovação", isso é normal: espere.

## Quando você recebe pedidos de mudança

- **Leia todos os comentários antes de responder.** Alguns dependem uns dos outros.
- **Faça as mudanças solicitadas ou explique por que não.** Discordar é ok se você der um motivo; ignorar um comentário não é.
- **Responda a cada comentário** com o que você fez ("Feito em abc123" ou "Mudei para usar o helper existente"). Deixe o revisor encerrar as conversas, a menos que o projeto peça o contrário.
- **Faça push e depois peça revisão novamente** usando o botão no pull request, ou deixe um comentário curto dizendo que está pronto de novo.
- **Mantenha o escopo.** Se um revisor pedir algo muito maior, discuta antes de escrever código.

Comentários de revisão são sobre o código, não sobre você. Mesmo contribuidores experientes passam por várias rodadas de feedback em um projeto novo.

## Revisores automatizados

Alguns projetos usam bots que publicam revisões automatizadas. Trate os comentários como sugestões: corrija problemas reais que encontrarem e note educadamente quando uma sugestão não se aplica. Mantenedores humanos fazem a decisão final.

## Quando nada acontece

O silêncio é comum e costuma significar "ocupados", não "não".

- Depois de uma ou duas semanas, um ping educado (capítulo 7).
- Verifique se o projeto tem uma fila de revisão ou etiquetas como `waiting-on-review`.
- Mantenha seu branch mesclável: resolva conflitos quando eles aparecerem.
- Após um mês ou mais, você pode perguntar se a mudança ainda é desejada. Se não for, fechá-la você mesmo é ok e apreciado.

## Quando seu pull request é fechado

Acontece com todo mundo. Motivos comuns:

| Motivo | O que fazer |
| --- | --- |
| Outra pessoa corrigiu primeiro | Feche o seu, agradeça e escolha outra issue mais cedo na próxima vez que ela for aberta |
| Os mantenedores querem outra abordagem | Pergunte se aceitariam uma versão revisada, ou deixe que façam do jeito deles |
| Fora do escopo do projeto | Aceite; pergunte se um plugin ou um pacote separado faz sentido |
| Baixa qualidade ou pouco claro | Leia o feedback com atenção; seu próximo PR nesse projeto precisa ser claramente melhor |
| Fechado por automação | Leia a mensagem do bot e o arquivo de workflow; corrija o que ele pede ou contate os mantenedores |
| Sem resposta, fechado como inativo | Pergunte educadamente se gostariam de reabrir; se não, siga em frente |

Um pull request fechado com uma resposta educada e construtiva ainda deixa uma boa impressão.

## Depois da mesclagem

- Exclua seu branch (o GitHub oferece um botão).
- Atualize o branch padrão do seu fork: `git fetch upstream && git switch main && git rebase upstream/main && git push`.
- Anote o que você aprendeu sobre o processo do projeto. Seu segundo pull request lá será muito mais rápido.

## Lista de verificação

- [ ] Li os logs do CI a partir do primeiro erro e separei minhas falhas das que já existiam.
- [ ] Respondi a todos os comentários de revisão e pedi revisão novamente.
- [ ] Mantive o escopo do pull request pequeno.
- [ ] Fiz acompanhamento educado, no máximo uma vez por semana.

Próximo: [Continue](09-keep-going.md)
