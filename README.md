# Python: ideas que se convierten en herramientas

Este repositorio reúne proyectos y experimentos desarrollados en Python para resolver problemas concretos, automatizar tareas y aprender creando. Cada proyecto vive en su propia carpeta y puede tener sus propios requisitos, instrucciones y forma de ejecución.

La idea no es construir una única aplicación enorme, sino partir de una necesidad —a veces pequeña y cotidiana—, pensar una solución práctica y desarrollarla paso a paso hasta convertirla en una herramienta que se pueda utilizar.

## Del problema a la solución

Algunos ejemplos de ese enfoque:

| Necesidad | Solución desarrollada |
|---|---|
| Calcular rápidamente las dimensiones recomendadas para una imagen | Una herramienta que calcula la altura a partir de la orientación y el ancho. |
| Reducir una imagen manteniendo sus proporciones | Una calculadora de resolución que obtiene las nuevas dimensiones a partir de un porcentaje. |
| Escuchar un texto en lugar de leerlo en pantalla | Un conversor de texto a audio MP3 con selección de idioma. |
| Programar el apagado o la hibernación del ordenador | Una aplicación de escritorio con cuenta atrás visual y opción para cancelar. |
| Resolver cálculos repetitivos o explorar conceptos de programación | Scripts y ejercicios independientes, desde sistemas de ecuaciones hasta problemas de Project Euler. |

Cada proyecto es también una oportunidad para probar distintas formas de resolver una necesidad: scripts de consola, interfaces gráficas, automatizaciones, integración con servicios y pequeños experimentos.

## Explora los proyectos

### Herramientas y utilidades

- [Calcular tamaños para Instagram](./calcular-instagram/): calcular dimensiones de imagen según su orientación.
- [Calcular resolución](./calcular-resolucion/): reducir las dimensiones de una imagen mediante un porcentaje.
- [Temporizador para apagar el ordenador](./apagar-ordenador/): programar el apagado o la hibernación desde una interfaz gráfica.
- [Convertir texto a MP3](./generar-mp3-desde-txt/): generar audio a partir de archivos de texto.

### Bots, APIs e integración

- [Bot de Telegram](./telegram%20bot/): conectar Telegram con un servicio de generación de respuestas.

### Aprendizaje y experimentación

- [Project Euler](./project-euler/): soluciones a problemas de programación y matemáticas, organizadas por ejercicio.
- [Resolver sistemas de ecuaciones](./resolver-ecuaciones-multiples-incognitas/): aplicación de Python y NumPy a un problema matemático.

> El contenido y el nivel de documentación varían entre proyectos. Consulta el README de cada carpeta para conocer sus instrucciones y requisitos específicos.

## Cómo empezar

1. Clona el repositorio:

   ```bash
   git clone https://github.com/isromar/Python.git
   ```

2. Entra en la carpeta del proyecto que te interese.
3. Lee su README para identificar los requisitos y el comando de ejecución.
4. Instala solo las dependencias necesarias para ese proyecto y ejecútalo con Python.

No hay un único comando de instalación para todo el repositorio: algunos scripts usan únicamente la biblioteca estándar y otros requieren paquetes o servicios externos.

## Tecnologías y enfoques

Según el proyecto, aquí encontrarás:

- Python para scripts, automatización y herramientas independientes.
- Tkinter para interfaces gráficas de escritorio.
- NumPy para cálculos y sistemas de ecuaciones.
- Integración con APIs y bots de Telegram.
- Conversión de texto a voz y trabajo con archivos multimedia.
- Ejercicios de programación y experimentación con distintas ideas.

## Filosofía

Una herramienta útil no tiene que empezar siendo compleja. Puede empezar con una pregunta sencilla: **¿qué tarea me gustaría hacer más fácil?** A partir de ahí, se puede definir el problema, probar una solución pequeña, observar qué falta y mejorarla de forma incremental.

Este repositorio documenta precisamente ese recorrido: ideas convertidas en proyectos, soluciones prácticas y aprendizaje a través de la programación.
