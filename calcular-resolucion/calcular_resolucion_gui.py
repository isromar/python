import re
import tkinter as tk


def calcular_resolucion(reduccion=0.75):
    # Obtiene el texto del campo de entrada global, elimina espacios y pasa a minúsculas
    entrada_texto = entrada.get().strip().lower()
    # Si el campo está vacío, usa una resolución por defecto
    if not entrada_texto:
        entrada_texto = "1920x1080"

    try:
        # Divide el texto usando 'x' o '*' como separador para obtener ancho y alto
        ancho_str, alto_str = re.split(r"[x*]", entrada_texto)
        ancho = int(ancho_str)

        # --- INICIO DE BLOQUE PROBLEMÁTICO ---
        # Crea una NUEVA ventana principal (Tk) dentro de la función
        ventana = tk.Tk()
        ventana.title("Calculadora de Resolución")

        # Crea widgets (Entry, Button, Label) DENTRO de esta nueva ventana local
        entrada = tk.Entry(ventana)
        entrada.pack(pady=10)

        btn = tk.Button(ventana, text="Calcular 75%", command=calcular_resolucion)
        btn.pack()

        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack(pady=10)

        # Inicia el bucle principal de ESTA ventana secundaria (bloquea el código siguiente)
        ventana.mainloop()
        # --- FIN DE BLOQUE PROBLEMÁTICO ---
        # El código debajo de mainloop() no se ejecuta hasta que se cierra 'ventana'

        # Convierte el alto a entero (se ejecuta tras cerrar la ventana secundaria)
        alto = int(alto_str)

        # Calcula las nuevas dimensiones aplicando el factor de reducción
        nuevo_ancho = int(ancho * reduccion)
        nuevo_alto = int(alto * reduccion)

        # Intenta actualizar la etiqueta de resultado (fallará si 'resultado_label' es la local ya destruida)
        resultado_label.config(
            text=f"Resolución reducida al {int(reduccion*100)}%: {nuevo_ancho}x{nuevo_alto}"
        )

    except ValueError:
        # Captura error si la conversión a entero falla o el formato es incorrecto
        resultado_label.config(text="Formato inválido. Usa '1920x1080'.")


# Interfaz Gráfica Principal (GUI)
root = tk.Tk()
root.title("Calculadora de Resoluciones")
root.geometry("400x200+500+50")

# Etiqueta de instrucción
label = tk.Label(root, text="Introduce la resolución (ejemplo: 1920x1080):")
label.pack(pady=10)

# Campo de entrada global (el que realmente usa el usuario)
entrada = tk.Entry(root)
entrada.pack(pady=5)

# Pone el foco del teclado en el campo de entrada al iniciar
entrada.focus_set()

# Vincula la tecla Enter para llamar a la función calcular_resolucion
entrada.bind("<Return>", lambda event: calcular_resolucion())

# Botón principal que ejecuta el cálculo
boton = tk.Button(root, text="Calcular", command=lambda: calcular_resolucion())
boton.pack(pady=10)

# Etiqueta global para mostrar el resultado o errores
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

# Inicia el bucle principal de la aplicación (ventana 'root')
root.mainloop()
