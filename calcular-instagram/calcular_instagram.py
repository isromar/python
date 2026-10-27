def calcular_tamano_instagram():
    # Función que calcula el tamaño mínimo de una imagen para Instagram según su orientación

    # Obtener la orientación de la imagen
    # Si el usuario no ingresa nada o no es vertical/v, se asume horizontal
    orientacion = input("¿La imagen es vertical u horizontal v/h? [Enter para horizontal]: ").strip().lower()
    if orientacion not in ["vertical", "v"]:
        orientacion = "horizontal"

    # Obtener el ancho de la imagen
    # Si el usuario no ingresa un valor numérico, se usa el valor por defecto (2500)
    entrada_ancho = input("Introduce el ancho de la imagen (por defecto 2500): ").strip()
    ancho = int(entrada_ancho) if entrada_ancho.isdigit() else 2500

    # Calcular la altura según la orientación
    if orientacion == "horizontal":
        # Relación de aspecto para imágenes horizontales: ancho / alto = 1.91
        relacion = 1.91
        alto = int(ancho / relacion)
        print(f"Relación horizontal 1.91:1. Para ancho {ancho}, la altura mínima es {alto}.")
    else:
        # Relación de aspecto para imágenes verticales: ancho / alto = 4/5 (equivalente a alto = ancho * 1.25)
        relacion = 4 / 5
        alto = int(ancho / relacion)
        print(f"Relación vertical 4:5. Para ancho {ancho}, la altura mínima es {alto}.")

if __name__ == "__main__":
    calcular_tamano_instagram()
