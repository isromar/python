import random
import string

def generar_contrasenas():
    num_mayusculas = int(input("¿Cuántas mayúsculas quieres? "))
    num_minusculas = int(input("¿Cuántas minúsculas quieres? "))
    num_simbolos = int(input("¿Cuántos símbolos quieres? "))
    num_numeros = int(input("¿Cuántos números quieres? "))
    cantidad = int(input("¿Cuántas contraseñas quieres generar? "))

    contrasenas = []

    for _ in range(cantidad):
        caracteres = []

        for _ in range(num_mayusculas):
            caracteres.append(random.choice(string.ascii_uppercase))

        for _ in range(num_minusculas):
            caracteres.append(random.choice(string.ascii_lowercase))

        for _ in range(num_simbolos):
            caracteres.append(random.choice(string.punctuation))

        for _ in range(num_numeros):
            caracteres.append(random.choice(string.digits))

        random.shuffle(caracteres)

        contrasena = "".join(caracteres)
        contrasenas.append(contrasena)

    return contrasenas

def guardar_contrasenas(contrasenas, archivo):
    with open(archivo, "w") as file:
        for contrasena in contrasenas:
            file.write(contrasena + "\n")

# Ejemplo de uso
contrasenas_generadas = generar_contrasenas()
archivo = "password.txt"
guardar_contrasenas(contrasenas_generadas, archivo)
print("Archivo generado: " + archivo)
