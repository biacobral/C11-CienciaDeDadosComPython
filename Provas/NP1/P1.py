# Beatriz Vaz Pedroso Santos Cobral
# 2082

import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')
print(ds[0,:]) # mostrar colunas

# Média de idade dos homens
print("====Questão 1====")
ds_genero = ds[1:,2]
ds_homens = np.char.find(ds_genero, 'Male')>=0
ds_idade = ds[1:,1]
ds_idade = ds_idade.astype(int)
ds_homens_idade = ds_idade[ds_homens]

print(f"Média de idade dos homens: {ds_homens_idade.mean()}")

# Quantidade de clientes que gastaram mais que a média de gastos
print("\n====Questão 2====")

ds_gastos = ds[1:,5]
ds_gastos = ds_gastos.astype(float)
ds_media_gastos = ds_gastos.mean()
print(f"Média de gastos: {ds_media_gastos}")
ds_gastos_acima_media = ds_gastos>ds_media_gastos # máscara

print(f"Quantidade acima da média: {ds_gastos[ds_gastos_acima_media].size}")

# Porcentagem de vendas do item menos vendido
print("\n====Questão 3====")
ds_itens = ds[1:,3]
ds_itens_unique, count = np.unique(ds_itens, return_counts=True)
count = count.astype(int)
ds_itens_min = count.min()

print(f"A porcentagem do item menos vendido é: "
      f"{ds_itens_unique.size/ds_itens_min*100}%")

# Porcentagem de vendas com desconto
print("\n====Questão 4====")

ds_descontos = ds[1:,13]
ds_com_desconto = np.char.find(ds_descontos, 'Yes')>=0
quantidade_desconto = ds_descontos[ds_com_desconto].size

print(f"Porcentagem com desconto: {quantidade_desconto/ds_descontos.size*100}%")

# Cor de roupa mais popular no verão
print("\n====Questão 5====")

ds_cor = ds[0:,8]

ds_season = ds[0:,9]
ds_verao = np.char.find(ds_season, 'Summer')>=0
ds_cor_verao = ds_cor[ds_verao]

ds_cor_verao_unique, count = np.unique(ds_cor_verao, return_counts=True)
count = count.astype(int)
ds_cor_verao_max = count.argmax()
ds_cor_do_verao = ds_cor_verao_unique[ds_cor_verao_max]

print(f"A cor de roupa mais vendida no verão foi: {ds_cor_do_verao}")
