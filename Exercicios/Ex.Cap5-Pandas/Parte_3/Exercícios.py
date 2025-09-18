import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', delimiter=';')

# Questão 1
print("====Questão 1====")

print(df[df['Region'].str.contains('OCEANIA')]['Country'])

group_region = df.groupby('Region')
country_region = group_region['Country'].count()

country_region.index = country_region.index.str.strip()
print(country_region['OCEANIA'])

# Questão 2
print("====Questão 2====")

print(df.nlargest(1, 'Population')[['Country', 'Region']])

# Questão 3
print("====Questão 3====")

print(group_region['Literacy (%)'].mean())

# Questão 4
noCoast = df[df['Coastline (coast/area ratio)'] == 0]

noCoast.to_csv('noCoast.csv', sep=';')

# Questão 5
print("====Questão 5====")

def humanitarianHelp(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'
df['Humanitarian Help'] = df['Deathrate'].apply(humanitarianHelp)
print(df)