import numpy as np

np.random.seed(10)

arr = np.random.randint(1, 51, [4,4])

print(arr)

print(arr.mean(axis=0)) # media das colunas
print(arr.mean(axis=1)) # media das linhas

print(arr.mean(axis=0).max()) # maior media das colunas
print(arr.mean(axis=1).max()) # maior media das linhas

print(np.unique(arr, return_counts=True))

valores, contagens = np.unique(arr, return_counts=True)
print(valores[contagens == 2])