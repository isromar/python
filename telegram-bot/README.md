# Bot de Telegram con OpenRouter

Este proyecto conecta un bot de Telegram con un modelo de lenguaje servido por OpenRouter. Para consultar el modelo, envía un mensaje que empiece por un punto; por ejemplo: `.¿Qué es Python?`.

## Requisitos

- Python 3.
- Una cuenta de Telegram y un bot creado con [BotFather](https://t.me/BotFather).
- Una clave de API de [OpenRouter](https://openrouter.ai/).

## Instalación

Desde esta carpeta, instala las dependencias de Python:

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en esta carpeta con las credenciales del bot y de OpenRouter:

```env
TELEGRAM_BOT_TOKEN=token_del_bot
OPENROUTER_API_KEY=clave_de_openrouter
```

No compartas ni subas este archivo: contiene credenciales privadas.

## Ejecución

Inicia el bot desde esta carpeta:

```bash
python bot_telegram.py
```

En Telegram, envía `/start` para comprobar que el bot responde. Para consultar el modelo, empieza el mensaje con un punto, por ejemplo:

```text
.Resume qué es una API en una frase
```

Los mensajes sin punto reciben una respuesta indicando que el bot está en pruebas. El código utiliza actualmente el modelo gratuito `google/gemma-3-12b-it:free` de OpenRouter.

## Vista previa

![Vista previa del bot](https://raw.githubusercontent.com/isromar/Python/main/telegram-bot/preview.JPG)