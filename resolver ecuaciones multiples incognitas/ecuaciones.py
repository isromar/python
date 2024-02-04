import numpy as np

""""
Resuelve un sistema de ecuaciones donde las incógnitas son x1, x2, x3...x100 y conocemos el valor de los coeficientes a1,a2,a3...b1,b2,b3... y de los términos independientes t1,t2...t100, ejemplo:

a1x1 + a2x2 + a3x3 + ... + a99x99 + a100x100 = t1
b1x1 + b2x2 + b3x3 + ... + b99x99 + b100x100 = t2
...
u1x1 + u2x2 + u3x3 + ... + u99x99 + u100x100 = t100

Se ha de crear un archivo de texto con los coeficientes de cada ecuación en filas, separados por comas o tabulador y el último de cada fila será el término independiente, ejemplo:

a1,a2,a3...a100,t1
b1,b2,b3...b100,t2
...
u1,u2,u3...u100,t100

que se guardará como coeficientes.txt
"""

# Leemos el archivo
#coeficientes = np.loadtxt('coeficientes.txt', delimiter=',|\t| ') no funciona esta expresión regular
try:
    coeficientes = np.loadtxt('coeficientes.txt', delimiter='\t')
except:
    pass
try:
    coeficientes = np.loadtxt('coeficientes.txt', delimiter=',')
except:
    pass

# Separamos la matriz de coeficientes A y el vector de términos independientes b
A = coeficientes[:, :-1]
b = coeficientes[:, -1]

# Obtenemos el número de incógnitas
n = A.shape[1]

# Imprimimos los datos
print('\nMatriz de coeficientes')
print(A)
print('\nTérminos independientes')
print(b)
print('\nNúmero de incógnitas:',n)

# Resolvemos el sistema de ecuaciones
try:
    det = np.linalg.det(A)
    if det == 0:
        print("\nEl sistema tiene soluciones infinitas.")
    else:
        x = np.linalg.solve(A, b)
        # Guardamos la solución en un archivo de texto
        np.savetxt('solucion.txt', x)
        # Imprimimos la solución
        print('\nSolución:',x)
except np.linalg.LinAlgError:
    print("\nEl sistema no tiene solución.")