import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

df_usaCompany = df[df['Location'].str.contains('USA')]['Company Name']
df_chinaCompany = df[df['Location'].str.contains('China')]['Company Name']


df_usaCompany_unique = np.unique(df_usaCompany)
df_chinaCompany_unique = np.unique(df_chinaCompany)

count_usaCompany = len(df_usaCompany_unique)
count_chinaCompany = len(df_chinaCompany_unique)

x = ['EUA', 'China']
y = [count_usaCompany, count_chinaCompany]

plt.xlabel('País')
plt.ylabel('Número de Empresas')
plt.bar(x, y)
plt.show()