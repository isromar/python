# Este programa implementa un bot de Telegram que utiliza la API de OpenAI para generar respuestas a mensajes de texto.

# Importa la librería para cargar variables de entorno desde el archivo .env
from dotenv import load_dotenv
# Importa la librería para trabajar con la API de Telegram
import telebot
# Importa la librería de OpenAI
import openai
# Importa la librería para interactuar con el sistema operativo
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a las variables de entorno cargadas
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAPI_KEY = os.getenv('OPENAPI_KEY')

# Configuración de la API de OpenAI
openai.api_key = OPENAPI_KEY
model_engine = "gpt-3.5-turbo-16k-0613"  # Motor predeterminado válido hasta 2024-06-13
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Función para generar una respuesta a partir de un mensaje de texto usando OpenAI
def generate_response(text):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=text,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.6,
    )
    respuesta = response.choices[0].text.strip()
    return respuesta

# Comprueba el texto escrito en Telegram que empieza por / si está en la lista de comandos
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, 'Hola, soy el bot')

# Controla el texto escrito en Telegram
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    responde = generate_response(message.text)  # Llama a la función de OpenAI y le envía el texto
    if message.text.startswith("."):    # He puesto que haya que escribir un punto antes de la frase, por ejemplo .Hola
        bot.send_message(message.chat.id, responde)
    else:
        bot.send_message(message.chat.id, "Bot en pruebas")

if __name__ == "__main__":
    print('Bot iniciado')
    bot.infinity_polling()
