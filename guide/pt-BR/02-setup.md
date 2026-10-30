# 2. Configure suas ferramentas

Você precisa de Git, uma conta no GitHub, um jeito de se autenticar, um editor e a toolchain da linguagem do projeto que você escolher. Fazer isso uma vez leva cerca de uma hora.

## Git

Instale o Git:

- **macOS:** `xcode-select --install` (instala o Git com as Command Line Tools), ou `brew install git` com o [Homebrew](https://brew.sh).
- **Windows:** [Git for Windows](https://git-scm.com/download/win). Inclui o Git Bash, um terminal que executa os comandos deste guia.
- **Linux:** o gerenciador de pacotes da sua distro, por exemplo `sudo apt install git` ou `sudo dnf install git`.

Diga ao Git quem é você. Use o mesmo e-mail da sua conta no GitHub (ou o endereço noreply privado do GitHub, veja abaixo) para que seus commits sejam vinculados ao seu perfil:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Mantenha seu e-mail privado (opcional)

O GitHub dá a cada conta um endereço noreply como `12345678+username@users.noreply.github.com`. Encontre o seu em **Settings → Emails**, ative **Keep my email addresses private** e use esse endereço como `user.email`. Os commits continuam contando no seu perfil.

> **Erro comum:** fazer commit com um e-mail que não está adicionado à sua conta no GitHub. Os commits aparecem sem seu avatar e não contam no seu perfil. Confira com `git config user.email` e compare com **Settings → Emails**.

## Uma conta no GitHub e autenticação

1. Crie uma conta em [github.com](https://github.com). Escolha um nome de usuário profissional; ele aparece em cada contribuição.
2. Ative a autenticação de dois fatores em **Settings → Password and authentication**. Muitas organizações exigem isso.
3. Configure um jeito de o Git se autenticar. O mais fácil é o GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: veja cli.github.com
gh auth login          # escolha GitHub.com, HTTPS, e entre com o navegador
gh auth setup-git      # permite git push por HTTPS usando esse login
```

Como alternativa, [adicione uma chave SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) e clone com URLs `git@github.com:`.

## Um editor

Use o que você já domina. O [VS Code](https://code.visualstudio.com) é uma escolha comum: tem boa integração com Git, e as extensões oficiais de cada linguagem dão formatação e verificação de erros. JetBrains IDEs, Neovim, Zed e Emacs servem também.

Duas configurações poupam comentários de revisão:

- **Formatar ao salvar** com o formatador do projeto (Prettier, Black, rustfmt, gofmt e por aí vai).
- **Respeitar o `.editorconfig`**. Muitos projetos trazem um para definir indentação e quebras de linha.

## Os comandos Git que você vai realmente usar

| Comando | O que faz |
| --- | --- |
| `git clone URL` | Baixar um repositório |
| `git status` | Ver o que mudou |
| `git switch -c fix-typo` | Criar e trocar para uma nova branch |
| `git add path/to/file` | Preparar uma mudança para o próximo commit |
| `git commit -m "message"` | Registrar as mudanças preparadas |
| `git push -u origin fix-typo` | Enviar sua branch |
| `git fetch upstream` | Baixar as mudanças mais recentes do projeto original |
| `git rebase upstream/main` | Reaplicar seus commits sobre essas mudanças |
| `git log --oneline -10` | Ver os commits recentes |
| `git diff` | Ver mudanças não preparadas (`git diff --staged` para as preparadas) |

Se você nunca usou Git, passe 30 minutos no [Learn Git Branching](https://learngitbranching.js.org) primeiro. É interativo e cobre exatamente o que você precisa.

## Toolchains de linguagem

Instale a toolchain do projeto que você escolher, usando a versão que o projeto pede (procure arquivos como `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod`, `.tool-versions`). Os [quickstarts de linguagem](../../languages/README.md) listam os comandos usuais por linguagem.

Gerenciadores de versão facilitam isso:

- **Várias linguagens:** [mise](https://mise.jdx.dev) ou [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) ou nvm, mais `corepack enable` para pnpm e Yarn
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** o instalador oficial, ou o gerenciador de pacotes; o Go baixa toolchains mais novas sozinho quando o `go.mod` pede

## Lista de verificação

- [ ] `git --version` funciona e `git config user.email` corresponde a um e-mail da minha conta no GitHub.
- [ ] A autenticação de dois fatores está ativada.
- [ ] `gh auth status` (ou `ssh -T git@github.com`) mostra que consigo me autenticar.
- [ ] Meu editor formata ao salvar.

Próximo: [Escolha um projeto](03-choose-a-project.md)
