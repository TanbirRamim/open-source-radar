# 10. Cómo leer una base de código

Un obstáculo inicial habitual es abrir un proyecto con miles de archivos y no saber por dónde empezar. No necesitas entenderlo todo, solo el camino desde el issue hasta el código que vas a cambiar.

[English version](../10-reading-a-codebase.md)

## Por dónde empezar a mirar

Cuando descargues un nuevo repositorio, no intentes leer cada archivo. En su lugar, utiliza estos puntos de entrada:

- **Lee la documentación básica:**
  - **`README.md`:** explica qué hace realmente el proyecto, cómo está estructurado y cómo configurar y ejecutar la aplicación en tu equipo.
  - **`CONTRIBUTING.md`:** explica las reglas del proyecto para los colaboradores, incluidas las guías de estilo de código, cómo abrir pull requests y cómo esperan los mantenedores que envíes los cambios.
- **Encuentra y ejecuta las pruebas:**
  - **¿Qué son las pruebas?** Las pruebas son archivos de código independientes creados para comprobar automáticamente si la aplicación funciona de forma correcta, sin necesidad de hacer clics manuales en cada funcionalidad.
  - **¿Dónde están ubicadas?** Busca una carpeta específica `tests/` o `test/` en la raíz del proyecto, o revisa junto a los archivos fuente en busca de nombres de archivo como `auth.test.js` o `auth_spec.rb`.
  - **Cómo ejecutarlas:** consulta `README.md` o `CONTRIBUTING.md` para encontrar el comando exacto (como `npm test`, `pytest` o `cargo test`). Ejecutarlas te permite verificar que tu configuración funciona.
- **Busca el texto del error o la cadena de la interfaz que aparece en el issue:** si tu issue menciona un mensaje de error concreto o la etiqueta de un botón, utiliza la búsqueda global de tu editor (`Ctrl+Shift+F` o `Cmd+Shift+F`) para encontrar con exactitud en qué parte del código está definido ese texto.

## Arqueología con Git

Cuando encuentres el archivo que necesitas modificar, Git puede mostrarte su historial:

| Comando | Qué hace |
| --- | --- |
| `git log -p path/to/file` | Ver cada cambio que se ha hecho en el archivo y por qué |
| `git blame path/to/file` | Ver quién escribió cada línea y en qué commit |

## Seguir la ejecución y el historial

- **Sigue el flujo desde el punto de entrada:** identifica dónde comienza la ejecución (como `main()`, un manejador de rutas de API o el componente principal de la interfaz) y sigue las llamadas a funciones hacia el interior de la lógica.
- **Revisa pull requests fusionados recientemente:** busca en el repositorio PR cerrados que hayan modificado la misma zona del código. Te servirán como modelo para saber cómo esperan los mantenedores que se formateen y prueben los cambios.

## Lista de comprobación

- [ ] Leí `README.md` para entender qué hace el proyecto y cómo ejecutarlo.
- [ ] Leí `CONTRIBUTING.md` para conocer las reglas y las guías de estilo del proyecto.
- [ ] Encontré el conjunto de pruebas, lo ejecuté y comprobé que todas las pruebas pasan en local.
- [ ] Busqué el texto del error o la cadena de la interfaz del issue para localizar los archivos relevantes.
- [ ] Revisé pull requests fusionados recientemente o el historial de Git para obtener contexto sobre las convenciones.

Volver al [índice de la guía](README.md) · Encuentra tu próximo issue en el [índice de issues](../../issues/README.md).
