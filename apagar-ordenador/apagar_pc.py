
##
# Este programa presenta un menú con dos opciones; Hibernar o Apagar, una vez elegida la opción deseada, pregunta el tiempo en minutos pasado el cual queremos que ejecute la acción.
#

import os
import time
from datetime import datetime

def apagar(minutos):
    segundos = minutos * 60
    for i in range(segundos, 0, -1):
        print(f"El equipo se apagará en {i // 60} minutos y {i % 60} segundos.", end="\r")
        time.sleep(1)
    os.system("shutdown /s /f")

def hibernar(minutos):
    segundos = minutos * 60
    for i in range(segundos, 0, -1):
        print(f"El equipo se hibernará en {i // 60} minutos y {i % 60} segundos.", end="\r")
        time.sleep(1)
    os.system("shutdown /h /f")

    # Mostrar la hora actual
def mostrarHora():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nHora actual: {current_time}")

while True:
    print("\n1. Apagar el ordenador")
    print("2. Hibernar el ordenador")
    opcion = input("\nSelecciona una opción: ")
    if opcion == "1":
        minutos = int(input("\n¿En cuántos minutos deseas apagar el ordenador?: "))
        mostrarHora()
        apagar(minutos)
        break
    elif opcion == "2":
        minutos = int(input("\n¿En cuántos minutos deseas hibernar el ordenador?: "))
        mostrarHora()
        hibernar(minutos)
        break
    else:
        print("\nOpción inválida. Inténtalo de nuevo.")
        