# 6. Reglas que debes comprobar antes de empezar

Cada proyecto tiene reglas para las contribuciones. Algunas son simplemente convenciones; otras determinan si tu pull request puede fusionarse o incluso si se cerrará automáticamente. Compruébalas **antes** de escribir código.

[English version](../06-rules-before-you-start.md)

El [índice de issues](../../issues/README.md) muestra indicaciones detectadas automáticamente para cada proyecto. Son solo indicaciones, no garantías: lee siempre los archivos del propio proyecto.

| Nota en el índice  | Significado                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| ⚠️ AI restricted   | Los archivos de contribución del proyecto parecen prohibir o restringir considerablemente las contribuciones generadas por IA |
| 🤖 disclose AI use | El proyecto te pide que declares el uso de asistencia de IA                                                                   |
| 📄 AI policy       | El proyecto tiene una política sobre IA; léela                                                                                |
| ✍️ CLA             | Probablemente necesites firmar un Contributor License Agreement                                                               |
| 🔏 DCO             | Probablemente los commits necesiten una línea `Signed-off-by`                                                                 |

## Dónde están las reglas

Busca en todos estos lugares, no solo en el README:

* `CONTRIBUTING.md` (raíz, `.github/` o `docs/`)
* `.github/PULL_REQUEST_TEMPLATE.md` y las plantillas de issues
* `CODE_OF_CONDUCT.md`
* `AI_POLICY.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.claude/`, `.cursor/rules`
* `DEVELOPMENT.md`, `docs/development/` o una página de contribución en el sitio web del proyecto
* `.github/workflows/` (automatizaciones que etiquetan, comprueban o cierran pull requests)

## Contributor License Agreements (CLA)

Un CLA es un acuerdo legal que otorga al proyecto (o a la empresa que lo respalda) derechos para utilizar tu contribución. Muchos proyectos respaldados por empresas requieren uno.

* Normalmente, un bot comenta en tu primer pull request con un enlace. Lo firmas una vez, en línea, y cubre futuras contribuciones a ese proyecto u organización.
* Algunos CLA están vinculados a una cuenta de toda la organización, como EasyCLA de Linux Foundation (utilizado por muchos proyectos de CNCF) o el CLA de Google.
* **Lee lo que firmas.** Si contribuyes en nombre de un empleador, es posible que tu empleador tenga que firmar un CLA corporativo.

## Developer Certificate of Origin (DCO)

El DCO es una alternativa más sencilla a un CLA: certificas que tienes derecho a enviar el código. Lo haces añadiendo una línea de firma a cada commit:

```bash
git commit -s -m "fix: handle empty username"
# adds: Signed-off-by: Your Name <you@example.com>
```

Un bot de DCO comprueba cada commit del pull request. Si lo olvidaste, corrígelo con:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

El nombre y el correo electrónico de la firma deben coincidir con los del autor del commit.

## Contribuciones asistidas por IA

Los mantenedores han visto una avalancha de pull requests de baja calidad generados por IA, y muchos proyectos ahora tienen reglas explícitas. Estas varían bastante:

* **Permitidas con los estándares habituales.** Eres responsable de cada línea y debes poder explicarla.
* **Permitidas con declaración.** Debes indicar en la descripción del PR qué herramienta utilizaste y para qué, o añadir un indicador como `Assisted-by:` a los commits.
* **Comunicación escrita únicamente por humanos.** La IA puede ayudar con el código, pero los comentarios de los issues y las descripciones de los PR deben estar escritos por ti.
* **Restringidas o prohibidas.** Algunos proyectos no aceptan código o documentación generados por IA en absoluto, o no permiten que agentes de IA abran pull requests.

Independientemente de la política, estas reglas se aplican en todas partes:

* Debes entender y ser capaz de defender cada cambio que envíes.
* Nunca permitas que una herramienta abra pull requests o publique comentarios en tu nombre sin revisarlos tú mismo.
* Sigue exactamente las reglas de declaración cuando un proyecto las tenga. Ocultar el uso de IA cuando es obligatorio declararlo es una forma rápida de que te prohíban participar en un proyecto.

## Automatización contra el spam y para nuevos colaboradores

Debido al spam, algunos proyectos ejecutan workflows que cierran o etiquetan automáticamente los pull requests. Algunas reglas que se ven en proyectos reales incluyen:

* cerrar pull requests de cuentas que hayan abierto PR en muchos repositorios no relacionados en poco tiempo
* cerrar PR de autores cuyos pull requests hayan sido rechazados recientemente en otros lugares
* cerrar PR de ramas cuyos nombres estén relacionados con herramientas de IA (por ejemplo, `claude/...` o `codex/...`)
* exigir un issue vinculado o una etiqueta de issue como `help wanted` antes de aceptar un PR
* exigir una plantilla de PR completada con todas las casillas respondidas
* mantener el CI detenido hasta que un mantenedor lo apruebe para nuevos colaboradores (esto es normal e inofensivo)

Mira en `.github/workflows/` los archivos con nombres como `close-spam`, `first-interaction` o `pr-checks` para ver qué reglas se aplican. El consejo práctico: contribuye de forma constante a unos pocos proyectos en lugar de abrir pull requests en decenas de repositorios durante una sola semana.

## Declaraciones legales y licencias

Algunos proyectos te piden incluir una declaración en tu pull request, por ejemplo, que escribiste el código y que lo licencias bajo los términos del proyecto. Haz únicamente declaraciones que sean verdaderas. Al enviar una contribución, generalmente la licencias bajo la licencia del proyecto, así que comprueba que dicha licencia sea aceptable para ti (y para tu empleador, si corresponde).

## Lista de comprobación

* [ ] Leí la guía de contribución, la plantilla del PR y cualquier política de IA o instrucciones para agentes.
* [ ] Sé si necesito un CLA o una firma DCO.
* [ ] Conozco las convenciones del proyecto para los mensajes de commit y los títulos de los PR.
* [ ] Revisé `.github/workflows/` para detectar automatizaciones que podrían cerrar mi PR.
* [ ] Si la IA me ayudó, sé si debo declararlo y cómo hacerlo.

Siguiente: [Cómo comunicarte con los mantenedores](07-communication.md)
