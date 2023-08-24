import numpy as np

c = int(input("Cantidad de vectores: "))

vectores = []
arr = []
vect = []
for j in range(1,c+1):
    vect = tuple(map(int, input("Vector "+ str(j) +": ").split(',')))
    vectores.append(vect)
res = np.linalg.matrix_rank(vectores)

if res == c:
   print("Linealmente Independiente")
else:
    print("Linealmente Dependiente")