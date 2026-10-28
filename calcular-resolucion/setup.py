import sys  # Importa el módulo sys para operaciones del sistema
import os  # Importa el módulo os para manejar rutas de archivos y directorios
from cx_Freeze import setup, Executable  # Importa las funciones principales de cx_Freeze para crear ejecutables

# Rutas de Tcl/Tk dentro del entorno virtual
venv_dir = r"C:\xampp\htdocs\Python\entorno_para_tkinter\1\.venv_2"  # Ruta al entorno virtual de Python donde está instalado Tkinter
tcl_dir = os.path.join(venv_dir, "tcl", "tcl8.6")  # Ruta completa a la biblioteca Tcl dentro del entorno virtual
tk_dir = os.path.join(venv_dir, "tcl", "tk8.6")  # Ruta completa a la biblioteca Tk dentro del entorno virtual

build_options = {
    "packages": ["tkinter", "re"],  # Paquetes de Python que se incluirán en el ejecutable final
    "include_files": [
        (tcl_dir, "tcl"),  # Copia los archivos de Tcl al directorio de compilación para que Tkinter funcione
        (tk_dir, "tk"),  # Copia los archivos de Tk al directorio de compilación para que Tkinter funcione
    ],
}

exe = Executable(
    script="calcular_resolucion.py",  # Archivo principal de Python que se convertirá en ejecutable
    base="Win32GUI",  # Indica que es una aplicación de interfaz gráfica de Windows y evita que se abra la consola negra
)

setup(
    name="CalculadoraResoluciones",  # Nombre que se le dará a la aplicación generada
    version="1.0",  # Número de versión del programa
    description="Calculadora de Resoluciones con Tkinter",  # Descripción breve de lo que hace la aplicación
    options={"build_exe": build_options},  # Pasa las opciones de compilación definidas anteriormente
    executables=[exe],  # Lista con los ejecutables que cx_Freeze debe generar
)
