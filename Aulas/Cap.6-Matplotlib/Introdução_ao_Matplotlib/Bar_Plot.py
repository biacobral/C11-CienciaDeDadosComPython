import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('paises.csv', delimiter=';')
print(df.columns)

# extraindo 5 países com maior GDP
df_ricos = df.nlargest(5, 'GDP ($ per capita)')
print(df_ricos['Country'])

# plotando em barras
plt.bar(df_ricos['Country'], df_ricos['GDP ($ per capita)'])
plt.show()