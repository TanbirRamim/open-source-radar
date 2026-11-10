<a id="newcomer-faq"></a>
# Preguntas frecuentes para principiantes

Respuestas breves a las dudas más comunes antes y después del primer pull request. Cada respuesta enlaza al capítulo que explica el tema en detalle.

<a id="before-you-start"></a>
## Antes de empezar

<a id="do-i-need-to-ask-before-working-on-an-issue"></a>
### ¿Tengo que preguntar antes de trabajar en un issue?

Depende del proyecto. Consulta `CONTRIBUTING.md`: algunos proyectos piden un comentario previo, otros asignan issues con el comando `/claim` o `/assign`, y otros dicen que abras un PR directamente. Si la guía no dice nada y el issue es pequeño, normalmente puedes abrir un pull request sin preguntar. Para algo más grande, comenta primero para que nadie pierda el tiempo. Consulta el [capítulo 7](07-communication.md#reclamar-un-issue) (en inglés).

<a id="how-do-i-claim-an-issue-without-sounding-like-everyone-else"></a>
### ¿Cómo reclamo un issue sin decir lo mismo que todo el mundo?

En lugar de limitarte a preguntar «¿Puedo trabajar en esto?», explica en dos o tres frases qué has encontrado y qué planeas cambiar. Así, un mantenedor puede darte el visto bueno o sugerirte una mejor solución antes de que escribas código. Hay un ejemplo en el [capítulo 7](07-communication.md#reclamar-un-issue) (en inglés).

<a id="someone-commented-ill-take-this-weeks-ago-and-never-opened-a-pr-can-i-take-it"></a>
### Alguien dijo «yo me encargo» hace semanas y nunca abrió un PR. ¿Puedo hacerlo yo?

Pregunta primero en el issue: «¿Sigues trabajando en esto? Si no, me gustaría encargarme». Si pasan unos días sin respuesta, pide a un mantenedor que lo reasigne. No abras un pull request que compita con el suyo sin preguntar. Consulta el [capítulo 4](04-find-an-issue.md#alguien-ya-está-trabajando-en-ello) (en inglés).

<a id="how-many-issues-should-i-claim-at-once"></a>
### ¿Cuántos issues debería reclamar a la vez?

Uno. Reclama el siguiente después de abrir tu primer pull request.

<a id="im-not-sure-i-can-finish-it-should-i-still-try"></a>
### No sé si podré terminarlo. ¿Debería intentarlo de todos modos?

Sí, pero elige algo cuyo alcance puedas calcular. Si puedes reproducir el problema y encontrar el código relacionado en una hora, probablemente sea una buena opción. Si te atascas, puedes decirlo en el issue y quitarte la asignación. Consulta el [capítulo 4](04-find-an-issue.md#puedes-completarlo) (en inglés).

<a id="rules-and-paperwork"></a>
## Reglas y trámites

<a id="a-bot-asked-me-to-sign-a-cla-is-that-normal"></a>
### Un bot me pidió que firmara un CLA. ¿Es normal?

Sí. Un Contributor License Agreement concede al proyecto derechos para usar tu cambio. Lo firmas una vez por internet y cubre contribuciones posteriores. Léelo y, si contribuyes para una empresa, comprueba si también tiene que firmarlo. Consulta el [capítulo 6](06-rules-before-you-start.md#contributor-license-agreements-cla).

<a id="the-dco-check-failed-how-do-i-fix-it"></a>
### Falló la comprobación del DCO. ¿Cómo lo soluciono?

Cada commit necesita una línea `Signed-off-by:` que coincida con su autor. Añádela a todos los commits de tu rama y vuelve a hacer push:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

De ahí en adelante, usa `git commit -s`. Consulta el [capítulo 6](06-rules-before-you-start.md#developer-certificate-of-origin-dco).

<a id="can-i-use-ai-tools"></a>
### ¿Puedo usar herramientas de IA?

Consulta la política del proyecto antes de empezar. Algunos prohíben las contribuciones generadas con IA, otros piden que declares su uso y muchos no dicen nada. Sea cual sea la regla, eres responsable de cada línea: debes entenderla, probarla y poder explicarla durante la revisión. Consulta el [capítulo 6](06-rules-before-you-start.md#contribuciones-asistidas-por-ia) (en inglés).

<a id="a-bot-closed-my-pr-or-labeled-it-as-spam-what-now"></a>
### Un bot cerró mi PR o lo marcó como spam. ¿Qué hago?

Lee el mensaje del bot. Muchos proyectos cierran los pull requests de quienes contribuyen por primera vez si no están vinculados a un issue o no siguen la plantilla. Corrige lo que indique o responde con educación y pide a un mantenedor que lo revise. Consulta el [capítulo 6](06-rules-before-you-start.md#automatización-contra-el-spam-y-para-nuevos-colaboradores) (en inglés).

<a id="after-you-open-the-pull-request"></a>
## Después de abrir el pull request

<a id="nobody-has-replied-how-long-should-i-wait"></a>
### Nadie ha respondido. ¿Cuánto debería esperar?

Es normal esperar una o dos semanas. Después, deja un comentario breve y educado para preguntar si necesitan algo de tu parte. Mientras esperas, mantén la rama libre de conflictos. Pasado un mes, pregunta si el cambio sigue siendo de interés. Consulta el [capítulo 8](08-reviews.md#cuando-no-pasa-nada) (en inglés).

<a id="ci-is-red-and-i-dont-understand-why"></a>
### El CI está en rojo y no entiendo por qué.

Abre la tarea que falló y busca el primer error, no el último. Ejecuta el mismo comando localmente. Si el fallo está en código que no has tocado, indícalo en el pull request; podría tratarse de una prueba intermitente o de un problema en la rama principal. Consulta el [capítulo 8](08-reviews.md#cuando-falla-el-ci) (en inglés).

<a id="the-maintainer-asked-for-changes-do-i-open-a-new-pr"></a>
### El mantenedor pidió cambios. ¿Abro otro PR?

No. Haz push de nuevos commits a la misma rama y el pull request se actualizará. Responde a cada comentario para que la persona que revisa sepa que ya lo atendiste. Consulta el [capítulo 8](08-reviews.md#cuando-recibes-solicitudes-de-cambios) (en inglés).

<a id="my-pr-has-merge-conflicts"></a>
### Mi PR tiene conflictos de merge.

Actualiza tu rama con la rama principal del proyecto, resuelve los conflictos y haz push:

```bash
git fetch upstream
git rebase upstream/main
# fix the files, then: git add <file> && git rebase --continue
git push --force-with-lease
```

Consulta el [capítulo 5](05-first-pull-request.md).

<a id="my-pr-was-closed-without-merging-did-i-do-something-wrong"></a>
### Cerraron mi PR sin fusionarlo. ¿Hice algo mal?

No siempre. Puede que alguien lo haya solucionado antes o que el proyecto prefiera otra solución. Lee el motivo, da las gracias y pregunta si una versión revisada sería útil. Consulta el [capítulo 8](08-reviews.md#cuando-cierran-tu-pull-request) (en inglés).

<a id="after-the-merge"></a>
## Después de la fusión

<a id="does-a-merged-pr-in-a-small-project-count"></a>
### ¿Cuenta un PR fusionado en un proyecto pequeño?

Sí. Un pull request fusionado es trabajo real hecho en público, sin importar el tamaño del proyecto. Unos pocos cambios fusionados en un proyecto que te interesa valen más que muchas correcciones de una línea repartidas entre repositorios. Consulta el [capítulo 9](09-keep-going.md).

<a id="what-should-i-do-next"></a>
### ¿Qué hago después?

Sigue en el mismo proyecto. Ya sabes cómo compilarlo y cómo revisan los mantenedores. Elige un issue un poco más grande, ayuda a clasificar los nuevos o revisa el pull request de otra persona. Consulta el [capítulo 9](09-keep-going.md).
