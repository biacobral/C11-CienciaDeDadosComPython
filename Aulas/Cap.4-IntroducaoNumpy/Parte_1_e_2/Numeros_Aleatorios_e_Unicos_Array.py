import numpy as np

# Gerar numeros aleatorios
arr = np.random.randint(1, 101, 10) # intervalo e quantidade
print(arr)

# Semente aleatória
np.random.seed(10)
arr = np.random.randint(1, 101, 10)
print(arr)

# Elementos unicos
# no python utiliza-se conjuntos para elementos unicos
arr = np.random.randint(1, 10, 10)
print(arr)
print(np.unique(arr)) # mostra elementos únicos ordenados
print(np.unique(arr, return_counts=True)) # quantidade de vezes - elementos unicos e contagem