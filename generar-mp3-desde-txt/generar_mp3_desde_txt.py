# Script de Python que utiliza la librería gTTS (Google Text-to-Speech) para convertir un archivo de texto en un archivo de audio en formato MP3, al final pregunta si quieres reproducirlo.
# Para instalar la librería gTTS en tu entorno de Python, para convertir texto a voz.
# pip install gtts
# 
# @Author Isabel Rodenas Marin
#

from gtts import gTTS  # Importa la clase gTTS desde la librería gtts
import os  # Importa el módulo os para interactuar con el sistema operativo

print("*** C O N V E R T I D O R  D E  T X T  A  M P 3 ***")
print("1.Escribe el nombre de un archivo de texto existente en el mismo directorio que está el programa\n2.Selecciona el idioma en que está escrito el texto, por defecto inglés\n3.Espera hasta que el archivo esté generado\n4.Finalmente responde si quieres que se reproduzca ahora")

# Pregunta por el archivo para leer sin la extensión
nombre_archivo = input("\nIngrese el nombre del archivo de texto sin extensión .txt: ").lower()  # Solicita al usuario el nombre del archivo y lo convierte a minúsculas
nombre_archivo_con_extension = nombre_archivo + ".txt"  # Agrega la extensión .txt al nombre del archivo
idioma_texto = input("\n¿En qué idioma está el texto?(es/en) (Por defecto 'en'): ")  # Solicita al usuario el idioma del texto
print("Espera...")  # Imprime un mensaje indicando que se debe esperar

if idioma_texto == 'es':  # Verifica si el idioma es español
    idioma_texto = 'es'  # Establece el idioma a español
else:  # Si no es español
    idioma_texto = 'en'  # Establece el idioma a inglés

with open(nombre_archivo_con_extension, "r", encoding="utf-8", errors='ignore') as archivo:  # Abre el archivo de texto
    texto = archivo.read()  # Lee el contenido del archivo

tts = gTTS(text=texto, lang=idioma_texto)  # Crea un objeto gTTS con el texto y el idioma especificados
tts.save(nombre_archivo +".mp3")  # Guarda el archivo de audio en formato MP3

print("\nArchivo guardado: "+ nombre_archivo + ".mp3")  # Imprime un mensaje indicando que el archivo se ha guardado con éxito

quieres_reproducir = input('\n¿Reproducir el archivo (s/n)?:')  # Pregunta al usuario si desea reproducir el archivo

if quieres_reproducir == 's':  # Si el usuario desea reproducir el archivo
    os.system(nombre_archivo +".mp3")  # Reproduce el archivo de audio
else:  # Si no desea reproducirlo
    print('\nArchivo guardado')  # Imprime un mensaje indicando que el archivo se ha guardado
