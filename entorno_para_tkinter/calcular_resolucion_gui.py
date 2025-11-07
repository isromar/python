import re
import tkinter as tk


def calcular_resolucion(reduccion=0.75):
    entrada_texto = entrada.get().strip().lower()
    if not entrada_texto:
        entrada_texto = "1920x1080"

    try:
        ancho_str, alto_str = re.split(r'[x*]', entrada_texto)
        ancho = int(ancho_str)
        alto = int(alto_str)

        nuevo_ancho = int(ancho * reduccion)
        nuevo_alto = int(alto * reduccion)

        resultado_label.config(text=f"Resolución reducida al {int(reduccion*100)}%: {nuevo_ancho}x{nuevo_alto}")

    except ValueError:
        resultado_label.config(text="Formato inválido. Usa '1920x1080'.")


# Interfaz Gráfica - GUI
root = tk.Tk()
root.title("Calculadora de Resoluciones")
root.geometry("400x200+500+50")

# Crear widget
label = tk.Label(root, text="Introduce la resolución (ejemplo: 1920x1080):")
# Colocar widget
label.pack(pady=10)

# Crear input
entrada = tk.Entry(root)
# Colocar input
entrada.pack(pady=5)

# Focus en el input
entrada.focus_set()

# Enlazar tecla 'Enter' con botón
entrada.bind("<Return>", lambda event: calcular_resolucion())

# Crear botón
boton = tk.Button(root, text="Calcular", command=lambda: calcular_resolucion())
# Colocar botón
boton.pack(pady=10)

# Crear widget vacío
resultado_label = tk.Label(root, text="")
# Colocar label
resultado_label.pack(pady=10)

# Mantener interfaz visible
root.mainloop()
