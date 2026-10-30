# 3. Escolha um projeto

O projeto importa mais do que a issue. Um projeto acolhedor e ativo vai revisar seu pull request em dias. Um inativo ou sobrecarregado pode nunca olhar para ele, por melhor que seja.

## Comece pelo que você usa

O melhor primeiro projeto é um que você já usa: uma biblioteca do seu próprio código, uma ferramenta que você roda todo dia, um app de que você gosta. Você entende o que ele deveria fazer, consegue testar sua mudança de verdade e se importa com o resultado.

Se nada vier à mente, navegue pelo [índice de issues](../../issues/README.md) pela linguagem que você domina e repare em quais projetos aparecem sempre.

## Sinais de um projeto saudável e acolhedor

Confira estes pontos na página do repositório. Cinco minutos aqui poupam semanas de espera.

| Verificação | Onde olhar | Bom sinal |
| --- | --- | --- |
| Atividade recente | Aba de commits, data do "último commit" | Commits nas últimas semanas |
| Contribuições externas aceitas | **Pull requests → Closed**, filtre `is:merged` e olhe os autores | Pull requests de quem não é mantenedor foram aceitos no último mês |
| Velocidade de revisão | Abra alguns PRs recentemente aceitos de gente de fora | Primeira resposta em dias, não meses |
| Guia de contribuição | `CONTRIBUTING.md` na raiz, em `.github/` ou `docs/` | Existe e explica configuração e testes |
| Etiquetas para iniciantes | Issues, filtre por `good first issue` ou `help wanted` | As etiquetas são usadas, e issues etiquetadas são assumidas |
| Tom | Leia algumas threads de issues | Mantenedores são pacientes e específicos, mesmo dizendo não |
| Código de conduta | `CODE_OF_CONDUCT.md` | Existe |
| CI | Checks nos PRs recentes | Testes rodam automaticamente nos pull requests |

Uma busca rápida que mostra PRs aceitos de contribuidores externos, para qualquer repositório (troque `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Olhe os autores: se todo PR aceito é das mesmas duas pessoas, contribuições externas podem não ser prioridade ali.

## Sinais de alerta

- **Centenas de pull requests abertos sem revisão.** O seu vai entrar na fila.
- **Um guia de contribuição que diz que o projeto não aceita pull requests**, ou só aceita para issues com uma etiqueta específica. Alguns projetos populares funcionam assim. Respeite.
- **Toda issue recente já tem vários pull requests concorrentes.** Projetos populares costumam receber PRs avulsos horas depois de um bug ser registrado. Dá para contribuir mesmo assim, mas escolha trabalho menos disputado (docs, testes, bugs antigos confirmados) ou um projeto menor.
- **Mantenedores pedindo para pararem de abrir pull requests de baixo esforço.** Leia essas threads: elas dizem exatamente o que não fazer.
- **Sem commits há meses.** O projeto pode estar pronto, ou abandonado.

## Projeto grande ou projeto pequeno?

| | Projeto grande e famoso | Projeto menor e ativo |
| --- | --- | --- |
| Concorrência por issues fáceis | Altíssima | Baixa |
| Velocidade de revisão | Varia muito; muitas vezes lenta para gente de fora | Muitas vezes rápida e pessoal |
| Processo | Formal: templates, CLAs, CI rígido | Mais leve |
| Mentoria | Às vezes existem programas estruturados | Contato direto com o mantenedor |
| Sinal no seu perfil | Nome forte e reconhecido | Forte se você virar regular |

Uma boa estratégia: faça suas uma ou duas primeiras contribuições em um projeto menor e ativo, onde você recebe feedback rápido, e leve o que aprendeu para os maiores.

## Lista de verificação

- [ ] O projeto teve commits no último mês.
- [ ] Aceitou pull requests de contribuidores externos recentemente.
- [ ] Tem um guia de contribuição, e eu o li.
- [ ] Consigo compilar e rodar na minha máquina (o capítulo 5 cobre isso).

Próximo: [Encontre uma issue que você consegue concluir](04-find-an-issue.md)
