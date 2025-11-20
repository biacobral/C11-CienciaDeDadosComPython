import numpy as np

# Para estruturar arrays utiliza-se zeros e ones
# Array 1D de 1's
arr = np.ones(10)
print(arr)
# Array 2D de 0's com RESHAPE (para ser bidirecional)
mtz = np.zeros(10).reshape(5,2) # matriz 5x2
print(mtz)

# Matriz
mtz = np.zeros([5,2])
print(mtz)

# ARANGE
arr = np.arange(10,101,10) # de 10 (inclusivo) a 101 (exclusivo) passo de 10
print(arr)