from email.utils import decode_rfc2231

import pandas as pd

df = pd.read_csv('paises.csv', delimiter=';')

# remove linhas que possuam dados ausentes
df2 = df.dropna()

# preenche dados ausentes com um valor padrao
df3 = df.fillna(0)