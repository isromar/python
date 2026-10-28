import re  # Importa el módulo para trabajar con expresiones regulares


def calcular_resolucion(reduccion=0.75):
    # Pide al usuario la resolución original, elimina espacios sobrantes y convierte a minúsculas
    entrada = (
        input(
            "Introduce la resolución original (ejemplo: 1920x1080) [Enter para usar 1920x1080]: "
        )
        .strip()
        .lower()
    )

    # Si el usuario presionó Enter sin escribir nada, se asigna la resolución predeterminada
    if not entrada:
        entrada = "1920x1080"

    try:
        # Separa el texto usando "x" o "*" como delimitador para obtener ancho y alto como cadenas
        ancho_str, alto_str = re.split(r"[x*]", entrada)
        ancho = int(ancho_str)
        alto = int(alto_str)

        # Calcula el nuevo ancho y alto multiplicando por el factor de reducción y convirtiendo a entero
        nuevo_ancho = int(ancho * reduccion)
        nuevo_alto = int(alto * reduccion)

        # Imprime la resolución reducida mostrando el porcentaje aplicado
        print(
            f"Resolución reducida al {int(reduccion*100)}%: {nuevo_ancho}x{nuevo_alto}"
        )

    except ValueError:
        # Se ejecuta si los valores no se pueden convertir a número o el formato es incorrecto
        print("Formato inválido. Asegúrate de escribir la resolución como '1920x1080'.")


if __name__ == "__main__":
    # Llama a la función principal solo cuando el script se ejecuta directamente
    calcular_resolucion()
