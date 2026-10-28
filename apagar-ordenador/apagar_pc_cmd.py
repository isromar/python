
# Versión por línea de comandos del temporizador para apagar o hibernar el ordenador.
# A diferencia de apagar_pc.py, que es la versión de escritorio con una interfaz gráfica
# hecha con Tkinter, este programa se maneja desde la consola mediante un menú de texto.

# Permite ejecutar los comandos de apagado e hibernación de Windows.
import os
# Permite pausar la ejecución durante la cuenta atrás.
import time
# Se utiliza para mostrar la hora actual antes de iniciar la cuenta atrás.
from datetime import datetime


def apagar(minutos):
    # Convertimos los minutos indicados por el usuario a segundos.
    segundos = minutos * 60
    # Mostramos el tiempo restante y esperamos un segundo en cada iteración.
    for i in range(segundos, 0, -1):
        print(f"El equipo se apagará en {i // 60} minutos y {i % 60} segundos.", end="\r")
        time.sleep(1)
    # Al terminar la cuenta atrás, solicitamos a Windows que apague el equipo.
    os.system("shutdown /s /f")


def hibernar(minutos):
    # Convertimos los minutos indicados por el usuario a segundos.
    segundos = minutos * 60
    # Mostramos el tiempo restante y esperamos un segundo en cada iteración.
    for i in range(segundos, 0, -1):
        print(f"El equipo se hibernará en {i // 60} minutos y {i % 60} segundos.", end="\r")
        time.sleep(1)
    # Al terminar la cuenta atrás, solicitamos a Windows que hiberne el equipo.
    os.system("shutdown /h /f")


# Muestra la hora actual en la consola.
def mostrarHora():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nHora actual: {current_time}")


# Repetimos el menú hasta que se elija una de las opciones disponibles.
while True:
    print("\n1. Apagar el ordenador")
    print("2. Hibernar el ordenador")
    opcion = input("\nSelecciona una opción: ")
    if opcion == "1":
        # Pedimos el tiempo de espera, mostramos la hora e iniciamos el apagado.
        minutos = int(input("\n¿En cuántos minutos deseas apagar el ordenador?: "))
        mostrarHora()
        apagar(minutos)
        break
    elif opcion == "2":
        # Pedimos el tiempo de espera, mostramos la hora e iniciamos la hibernación.
        minutos = int(input("\n¿En cuántos minutos deseas hibernar el ordenador?: "))
        mostrarHora()
        hibernar(minutos)
        break
    else:
        # Si la opción no es válida, mostramos un aviso y volvemos a presentar el menú.
        print("\nOpción inválida. Inténtalo de nuevo.")
