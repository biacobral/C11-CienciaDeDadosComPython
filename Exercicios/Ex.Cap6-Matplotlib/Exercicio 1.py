import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('paises.csv', delimiter=';')

df_northAmer = df[df['Region']=='NORTHERN AMERICA                   ']



northAmer_country = df_northAmer['Country']
northAmer_deathrate = df_northAmer['Deathrate']
northAmer_birthrate = df_northAmer['Birthrate']

plt.plot(northAmer_country, northAmer_deathrate, '.-r', northAmer_country, northAmer_birthrate, '.-b', linewidth=2, markersize=10)
plt.show()
