import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'], # linhas
    columns=['W', 'X', 'Y', 'Z'],   # colunas
    data = np.random.randint(1, 50, [5,4])  # inserindo valores aleatorios no df e, uma matriz 5x4
    )
print(df)

# slicing com iloc (padrão Numpy - índices numéricos)
print(df.iloc[0:2,:])
# slicing com loc (índices customizados)
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']])
print(df.loc[['A', 'B'], ['W', 'Y']])

# slicing para todas as linhas de colunas específicas
print(df[['W', 'Y']])
