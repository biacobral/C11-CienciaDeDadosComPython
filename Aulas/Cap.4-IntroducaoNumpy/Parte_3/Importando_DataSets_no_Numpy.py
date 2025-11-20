import numpy as np

ds = np.loadtxt('space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

# Colunas do dataset
print(ds[0,:]) # ou print(ds[0]) -> primeira linha

# Média de gastos de uma missão (coluna 'Cost')
ds_cost = ds[:,6] # slicing da coluna 'Cost'(todas as linhas)
print(ds_cost)
ds_cost = ds[1:,6] # slicing para pegar apenas valores
print(ds_cost)

ds_cost = ds_cost.astype(float) # str -> float
print(np.mean(ds_cost)) # media
