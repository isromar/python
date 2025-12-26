# Genera números a elegir si aleatorios o no
import random

def generar_numeros():
    inicio = int(input("¿Desde qué número quieres empezar? "))
    cantidad = int(input("¿Cuántos números quieres generar? "))
    aleatorio = input("¿Quieres que los números sean aleatorios? (s/n) ").lower() == "s"
    digitos = 8

    numeros = []

    if aleatorio:
        for _ in range(cantidad):
            numeros.append(str(random.randint(inicio, 10**digitos - 1)).zfill(digitos))
    else:
        for i in range(inicio, inicio + cantidad):
            numeros.append(str(i).zfill(digitos))

    with open("numeros.txt", "w") as archivo:
        archivo.write("\n".join(numeros))

# Ejemplo de uso
generar_numeros()

