# subpacote char

import numpy as np

arr = np.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma', 'Mago'])
print(arr)

# Encontrar um padrão no array
print(np.char.find(arr, 'Go')) # -1 não encontrado, se encontrado retorna índice>=0

# Criar 'máscara' True e False
print(np.char.find(arr, 'Go')>=0)

# Retornar os elementos
print(arr[np.char.find(arr, 'Go')>=0])

print() #pular linha

# Padronizar a busca
arr = np.char.upper(arr)
print(arr)
print(np.char.find(arr, 'GO')>=0)
print(arr[np.char.find(arr, 'GO')>=0])