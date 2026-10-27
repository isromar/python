# Convertidor de Texto a MP3 con gTTS

## Descripción
Este script en Python convierte archivos de texto en archivos de audio MP3 utilizando la librería `gTTS` (Google Text-to-Speech). Al finalizar, pregunta al usuario para reproducir el archivo generado.

## Requisitos
- Tener instalado Python.
- Instalar la librería `gTTS`:
  ```bash
  pip install gtts
  ```

## Uso
1. Coloca el archivo de texto que deseas convertir en el mismo directorio que el script.
2. Ejecuta el script:
   ```bash
   python nombre_del_script.py
   ```
3. Sigue las indicaciones:
   - Ingresa el nombre del archivo de texto **sin extensión** (ej: `ejemplo` para `ejemplo.txt`).
   - Selecciona el idioma del texto (`es` para español, `en` para inglés por defecto).
   - Espera a que se genere el archivo MP3.
   - Al finalizar, responde `s` para reproducir el audio o `n` para solo guardarlo.

## Notas
- El archivo MP3 se guardará en el mismo directorio que el script.
- El script ignora caracteres no compatibles con UTF-8 al leer el archivo de texto.

## Image preview
![Preview](https://raw.githubusercontent.com/isromar/Python/main/generar-mp3-desde-txt/preview.JPG)

## How it works
[Video](https://youtu.be/skiGZmFa36k)

## Autor
Isabel Rodenas Marin