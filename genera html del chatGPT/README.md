# Preguntas y Respuestas con ChatGPT
Este programa permite realizar preguntas a ChatGPT y guardar las respuestas en archivos de texto y HTML.

## Configuración
Antes de ejecutar el programa, asegúrate de haber configurado la clave de la API de OpenAI en un archivo `.env` en el directorio raíz del proyecto. El archivo `.env` debe contener la siguiente variable:

- `OPENAI_API_KEY`: Clave de autenticación para la API de OpenAI.

## Uso
Una vez configurada la clave de la API, puedes ejecutar el programa. Este solicitará al usuario que introduzca una pregunta, y luego guardará la pregunta y la respuesta en un archivo de texto y en un archivo HTML con formato específico.

## Dependencias
El programa utiliza las siguientes bibliotecas de Python:

- `openai` para interactuar con la API de OpenAI.
- `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.

Asegúrate de instalar estas dependencias antes de ejecutar el programa.

```bash
pip install openai
pip install python-dotenv
```

## Idea
Surge a raíz de usar el chatGPT y pensar que sería una buena idea tener organizadas y a mano las preguntas y respuestas del chat simplemente con abrir un archivo .html  
Las preguntas están numeradas y se pincha sobre cada una para desplegar la respuesta