import numpy as np

arr1 = np.arange(1, 11, 1) # crescente

print(arr1.min()) # menor valor
print(arr1.max()) # maior valor
print(arr1.mean()) # media
print(arr1.argmax()) # índice do maior valor

arr2 = np.arange(10, 0, -1) # decrescente

print(arr1, arr2)

# Operação elemento a elemento (qualquer operador)
# números de elementos devem ser compativeis
print(arr1 + arr2)

# Concatenar
print(np.concatenate([arr1, arr2])) # dois arrays no mesmo array

# Operações com Matrizes (NumPy Array 2D)
# gastos janeiro, fevereiro, março
mtz = np.array([50, 10, 100, 60, 25, 100, 75, 80, 100]).reshape(3,3)
print(mtz)

print(mtz.sum(axis=1)) #somas das linhas (EIXO 1) - meses
print(mtz.sum(axis=0)) #somas das colunas (EIXO 0) - gastos

print(mtz.sum(axis=0)[2]) # soma das colunas (EIXO 0) no índice 0

# Broadcasting
# fazer operações de um vetor com um escalar

print(mtz/10)


