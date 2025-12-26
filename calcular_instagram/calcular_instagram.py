def calcular_tamano_instagram():
    orientacion = input("¿La imagen es vertical u horizontal v/h? [Enter para horizontal]: ").strip().lower()
    if orientacion not in ["vertical", "v"]:
        orientacion = "horizontal"

    entrada_ancho = input("Introduce el ancho de la imagen (por defecto 2500): ").strip()
    ancho = int(entrada_ancho) if entrada_ancho.isdigit() else 2500

    if orientacion == "horizontal":
        relacion = 1.91  # ancho / alto
        alto = int(ancho / relacion)
        print(f"Relación horizontal 1.91:1. Para ancho {ancho}, la altura mínima es {alto}.")
    else:
        relacion = 4 / 5  # ancho / alto → alto = ancho / (4/5) = ancho * 1.25
        alto = int(ancho / relacion)
        print(f"Relación vertical 4:5. Para ancho {ancho}, la altura mínima es {alto}.")

if __name__ == "__main__":
    calcular_tamano_instagram()
