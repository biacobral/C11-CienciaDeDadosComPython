import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', delimiter=';')

# criar uma nova coluna que mostre a porcentagem
# de população de cada país em relação a população global

somaPopulacao = np.sum(ds['Population'])
print(somaPopulacao)

# porcentagem da populacao de cada pais
# broadcasting (escalar por vetorial)
populationPerc = ds['Population']/somaPopulacao
print(populationPerc)

# adicionar coluna no dataset
ds['PopulationPercent'] = populationPerc
print(ds)

# criando uma nova versao do dataset
ds.to_csv('paises2.csv', sep=';')