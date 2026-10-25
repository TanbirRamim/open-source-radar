# 10. Lendo um codebase

Uma primeira barreira comum é abrir um projeto com milhares de arquivos e não saber por onde começar. Você não precisa entender tudo, só o caminho da issue até o código que vai mudar.

## Por onde começar a procurar

Ao clonar um repositório novo, não tente ler todos os arquivos. Use estes pontos de entrada:

- **Leia a documentação fundamental:**
  - **`README.md`:** Explica o que o projeto realmente faz, como está estruturado e como configurar e executar o aplicativo no seu computador.
  - **`CONTRIBUTING.md`:** Explica as regras do projeto para contribuidores, incluindo diretrizes de estilo de código, como abrir pull requests e como os mantenedores esperam que você envie mudanças.
- **Encontre e execute os testes:**
  - **O que são testes?** Testes são arquivos separados de código escritos para verificar automaticamente se o aplicativo funciona corretamente, sem exigir cliques manuais em cada recurso.
  - **Onde ficam?** Procure uma pasta dedicada `tests/` ou `test/` na raiz, ou verifique ao lado dos arquivos de origem por nomes como `auth.test.js` ou `auth_spec.rb`.
  - **Como executá-los:** Consulte `README.md` ou `CONTRIBUTING.md` para o comando exato (como `npm test`, `pytest` ou `cargo test`). Executá-los verifica se sua configuração funciona.
- **Pesquise o texto do erro ou a string da interface da issue:** Se a issue menciona uma mensagem de erro específica ou o rótulo de um botão, use a busca global do seu editor (`Ctrl+Shift+F` ou `Cmd+Shift+F`) para encontrar exatamente onde esse texto está definido no código.

## Arqueologia do Git

Quando você encontrar o arquivo que precisa mudar, o Git pode contar a história dele:

| Comando | O que faz |
| --- | --- |
| `git log -p path/to/file` | Ver todas as mudanças já feitas em um arquivo e por quê |
| `git blame path/to/file` | Ver quem escreveu cada linha e em qual commit |

## Rastreando a execução e a história

- **Rastreie a partir do ponto de entrada:** Descubra onde a execução começa (como `main()`, um handler de rota de API ou o componente principal da interface) e siga as chamadas de funções até chegar à lógica.
- **Veja pull requests mesclados recentes:** Pesquise PRs fechados no repositório que mexeram na mesma área. Eles servem como modelos de como os mantenedores esperam que as mudanças sejam formatadas e testadas.

## Lista de verificação

- [ ] Li o `README.md` para entender o que o projeto faz e como executá-lo.
- [ ] Li o `CONTRIBUTING.md` para aprender as regras e diretrizes de estilo do projeto.
- [ ] Encontrei a suíte de testes, executei-a e garanti que todos os testes passam localmente.
- [ ] Pesquisei o texto do erro ou a string da interface da issue para localizar os arquivos relevantes.
- [ ] Verifiquei PRs mesclados recentes ou a história do git para contexto sobre as convenções.

Voltar ao [índice do guia](README.md) · Encontre sua próxima issue no [índice de issues](../../issues/README.md).
