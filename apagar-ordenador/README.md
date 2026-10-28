# Temporizador Power

El proyecto incluye dos versiones: `apagar_pc.py`, una aplicación de escritorio con temporizador visual, y `apagar_pc_cmd.py`, para usar desde la línea de comandos.

## Requisitos

- Python 3.x
- Sistema operativo Windows (requiere comandos `shutdown` y `winsound`)

## Instalación

1. Clona o descarga el repositorio.
2. Ejecuta el script directamente:
   ```bash
   python apagar_pc.py
   ```

## Uso

1. Introduce el tiempo en minutos (ej. `60`).
2. Selecciona **APAGAR** o **HIBERNAR**.
3. La interfaz mostrará una cuenta regresiva con pitidos cada 15 segundos.
4. Usa **ABORTAR Y RESETEAR** para cancelar el proceso en cualquier momento.

## Compilación (opcional)

Genera un ejecutable standalone con PyInstaller:
```bash
pyinstaller --noconsole --onefile --name "Temporizador_Power" apagar_pc.py
```

## Características

- Interfaz gráfica intuitiva con Tkinter.
- Pitidos audibles para notificaciones.
- Cancelación segura del proceso de apagado/hibernación.

## Image preview
![Preview](https://raw.githubusercontent.com/isromar/Python/main/apagar-ordenador/preview.jpg)

## Idea

Este programa surge porque el apagado automático del PC no funcionaba adecuadamente, entonces pensé crear un programa que tuviese la opción de hibernar y de apagar el ordenador.

## Autor

Isabel Rodenas Marin




