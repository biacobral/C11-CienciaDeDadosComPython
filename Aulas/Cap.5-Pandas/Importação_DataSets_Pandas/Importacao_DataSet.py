import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', delimiter=';')

# printar colunas
print(ds.columns)
# printar n linhas de cima para baixo
print(ds.head(2))
# printar n linhas de baixo para cima
print(ds.tail(2))