# 5. Seu primeiro pull request, passo a passo

Este é o fluxo completo, do fork até a abertura do pull request. Troque `OWNER/REPO` pelo projeto e `your-username` pelo seu usuário do GitHub.

## 1. Fork e clone

Um **fork** é a sua própria cópia do repositório no GitHub. Você envia (push) para o seu fork e depois pede ao projeto original (chamado de **upstream**) para puxar (pull) as suas mudanças.

```bash
gh repo fork OWNER/REPO --clone
cd REPO
git remote -v
# origin    https://github.com/your-username/REPO.git  (seu fork)
# upstream  https://github.com/OWNER/REPO.git          (o original)
```

Sem o GitHub CLI: clique em **Fork** na página do repositório e depois:

```bash
git clone https://github.com/your-username/REPO.git
cd REPO
git remote add upstream https://github.com/OWNER/REPO.git
```

> Repositório grande? `git clone --filter=blob:none URL` baixa o conteúdo dos arquivos só quando necessário, o que é bem mais rápido.

## 2. Crie uma branch

Nunca trabalhe na branch padrão do seu fork. Comece cada mudança a partir do código mais recente do upstream:

```bash
git fetch upstream
git switch -c fix-empty-username upstream/main   # use o nome da branch padrão do projeto
```

Dê às branches o nome da mudança, como `fix-empty-username` ou `docs-install-windows`.

## 3. Compile e rode os testes antes de mudar qualquer coisa

Siga o `CONTRIBUTING.md` ou o `DEVELOPMENT.md` do projeto. Os [language quickstarts](../languages/README.md) (em inglês) mostram os comandos usuais. Rode os testes no código ainda sem modificações:

- Se passarem, você tem uma base funcionando.
- Se alguns já falharem, anote quais. Essas falhas não são suas, e vale mencioná-las no seu PR se forem relevantes.

## 4. Reproduza o problema

Antes de corrigir, prove que o bug existe na sua máquina seguindo os passos da issue. Anote o que acontece e o que deveria acontecer. Se não conseguir reproduzir, diga isso na issue (com sua versão e ambiente) em vez de chutar uma correção.

## 5. Escreva um teste que falha

Encontre o arquivo de teste do código que você vai mudar e adicione um teste que mostra o bug. Rode e veja falhar. Isso diz a você — e a quem revisar — que seu teste realmente cobre o bug.

Nem toda mudança precisa de teste (correções de documentação, por exemplo), mas correções de bug quase sempre precisam. Muitos projetos não fazem merge de uma correção sem um.

## 6. Faça a menor mudança que corrige o problema

- Mude só o que a issue precisa. Sem refatorações, renomeações ou reformatações de código não relacionado: elas dificultam a revisão do seu pull request.
- Siga o estilo do código ao redor, mesmo que você escrevesse diferente.
- Rode o teste do passo 5 de novo. Agora ele deve passar.

## 7. Rode todas as verificações localmente

Rode o que o CI do projeto roda, pelo menos na área que você tocou:

- a suíte de testes (ou a parte relevante dela)
- o formatador (por exemplo `prettier`, `black`/`ruff format`, `cargo fmt`, `gofmt`)
- o linter (por exemplo `eslint`, `ruff`, `clippy`, `go vet`)
- verificação de tipos, se o projeto usa (`tsc`, `mypy`)

Alguns projetos também pedem uma entrada no changelog ou um arquivo de "changeset". O guia de contribuição vai dizer.

## 8. Commit

```bash
git add path/to/changed/files
git commit
```

Escreva uma mensagem clara. Siga a convenção do projeto (olhe `git log --oneline -20`). Um formato comum:

```text
parser: handle empty username in login prompt

An empty username made the prompt loop forever because validation
rejected it without telling the user. Show the validation error and
ask again instead.

Fixes #1234
```

- Primeira linha: resumo curto, muitas vezes com prefixo da área ou um tipo de [Conventional Commits](https://www.conventionalcommits.org) como `fix:` ou `docs:`.
- Corpo: o que estava errado e por que esta mudança corrige.
- `Fixes #1234` fecha a issue automaticamente quando o PR recebe merge.
- Se o projeto exige assinatura DCO, use `git commit -s` (veja o capítulo 6).

## 9. Push e abertura do pull request

```bash
git push -u origin fix-empty-username
gh pr create --repo OWNER/REPO --fill   # ou abra no navegador o link que o git mostra
```

Preencha o modelo de pull request do projeto, se houver. O capítulo 7 explica como é uma boa descrição. Em resumo: o que estava errado, o que você mudou, como testou e qual issue ele corrige.

## 10. Mantenha sua branch atualizada

Se a branch do upstream andar antes do seu PR receber merge e houver conflitos, atualize sua branch:

```bash
git fetch upstream
git rebase upstream/main
# resolva os conflitos e então: git add <files> && git rebase --continue
git push --force-with-lease
```

`--force-with-lease` é o jeito seguro de atualizar uma branch que você reescreveu; ele se recusa a sobrescrever commits que você não tem localmente. Alguns projetos preferem fazer merge da `upstream/main` na sua branch em vez de rebase; siga o guia deles.

## Lista de verificação

- [ ] Branch criada a partir da branch padrão mais recente do upstream.
- [ ] Testes passaram antes da minha mudança (ou anotei as falhas existentes).
- [ ] Reproduzi o bug e escrevi um teste que falhou antes da correção.
- [ ] O diff contém só as mudanças necessárias para esta issue.
- [ ] Testes, formatador e linter passam localmente.
- [ ] A mensagem de commit segue a convenção do projeto e referencia a issue.
- [ ] O modelo de PR está preenchido.

Próximo: [Regras para verificar antes de começar](06-rules-before-you-start.md)
