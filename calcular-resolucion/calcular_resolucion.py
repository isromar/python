import re

def calcular_resolucion(reduccion=0.75):
    entrada = input("Introduce la resolución original (ejemplo: 1920x1080) [Enter para usar 1920x1080]: ").strip().lower()

    if not entrada:
        entrada = "1920x1080"

    try:
        # Expresión regular para separar por "x" o "*"
        ancho_str, alto_str = re.split(r'[x*]', entrada)
        ancho = int(ancho_str)
        alto = int(alto_str)

        nuevo_ancho = int(ancho * reduccion)
        nuevo_alto = int(alto * reduccion)

        print(f"Resolución reducida al {int(reduccion*100)}%: {nuevo_ancho}x{nuevo_alto}")

    except ValueError:
        print("Formato inválido. Asegúrate de escribir la resolución como '1920x1080'.")

if __name__ == "__main__":
    calcular_resolucion()
