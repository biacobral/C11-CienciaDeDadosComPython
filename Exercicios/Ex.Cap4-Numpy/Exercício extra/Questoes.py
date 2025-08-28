import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

print(f"Colunas: \n{ds[0,:]}") # mostrar colunas

# Country[0], Region[1], Population[2], Area[3]
print("\n====Questão 1====")
print(ds[1:,:4])

# Diferentes regiões
print("\n====Questão 2====")
ds_regions = ds[1:,1]
ds_regions_unique = np.unique(ds_regions)
print(f"Quantidade: {ds_regions_unique.size}")
print(f"Regiões:\n {ds_regions_unique}")


# Taxa média de Literacy do planeta
print("\n====Questão 3====")
ds_literacy = ds[1:,9]
ds_literacy = ds_literacy.astype(float)
print(f"Taxa média de alfabetização no planeta: {np.mean(ds_literacy)}%")

# Quantos países Northern America
print("\n====Questão 4====")
ds_regions_NA = np.char.find(ds_regions, "NORTHERN AMERICA")>=0
print(f"{np.sum(ds_regions_NA==True)} países da América do Norte")

# Maior renda per capita entre America do Sul e Caribe
print("\n====Questão 5====")

ds_GDP = ds[1:,8] # valores do GDP
ds_GDP = ds_GDP.astype(float)

ds_latinAmer_carib = np.char.find(ds_regions, "LATIN AMER. & CARIB")>=0
ds_latinAmer_carib_GDP = ds_GDP[ds_latinAmer_carib]
ds_latinAmer_carib_GDP_max = np.max(ds_latinAmer_carib_GDP)
index = np.argmax(ds_latinAmer_carib_GDP)
pais = ds[1:,0][ds_latinAmer_carib][index]
print(f"Maior renda per capita LATIN AMER. & CARIB: {pais} = ${ds_latinAmer_carib_GDP_max}")