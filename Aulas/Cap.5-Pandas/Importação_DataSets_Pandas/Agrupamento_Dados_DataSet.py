import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', delimiter=';')

group_region = ds.groupby('Region')

print(group_region.count()['Country']) # contar 'Country'
print(group_region.sum()['Country']) # agregar 'Country'
print(group_region.sum()['Population']) # somar populacao de cada regiao
