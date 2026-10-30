# 2. Configura tus herramientas

Necesitas Git, una cuenta de GitHub, un método de autenticación, un editor y las herramientas del lenguaje del proyecto que elijas. Configurar todo esto una vez lleva aproximadamente una hora.

## Git

Instala Git:

- **macOS:** `xcode-select --install` (instala Git con las Command Line Tools), o `brew install git` con [Homebrew](https://brew.sh).
- **Windows:** [Git for Windows](https://git-scm.com/download/win). Incluye Git Bash, una terminal que ejecuta los comandos de esta guía.
- **Linux:** tu gestor de paquetes, por ejemplo `sudo apt install git` o `sudo dnf install git`.

Dile a Git quién eres. Usa el mismo correo que en tu cuenta de GitHub (o la dirección noreply privada de GitHub, ver más abajo) para que tus commits se vinculen a tu perfil:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Mantén tu correo privado (opcional)

GitHub le da a cada cuenta una dirección noreply como `12345678+usuario@users.noreply.github.com`. Encuéntrala en **Settings → Emails**, activa **Keep my email addresses private** y usa esa dirección como `user.email`. Los commits seguirán contando en tu perfil.

> **Error común:** hacer commits con un correo que no está añadido a tu cuenta de GitHub. Los commits aparecerán sin tu avatar y no contarán en tu perfil. Compruébalo con `git config user.email` y compáralo con **Settings → Emails**.

## Una cuenta de GitHub y autenticación

1. Crea una cuenta en [github.com](https://github.com). Elige un nombre de usuario profesional; aparecerá en cada contribución.
2. Activa la autenticación de dos factores en **Settings → Password and authentication**. Muchas organizaciones la exigen.
3. Configura un método para que Git se autentique. Lo más sencillo es la GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: ver cli.github.com
gh auth login          # elige GitHub.com, HTTPS e inicia sesión con el navegador
gh auth setup-git      # permite hacer push por HTTPS usando ese inicio de sesión
```

Alternativamente, [añade una clave SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) y clona con URLs `git@github.com:`.

## Un editor

Usa el que te resulte cómodo. [VS Code](https://code.visualstudio.com) es una opción habitual: tiene buena integración con Git y las extensiones oficiales de cada lenguaje te dan formato y detección de errores. Los IDE de JetBrains, Neovim, Zed y Emacs también sirven.

Dos ajustes te ahorrarán comentarios en las revisiones:

- **Formatear al guardar** con el formateador del proyecto (Prettier, Black, rustfmt, gofmt, etc.).
- **Respetar `.editorconfig`**. Muchos proyectos incluyen uno para definir indentación y finales de línea.

## Los comandos de Git que realmente usarás

| Comando | Qué hace |
| --- | --- |
| `git clone URL` | Descargar un repositorio |
| `git status` | Ver qué cambió |
| `git switch -c fix-typo` | Crear y cambiar a una nueva rama |
| `git add path/to/file` | Preparar un cambio para el próximo commit |
| `git commit -m "mensaje"` | Guardar los cambios preparados |
| `git push -u origin fix-typo` | Subir tu rama |
| `git fetch upstream` | Descargar los últimos cambios del proyecto original |
| `git rebase upstream/main` | Reaplicar tus commits sobre esos cambios |
| `git log --oneline -10` | Ver commits recientes |
| `git diff` | Ver cambios sin preparar (`git diff --staged` para los preparados) |

Si nunca has usado Git, dedica 30 minutos a [Learn Git Branching](https://learngitbranching.js.org). Es interactivo y cubre justo lo que necesitas.

## Herramientas por lenguaje

Instala las herramientas del proyecto que elijas, usando la versión que pida el proyecto (busca archivos como `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod`, `.tool-versions`). Las [guías rápidas por lenguaje](../../languages/README.md) listan los comandos habituales de cada uno.

Los gestores de versiones lo hacen sencillo:

- **Varios lenguajes:** [mise](https://mise.jdx.dev) o [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) o nvm, más `corepack enable` para pnpm y Yarn
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** el instalador oficial, o tu gestor de paquetes; Go descarga toolchains más recientes solo cuando `go.mod` lo pide

## Lista de comprobación

- [ ] `git --version` funciona y `git config user.email` coincide con un correo de mi cuenta de GitHub.
- [ ] La autenticación de dos factores está activada.
- [ ] `gh auth status` (o `ssh -T git@github.com`) muestra que puedo autenticarme.
- [ ] Mi editor formatea al guardar.

Siguiente: [Elige un proyecto](03-choose-a-project.md)
