# 7. Cómo comunicarte con los mantenedores

Los mantenedores suelen ser voluntarios o ingenieros ocupados que revisan contribuciones además de realizar su propio trabajo. Una comunicación clara, breve y concreta te ayudará a recibir respuestas más rápidas y amables.

## Reclamar un issue

Algunos proyectos quieren que dejes un comentario antes de empezar; otros dicen que simplemente abras un PR. Consulta la guía de contribución del proyecto. Si decides comentar, procura que tu mensaje sea útil:

> Puedo reproducir este problema en la versión 4.2.1: `tool --flag ""` entra en un bucle infinito en lugar de mostrar un error. La comprobación en `src/prompt.ts` rechaza la entrada vacía sin explicar el motivo. Mi plan es mostrar el mensaje de validación y volver a solicitar la entrada, añadiendo una prueba en `prompt.test.ts`. ¿Puedo continuar?

Esto es mejor que preguntar «¿Puedo trabajar en esto?», porque demuestra que has entendido el problema y permite que el mantenedor corrija tu enfoque antes de que dediques tiempo al trabajo.

No reclames varios issues a la vez ni reclames uno en el que no vayas a empezar a trabajar esta semana.

## Pedir ayuda

Cuando te quedes atascado, pregunta en el issue o en el chat del proyecto, si lo tiene. Incluye lo siguiente:

- Qué intentas hacer.
- Qué has probado.
- Qué ha ocurrido, con el mensaje de error o la salida exactos.
- Tu entorno, cuando sea relevante (sistema operativo, versión del lenguaje y versión del proyecto).

Enlaza la línea de código sobre la que tienes dudas. Mientras esperas una respuesta, sigue investigando; si encuentras la solución, compártela.

## Redactar la descripción de un pull request

Los revisores leen muchos pull requests. Haz que el tuyo sea fácil de entender en 30 segundos.

**Buen ejemplo:**

> Corrige #1234.
>
> `login` volvía a solicitar el nombre de usuario indefinidamente cuando estaba vacío, porque `validateUsername` devolvía un error que el bucle de solicitud ignoraba. Ahora el bucle muestra el mensaje de validación antes de volver a preguntar.
>
> Añadí una prueba en `prompt.test.ts` que falla sin este cambio. `npm test` y `npm run lint` se ejecutan correctamente en mi entorno local.

**Por qué funciona:** enlaza el issue, explica qué estaba mal y por qué, indica qué ha cambiado y señala cómo se ha verificado. Sin relleno innecesario.

Evita lo siguiente:

- Resúmenes largos generados automáticamente, listas con todos los archivos modificados o encabezados para un cambio de diez líneas.
- Lenguaje publicitario («Este PR mejora significativamente...»).
- Afirmaciones que no hayas verificado («corrige todos los problemas relacionados»).
- Dejar el texto de ejemplo del modelo de PR sin sustituir.

Si hay algo que los revisores deban saber, dilo directamente: «No estaba seguro de si se debían permitir nombres de usuario vacíos en registros personalizados, así que mantuve el comportamiento existente en ese caso».

## Tono

- Sé amable y presupón buenas intenciones, incluso cuando alguien te responda de forma seca.
- Agradece una vez a los revisores el tiempo que dedican. No hace falta darles las gracias por cada comentario.
- No menciones repetidamente a los mantenedores con `@` ni etiquetes a personas que no estén involucradas.
- Mantén las conversaciones en el issue o el pull request, no en mensajes privados, a menos que te inviten a hacerlo.
- Escribe con tus propias palabras. Los mantenedores quieren saber que una persona entiende el cambio.

## Hacer seguimiento

Si no recibes respuesta después de aproximadamente una semana, está bien enviar un único recordatorio educado:

> Un pequeño recordatorio: esto está listo para revisión cuando alguien tenga tiempo. Estoy disponible para hacer cambios.

Si el proyecto tiene un canal de chat para colaboradores, también puedes preguntar allí una vez. Después, espera: algunos proyectos simplemente avanzan despacio.

## Lista de comprobación

- [ ] Mi comentario para reclamar el issue (si era necesario) demuestra que entendí el problema.
- [ ] La descripción de mi PR explica qué estaba mal, qué cambió, cómo lo probé y enlaza el issue.
- [ ] He eliminado el texto de ejemplo de la plantilla.
- [ ] Mis recordatorios son educados y están suficientemente espaciados.

Siguiente: [Revisiones, comentarios y rechazos](08-reviews.md)
