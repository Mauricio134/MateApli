import numpy as np

# Ingresar los vectores como filas
print("Ingresa los vectores en el formato (x, y):")
vector1 = tuple(map(int, input("Primer vector: ").split(',')))
vector2 = tuple(map(int, input("Segundo vector: ").split(',')))

# Crear la matriz con los vectores
matrix = np.array([vector1, vector2])

# Calcular el rango de la matriz
rank = np.linalg.matrix_rank(matrix)

if rank == len(matrix):
    print("El conjunto de vectores es linealmente independiente.")
else:
    print("El conjunto de vectores es linealmente dependiente.")
