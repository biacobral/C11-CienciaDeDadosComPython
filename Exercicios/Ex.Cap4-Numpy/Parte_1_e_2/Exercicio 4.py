# maneira simples

import numpy as np

mtz = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

linhas, colunas = mtz.shape
print(mtz.shape)

total = linhas * colunas

if total% 2 == 0:
    print("Par")
else:
    print("Ímpar")
