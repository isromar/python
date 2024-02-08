'''
Este módulo lee las carpetas y su contenido .txt
A partir de ahí crea un archivo .html que contiene como títulos los nombres de las carpetas y como contenido los diferentes textos de cada archivo .txt ordenado como listas
'''

import os

# Obtener la lista de carpetas en la carpeta raíz
carpetas = [d for d in os.listdir('.') if os.path.isdir(d)]

# Crear el archivo HTML
with open('index-de-carpetas.html', 'w', encoding='utf-8') as file:  # Especificar la codificación al crear el archivo
    file.write('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<title>Lista de Carpetas</title>\n</head>\n<body>\n')

    # Iterar sobre las carpetas y sus archivos
    for carpeta in carpetas:
        file.write(f'<h2>{carpeta}</h2>\n')
        archivos = [a for a in os.listdir(carpeta) if a.endswith('.txt')]
        file.write(f'<ol>')
        for archivo in archivos:
            with open(os.path.join(carpeta, archivo), 'r', encoding='latin-1') as txt_file:  # Especificar la codificación al abrir el archivo
                lineas = txt_file.readlines()
                titulo = lineas[0].strip('#').strip()
                texto = ''.join(lineas[2:]).strip()
                file.write(f'<li><h4>{titulo}</h4>\n<p>{texto}</p>\n</li>')
        file.write(f'</ol>')

    file.write('</body>\n</html>')