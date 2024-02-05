# Se hacen preguntas a Chatgpt y las respuestas las guarda en txt y html
import openai
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Motores de búsqueda de más costoso a menos
engineDavinci = "text-davinci-003"
engineBabbage = "text-babbage-001"
engineCurie = "text-curie-001"
engineAda = "text-ada-001"
engineCodeCushman = "code-cushman-001"
engineCodeDavinci = "code-davinci-002"

# Motor de búsqueda seleccionado
engineSelected = engineDavinci
filenameHtml = "Preguntas chatGPT.html"

max_tokens_selected = 500

# Accede a la clave de la API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Solicita al usuario que introduzca una pregunta
text = input("\nIntroduce una pregunta: ")
text = text[0:220]
filename = text + ".txt"  # Acorta la longitud del nombre del archivo

# Utiliza la API de OpenAI para obtener una respuesta basada en la pregunta ingresada
completion = openai.Completion.create(engine=engineSelected,
                                      prompt=text,
                                      temperature=0.6,
                                      max_tokens=max_tokens_selected)

respuesta = completion.choices[0].text
respuestaTxt = respuesta.replace(". ", ".\n")
print(respuesta)

# Escribe la pregunta y la respuesta en un archivo de texto
with open(filename, "a", encoding="UTF-8", errors='ignore') as file:
    file.write("##"+text + "\n",)
    file.write(respuestaTxt + "\n")

# Escribe la pregunta y la respuesta en un archivo HTML con formato específico
with open(filenameHtml, "a", encoding="UTF-8", errors='ignore') as file:
    file.write("\n<li class=\"preguntas\"><details><summary>\n<h4><div class=\"pregunta\">" +
               text + "</div></h4></summary>\n")
    file.write("<p><div class=\"respuesta\">" + respuesta + "</div></p></details></li>\n")

# Informa al usuario que el texto se ha escrito correctamente en el archivo
print("\nEl texto se ha escrito correctamente en el archivo '"+filename+"'")
