# Bot de Telegram con OpenAI
Este programa implementa un bot de Telegram que utiliza la API de OpenAI para generar respuestas a mensajes de texto.

## Configuración
Antes de ejecutar el bot, asegúrate de haber configurado las siguientes variables de entorno en un archivo `.env` en el directorio raíz del proyecto:

- `TELEGRAM_TOKEN`: Token de autenticación del bot de Telegram.
- `OPENAPI_KEY`: Clave de autenticación para la API de OpenAI.

## Uso
Para crear el bot de Telegram, se puede utilizar el servicio ofrecido por BotFather (https://botfather.io/) que no está explicado en reste README  
Una vez creado el bot, puedes ejecutar este programa bot_telegram.py y dejarlo corriendo.  
El bot de Telegram responderá a los mensajes de texto con respuestas generadas por OpenAI. 

## Dependencias
El programa utiliza las siguientes bibliotecas de Python:

- `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.
- `telebot` para interactuar con la API de Telegram.
- `openai` para utilizar la API de OpenAI.

Asegúrate de instalar estas dependencias antes de ejecutar el programa.

```bash
pip install python-dotenv
pip install pyTelegramBotAPI
pip install openai==0.28
```

Antes usaba
pip install openai
pero ahora hay que poner esa versión concreta

## Idea
Este script surge porque prefería tener la comodidad de accceder al chat a través de Telegram como una conversación, sin tener que acceder al chat de la web a través del navegador