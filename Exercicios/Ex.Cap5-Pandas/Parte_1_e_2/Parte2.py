import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'], # linhas
    columns = ['W', 'X', 'Y', 'Z'],   # colunas
    data = np.random.randint(1, 50, [5,4])
    )
print(df)

# Questão 6
print("====Questão 6====")
print((df['X'][df['X'] < 30]).mean())

# Questão 7
print("====Questão 7====")
print((df.loc['D']).mean())
print((df.iloc[4,0:]).sum())

# Questão 8
print("====Questão 8====")
df8 = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(df8)
print(f"Linhas:\n{df8.sum(axis=1)}")
print(f"Colunas:\n{df8.sum(axis=0)}")


