# pyinstaller --noconsole --onefile --name "Temporizador_Power" apagar_pc.py

# Importamos el módulo principal de la interfaz gráfica Tkinter y su cuadro de diálogo de mensajes.
import tkinter as tk
from tkinter import messagebox

# Necesario para ejecutar comandos del sistema operativo (apagar/hibernar).
import os

# Utilidad nativa de Windows para generar pitidos audibles.
import winsound


class PowerApp:
    def __init__(self, root):
        # Guardamos la ventana principal.
        self.root = root
        # Título de la ventana.
        self.root.title("Power Timer")
        # Tamaño inicial de la ventana.
        self.root.geometry("350x320")

        # Variables de estado.
        self.tiempo_restante = 0  # Segundos que quedan para actuar.
        self.proceso_id = None  # ID del temporizador programado con root.after.
        self.modo = None  # Acción a realizar: "apagar" o "hibernar".

        # ---------- CONFIGURACIÓN DE LA INTERFAZ ----------
        # Etiqueta informativa para el usuario.
        tk.Label(root, text="Tiempo en minutos:", font=("Arial", 10)).pack(pady=10)

        # Campo donde el usuario escribe los minutos.
        self.entry_minutos = tk.Entry(
            root, justify="center", font=("Arial", 14), width=10
        )
        self.entry_minutos.insert(0, "60")  # Valor por defecto.
        self.entry_minutos.pack()

        # Etiqueta que muestra el tiempo restante o el estado de espera.
        self.label_contador = tk.Label(
            root, text="Esperando orden...", font=("Arial", 12, "bold"), fg="blue"
        )
        self.label_contador.pack(pady=20)

        # Contenedor para los botones de acción.
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Botón para iniciar el apagado.
        self.btn_apagar = tk.Button(
            frame,
            text="APAGAR",
            bg="#e74c3c",
            fg="white",
            width=12,
            height=2,
            command=lambda: self.iniciar("apagar"),
        )
        self.btn_apagar.pack(side="left", padx=5)

        # Botón para iniciar la hibernación.
        self.btn_hibernar = tk.Button(
            frame,
            text="HIBERNAR",
            bg="#3498db",
            fg="white",
            width=12,
            height=2,
            command=lambda: self.iniciar("hibernar"),
        )
        self.btn_hibernar.pack(side="left", padx=5)

        # Botón para cancelar cualquier temporizador activo.
        self.btn_abortar = tk.Button(
            root,
            text="ABORTAR Y RESETEAR",
            bg="#95a5a6",
            fg="white",
            width=28,
            command=self.abortar,
        )
        self.btn_abortar.pack(pady=10)

    def actualizar_contador(self):
        """Actualiza la cuenta regresiva cada segundo y reproduce un pitido cuando queda poco tiempo."""
        if self.tiempo_restante > 0:
            # Convertimos segundos a formato mm:ss.
            mins, segs = divmod(self.tiempo_restante, 60)
            # Mostramos el texto actualizado (modo en mayúsculas) y lo ponemos en rojo.
            self.label_contador.config(
                text=f"{self.modo.upper()} en: {mins:02d}:{segs:02d}", fg="red"
            )

            # Si quedan 15 segundos o menos, emitimos un pitido breve.
            if self.tiempo_restante <= 15:
                winsound.Beep(1000, 300)  # 1000Hz durante 300ms.

            # Decrementamos el contador y programamos la próxima actualización.
            self.tiempo_restante -= 1
            self.proceso_id = self.root.after(1000, self.actualizar_contador)
        else:
            # Tiempo terminado: ejecutamos la acción final (pitido largo + apagado/hibernado).
            self.ejecutar_accion_final()

    def ejecutar_accion_final(self):
        """Emite un pitido prolongado e inicia el apagado o la hibernación según el modo seleccionado."""
        # Pitido final más largo para avisar antes de actuar.
        winsound.Beep(1500, 1000)  # 1500Hz durante 1 segundo.

        if self.modo == "apagar":
            # Apagado forzado inmediato.
            os.system("shutdown /s /f /t 0")
        elif self.modo == "hibernar":
            # Hibernación forzada.
            os.system("shutdown /h /f")

    def iniciar(self, tipo):
        """Inicia el temporizador con el número de minutos proporcionado por el usuario."""
        minutos = self.entry_minutos.get()
        # Validamos que el valor introducido sea un número entero positivo.
        if not minutos.isdigit():
            messagebox.showerror("Error", "Pon un número válido.")
            return

        # Guardamos el modo de acción y convertimos a segundos.
        self.modo = tipo
        self.tiempo_restante = int(minutos) * 60

        # Bloqueamos la interfaz mientras el temporizador está activo.
        self.btn_apagar.config(state="disabled")
        self.btn_hibernar.config(state="disabled")
        self.entry_minutos.config(state="disabled")

        # Comienza la cuenta regresiva.
        self.actualizar_contador()

    def abortar(self):
        """Cancela el temporizador activo, detiene el apagado/hibernado y resetea la interfaz."""
        # Si hay un temporizador pendiente, lo cancelamos.
        if self.proceso_id:
            self.root.after_cancel(self.proceso_id)
            self.proceso_id = None

        # Si se estaba contando hacia un apagado, lo detenemos.
        if self.modo == "apagar":
            os.system("shutdown -a")

        # Reiniciamos las variables de estado.
        self.modo = None
        self.tiempo_restante = 0

        # Restauramos la interfaz a su estado inicial.
        self.label_contador.config(text="Esperando orden...", fg="blue")
        self.btn_apagar.config(state="normal")
        self.btn_hibernar.config(state="normal")
        self.entry_minutos.config(state="normal")

        # Informamos al usuario que el proceso fue cancelado.
        messagebox.showinfo("Abortado", "Proceso cancelado correctamente.")


if __name__ == "__main__":
    # Punto de entrada principal: creamos la ventana y lanzamos la aplicación.
    root = tk.Tk()
    app = PowerApp(root)
    root.mainloop()
