import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Gráfico de Dispersão

df = pd.read_csv('paises.csv', delimiter=';')
print(df.columns)

# extraindo 6 maiores países (area) do mundo
df_maiores = df.nlargest(6, 'Area (sq. mi.)')
print(df_maiores['Country'])

# traça scatter plot para GDP per capita
plt.scatter(df_maiores['Country'], df_maiores['GDP ($ per capita)'], s=df_maiores['Area (sq. mi.)']/10000) # x - Country, y - GDP, size=tamanho do país
plt.show()

