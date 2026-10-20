# 8. Revisiones, comentarios y rechazos

Abrir el pull request es la mitad del proceso, no el final. La forma en que gestiones la revisión decide si se fusiona o no.

[English version](../08-reviews.md)

## Cuando falla el CI

1. Abre la comprobación que ha fallado y lee el log desde el primer error, no desde la última línea.
2. Decide si el fallo lo causó tu cambio:
   - **Fallo de formato o de lint:** ejecuta el formateador o el linter en local y haz commit del resultado.
   - **Falla una prueba que tocaste:** corrígela en local y vuelve a hacer push.
   - **Falla una prueba no relacionada** que también falla en la rama por defecto, o un job que parece inestable (timeouts, errores de red): indícalo en un comentario con un enlace al mismo fallo en otro lugar. No intentes arreglar fallos no relacionados en tu PR a menos que te lo pidan.
3. Sube las correcciones como commits nuevos, salvo que el proyecto pida hacer squash.

Muchos proyectos exigen que un mantenedor apruebe las ejecuciones de CI de quienes contribuyen por primera vez. Si las comprobaciones dicen «awaiting approval», es normal: espera.

## Cuando recibes solicitudes de cambios

- **Lee todos los comentarios antes de responder.** Algunos dependen unos de otros.
- **Haz los cambios solicitados o explica por qué no.** Discrepar está bien si das una razón; ignorar un comentario, no.
- **Responde a cada comentario** con lo que hiciste («Hecho en abc123» o «Cambiado para usar el helper existente»). Deja que sea el revisor quien resuelva las conversaciones, salvo que el proyecto te pida lo contrario.
- **Haz push y vuelve a solicitar la revisión** con el botón del pull request, o deja un comentario breve avisando de que está listo otra vez.
- **Mantén el alcance.** Si un revisor pide algo mucho más grande, propón un issue de seguimiento en lugar de hacer crecer el pull request.

Los comentarios de la revisión tratan sobre el código, no sobre ti. Incluso quienes tienen experiencia reciben muchas rondas de comentarios en un proyecto nuevo.

## Revisores automáticos

Algunos proyectos usan bots que publican revisiones automáticas. Trata sus comentarios como sugerencias: corrige los problemas reales que encuentren y señala con educación cuando una sugerencia no aplique. La decisión final es de los mantenedores humanos.

## Cuando no pasa nada

El silencio es habitual y normalmente significa «ocupado», no «no».

- Pasadas una o dos semanas, un único recordatorio amable (capítulo 7).
- Comprueba si el proyecto tiene una cola de revisión o etiquetas como `waiting-on-review`.
- Mantén tu rama fusionable: resuelve los conflictos en cuanto aparezcan.
- Después de un mes o más, puedes preguntar si el cambio todavía les interesa. Si no, cerrarlo tú mismo es válido y se agradece.

## Cuando cierran tu pull request

Le pasa a todo el mundo. Los motivos más habituales:

| Motivo                                       | Qué hacer                                                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Alguien lo arregló antes                     | Cierra el tuyo, agradéceselo y, la próxima vez, elige los issues poco después de que se publiquen              |
| Los mantenedores quieren otro enfoque        | Pregunta si aceptarían una versión revisada, o déjales hacerlo a su manera                                     |
| Queda fuera del alcance del proyecto         | Acéptalo; pregunta si tendría sentido un plugin o un paquete aparte                                            |
| Baja calidad o poco claro                    | Lee los comentarios con atención; tu siguiente PR en ese proyecto tiene que ser claramente mejor               |
| Cerrado por automatización                   | Lee el mensaje del bot y el archivo del workflow; corrige lo que pide o contacta con los mantenedores          |
| Sin respuesta, cerrado por inactividad (stale) | Pregunta con educación si quieren reabrirlo; si no, sigue adelante                                           |

Un pull request cerrado, con una respuesta amable y constructiva, sigue dejando buena impresión.

## Después de la fusión

- Elimina tu rama (GitHub ofrece un botón).
- Actualiza la rama por defecto de tu fork: `git fetch upstream && git switch main && git rebase upstream/main && git push`.
- Anota lo que has aprendido sobre el proceso del proyecto. Tu segundo pull request ahí será mucho más rápido.

## Lista de comprobación

- [ ] Leí los logs del CI desde el primer error y separé mis fallos de los que ya existían.
- [ ] Respondí a cada comentario de la revisión y volví a solicitar la revisión.
- [ ] Mantuve pequeño el alcance del pull request.
- [ ] Hice seguimiento con educación, como máximo una vez por semana.

Siguiente: [Sigue adelante](09-keep-going.md)
