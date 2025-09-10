import pandas as pd

dic1 = {'Java':16.25, 'C': 16.04, 'Python': 9.85}
dic2 = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}

# Questão 1
seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

# Questão 2
print("====Questão 2====")
print(f"Porcentagem total no mercado (ano 1): {seriesAno1.sum()}")
print(f"Porcentagem total no mercado (ano 2): {seriesAno2.sum()}")

# Questão 3
print("====Questão 3====")
cresc_decl = (seriesAno2 - seriesAno1)
print(f"Crescente / Declínio: \n{cresc_decl}")

# Questão 4
print("====Questão 4====")
print(cresc_decl[cresc_decl > 0])

# Questão 5
print("====Questão 5====")
seriesAno3 = seriesAno2 + cresc_decl
seriesAno4 = seriesAno3 + cresc_decl
print(seriesAno4.nlargest(1))
