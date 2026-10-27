# Resolución de un sistema de ecuaciones con NumPy
Este script en Python utiliza la biblioteca NumPy para resolver un sistema de ecuaciones lineales. El sistema de ecuaciones se define con un número variable de incógnitas (en este caso, hasta 100) y se espera que el usuario proporcione un archivo de texto con los coeficientes y términos independientes.  

## Archivo necesario llamado coeficientes.txt
Un ejemplo del archivo .txt a proporcionar sería  
2,4,6,18  
4,5,6,24  
3,1,-2,4  
siendo el último número de cada fila el término independiente de esa ecuación

## Instalación de NumPy
Asegúrate de tener NumPy instalado en tu entorno de Python. Si no lo tienes instalado, puedes hacerlo utilizando el siguiente comando:

```bash
pip install numpy
```

## Cómo ejecutarlo

Guarda los coeficientes en `coeficientes.txt` dentro de esta carpeta y ejecuta:

```bash
python ecuaciones.py
```

El programa muestra la matriz y la solución en la consola, y guarda los valores calculados en `solucion.txt`.

Para obtener una solución única, el sistema debe tener el mismo número de ecuaciones que de incógnitas y una matriz de coeficientes invertible.

## Image preview
![Preview](https://raw.githubusercontent.com/isromar/Python/main/resolver-ecuaciones-multiples-incognitas/preview.JPG)
