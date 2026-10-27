import os
import telebot
import openai
from dotenv import load_dotenv

# 1. Cargar el archivo .env
load_dotenv()

# 2. Leer las variables (asegúrate que en el .env se llamen igual)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

# 3. Configurar la conexión a OpenRouter
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = OPENROUTER_KEY

# 4. Elegir el modelo (el que es gratis)
model_engine = "google/gemma-3-12b-it:free"

# 5. Inicializar el Bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)


def generate_response(text):
    # Añadimos un espacio y quizás un punto para separar la pregunta de la orden
    prompt_final = (
        f"{text}. Responde breve y lo más objetivo posible, sin omitir lo más relevante."
    )

    try:
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[{"role": "user", "content": prompt_final}],
            # Te recomiendo dejar el max_tokens activo por seguridad
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Imprime el error en tu consola para saber qué pasó si falla
        print(f"Error en API: {e}")
        return "Error al conectar con la IA."


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Hola, soy el bot conectado a OpenRouter.")


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # Limpiamos el texto inicial
    texto_usuario = message.text.strip()

    if texto_usuario.startswith("."):
        # Feedback inmediato al usuario
        sent_msg = bot.send_message(message.chat.id, "Pensando...")

        # Limpiamos el punto y los espacios después del punto (.  hola -> hola)
        pregunta_final = texto_usuario[1:].strip()

        # Si el usuario solo puso un punto sin texto, avisamos
        if not pregunta_final:
            bot.edit_message_text(
                "¡Dime algo después del punto! Ejemplo: .Hola",
                message.chat.id,
                sent_msg.message_id,
            )
            return

        # 4. Llamada a la IA
        responde = generate_response(pregunta_final)

        # 5. Editamos el "Pensando..." con la respuesta final
        bot.edit_message_text(responde, message.chat.id, sent_msg.message_id)
    else:
        # Mensaje por defecto si no hay punto
        bot.send_message(message.chat.id, "Bot en pruebas.")


if __name__ == "__main__":
    print("Bot iniciado con OpenRouter Gratis")
    bot.infinity_polling()
