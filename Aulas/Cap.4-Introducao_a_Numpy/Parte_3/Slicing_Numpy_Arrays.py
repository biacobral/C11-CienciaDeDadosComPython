import numpy as np

# Criando um Numpy Array 2D
mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)

# Extraindo apenas uma linha
print(mtz[2]) # terceira linha

# Extraindo apenas uma coluna
print(mtz[:,1]) # segunda coluna -> : (todas as linhas) , 1 (coluna)

# Extraindo apenas umas coluna
print(mtz[:,1:]) # segunda e terceiras colunas (segunda [1] para frente)