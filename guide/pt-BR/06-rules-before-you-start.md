# 6. Regras para verificar antes de começar

Todo projeto tem regras para contribuições. Algumas são só convenções; outras decidem se o seu pull request pode receber merge — ou se ele será fechado automaticamente. Verifique-as **antes** de escrever código.

O [índice de issues](../issues/README.md) mostra dicas detectadas automaticamente para cada projeto. São dicas, não garantias: leia sempre os arquivos do próprio projeto.

| Nota no índice | Significado |
| --- | --- |
| ⚠️ AI restricted | Os arquivos de contribuição do projeto parecem proibir ou restringir bastante contribuições geradas por IA |
| 🤖 disclose AI use | O projeto pede que você declare o uso de IA |
| 📄 AI policy | O projeto tem uma política sobre IA; leia-a |
| ✍️ CLA | Você provavelmente precisa assinar um Contributor License Agreement |
| 🔏 DCO | Os commits provavelmente precisam de uma linha `Signed-off-by` |

## Onde as regras moram

Procure em todos estes lugares, não só no README:

- `CONTRIBUTING.md` (na raiz, em `.github/` ou em `docs/`)
- `.github/PULL_REQUEST_TEMPLATE.md` e modelos de issue
- `CODE_OF_CONDUCT.md`
- `AI_POLICY.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.claude/`, `.cursor/rules`
- `DEVELOPMENT.md`, `docs/development/` ou uma página de contribuição no site do projeto
- `.github/workflows/` (automação que rotula, verifica ou fecha pull requests)

## Contributor License Agreements (CLA)

Um CLA é um acordo legal que dá ao projeto (ou à empresa por trás dele) direitos de uso da sua contribuição. Muitos projetos mantidos por empresas exigem um.

- Geralmente um bot comenta no seu primeiro pull request com um link. Você assina uma vez, online, e vale para futuras contribuições àquele projeto ou organização.
- Alguns CLAs estão ligados a uma conta de uma organização, como o EasyCLA da Linux Foundation (usado por muitos projetos da CNCF) ou o CLA do Google.
- **Leia o que você assina.** Se você contribui em nome de um empregador, pode ser que ele precise assinar um CLA corporativo.

## Developer Certificate of Origin (DCO)

O DCO é uma alternativa mais leve ao CLA: você certifica que tem o direito de enviar o código. Faz isso adicionando uma linha de assinatura (sign-off) a cada commit:

```bash
git commit -s -m "fix: handle empty username"
# adiciona: Signed-off-by: Your Name <you@example.com>
```

Um bot de DCO verifica cada commit do pull request. Se você esqueceu, corrija com:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

O nome e o email na assinatura precisam ser iguais aos do autor do commit.

## Contribuições com ajuda de IA

Os mantenedores viram uma enxurrada de pull requests de baixa qualidade gerados por IA, e muitos projetos hoje têm regras explícitas. Elas variam bastante:

- **Permitido, com os padrões de sempre.** Você é responsável por cada linha e precisa saber explicá-la.
- **Permitido com declaração de uso.** Você precisa dizer na descrição do PR qual ferramenta usou e para quê, ou adicionar um rodapé como `Assisted-by:` nos commits.
- **Só comunicação escrita por humanos.** A IA pode ajudar no código, mas comentários em issues e descrições de PR precisam ser seus.
- **Restrito ou proibido.** Alguns projetos não aceitam código ou documentação gerados por IA, ou não permitem que agentes de IA abram pull requests.

Qualquer que seja a política, estas valem em todo lugar:

- Você precisa entender e saber defender cada mudança que enviar.
- Nunca deixe uma ferramenta abrir pull requests ou postar comentários em seu nome sem revisá-los você mesmo.
- Siga as regras de declaração à risca quando o projeto as tiver. Esconder o uso de IA onde a declaração é obrigatória é um jeito rápido de ser banido do projeto.

## Automação antispam e de novatos

Por causa de spam, alguns projetos rodam fluxos que fecham ou rotulam pull requests automaticamente. Regras vistas em projetos reais incluem:

- fechar pull requests de contas que abriram PRs para muitos repositórios não relacionados em pouco tempo
- fechar PRs de autores com pull requests rejeitados recentemente em outro lugar
- fechar PRs de branches com nome de ferramentas de IA (por exemplo `claude/...` ou `codex/...`)
- exigir uma issue vinculada, ou uma etiqueta como `help wanted`, antes de aceitar um PR
- exigir o modelo de PR preenchido, com todos os checkboxes respondidos
- segurar o CI até um mantenedor aprovar, no caso de quem contribui pela primeira vez (isto é normal e inofensivo)

Olhe `.github/workflows/` em busca de arquivos com nomes como `close-spam`, `first-interaction` ou `pr-checks` para ver o que se aplica. O conselho prático: contribua com regularidade para poucos projetos, em vez de abrir pull requests em dezenas de repositórios em uma semana.

## Declarações legais e licenciamento

Alguns projetos pedem uma declaração no seu pull request, por exemplo de que você escreveu o código e o licencia nos termos do projeto. Só faça declarações verdadeiras. Ao enviar uma contribuição, em geral você a licencia sob a licença do projeto — então confira se essa licença é aceitável para você (e para seu empregador, se for o caso).

## Lista de verificação

- [ ] Li o guia de contribuição, o modelo de PR e qualquer política de IA ou instrução de agente.
- [ ] Sei se preciso de CLA ou de assinatura DCO.
- [ ] Sei as convenções de mensagem de commit e de título de PR do projeto.
- [ ] Verifiquei `.github/workflows/` em busca de automação que poderia fechar meu PR.
- [ ] Se a IA me ajudou, sei se e como preciso declarar.

Próximo: [Talking to maintainers](../07-communication.md)
