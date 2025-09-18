import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('paises.csv', delimiter=';')
print(df.columns)

# extraindo sem costa
df_noCoast = df[df['Coastline (coast/area ratio)']==0]
print(df_noCoast['Country'])

# quantidade sem costa e com costa
count_noCoast = len(df_noCoast)
count_coast = len(df) - count_noCoast

# plotando pizza
plt.pie([count_noCoast, count_coast], labels=['Países sem costa', 'Países com costa'], autopct='%1.1f%%')
plt.show()