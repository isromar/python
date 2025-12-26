import sys
import os
from cx_Freeze import setup, Executable

# Rutas de Tcl/Tk dentro del venv
venv_dir = r"C:\xampp\htdocs\Python\entorno_para_tkinter\1\.venv_2"
tcl_dir = os.path.join(venv_dir, "tcl", "tcl8.6")
tk_dir = os.path.join(venv_dir, "tcl", "tk8.6")

build_options = {
    "packages": ["tkinter", "re"],
    "include_files": [
        (tcl_dir, "tcl"),
        (tk_dir, "tk"),
    ],
}

exe = Executable(
    script="calcular_resolucion.py",
    base="Win32GUI",  # evita consola negra
)

setup(
    name="CalculadoraResoluciones",
    version="1.0",
    description="Calculadora de Resoluciones con Tkinter",
    options={"build_exe": build_options},
    executables=[exe],
)
