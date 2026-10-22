# 3. Elige un proyecto

El proyecto importa más que el issue. Un proyecto activo y acogedor revisará tu pull request en cuestión de días. Uno inactivo o sobrecargado puede no revisarlo nunca, por muy bueno que sea.

## Empieza por lo que utilizas

El mejor primer proyecto es uno que ya utilizas: una biblioteca que utilizas en tu propio código, una herramienta que utilizas todos los días o una aplicación que te gusta. Entiendes cómo debería funcionar, puedes probar tu cambio de verdad y te importa el resultado.

Si no se te ocurre ninguno, explora el [índice de issues](../../issues/README.md) según el lenguaje que mejor conozcas y observa qué proyectos aparecen con frecuencia.

## Señales de un proyecto saludable y acogedor

Comprueba estos aspectos en la página del repositorio. Cinco minutos aquí pueden ahorrarte semanas de espera.

| Comprobación | Dónde buscar | Buena señal |
| --- | --- | --- |
| Actividad reciente | Pestaña de commits, fecha del "last commit" | Hay commits de las últimas semanas |
| Contribuciones externas fusionadas | **Pull requests → Closed**, filtra `is:merged` y revisa los autores | Se han fusionado pull requests de personas que no son mantenedores durante el último mes |
| Velocidad de las revisiones | Abre algunos PR fusionados recientemente de colaboradores externos | La primera respuesta llega en días, no en meses |
| Guía de contribución | `CONTRIBUTING.md` en la raíz, `.github/` o `docs/` | Existe y explica la configuración y las pruebas |
| Etiquetas para nuevos colaboradores | Issues, filtra por `good first issue` o `help wanted` | Se utilizan las etiquetas y los issues etiquetados reciben atención |
| Tono | Lee algunos hilos de issues | Los mantenedores son pacientes y específicos, incluso cuando dicen que no |
| Código de conducta | `CODE_OF_CONDUCT.md` | Existe |
| CI | Checks en los PR recientes | Las pruebas se ejecutan automáticamente en los pull requests |

Una búsqueda rápida que muestra PR fusionados de colaboradores externos para cualquier repositorio (reemplaza `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Observa los autores: si todos los PR fusionados son de las mismas dos personas, es posible que las contribuciones externas no sean una prioridad para ese proyecto.

## Señales de advertencia

- **Cientos de pull requests abiertos sin revisión.** El tuyo se unirá a la cola.
- **Una guía de contribución que indica que el proyecto no acepta pull requests**, o que solo los acepta para issues con una etiqueta específica. Algunos proyectos populares funcionan así. Respétalo.
- **Cada issue reciente ya tiene varios pull requests compitiendo.** Los proyectos populares suelen recibir PR de otras personas pocas horas después de que se publique un error. Aun así puedes contribuir, pero elige trabajos con menos competencia (documentación, pruebas o errores antiguos confirmados) o un proyecto más pequeño.
- **Los mantenedores piden a las personas que dejen de abrir pull requests de poco esfuerzo.** Lee esos hilos: te indican exactamente qué debes evitar.
- **No hay commits desde hace meses.** Es posible que el proyecto esté terminado o abandonado.

## ¿Proyecto grande o pequeño?

| | Proyecto grande y conocido | Proyecto más pequeño y activo |
| --- | --- | --- |
| Competencia por issues fáciles | Muy alta | Baja |
| Velocidad de revisión | Varía mucho; a menudo es lenta para colaboradores externos | A menudo es rápida y personalizada |
| Proceso | Formal: plantillas, CLAs, CI estricto | Más sencillo |
| Mentoría | A veces existen programas estructurados | Contacto directo con el mantenedor |
| Impacto en tu perfil | Fuerte reconocimiento del nombre | Fuerte si te conviertes en colaborador habitual |

Una buena estrategia es hacer tus primeras una o dos contribuciones en un proyecto más pequeño y activo donde puedas recibir comentarios rápidamente, y después llevar lo que hayas aprendido a proyectos más grandes.

## Lista de comprobación

- [ ] El proyecto ha tenido commits durante el último mes.
- [ ] Ha fusionado recientemente pull requests de colaboradores externos.
- [ ] Tiene una guía de contribución y la he leído.
- [ ] Puedo compilarlo y ejecutarlo en mi máquina (el capítulo 5 explica cómo hacerlo).

Siguiente: [Encuentra un issue que puedas completar](04-find-an-issue.md)
