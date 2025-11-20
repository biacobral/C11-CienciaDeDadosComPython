#07/08/2025

# Exercício 2:

numero = int(input("Digite um numero para a tabuada: "))

i = int(input("Intervalo: "))

for j in range (0, i+1):
    print(f"{numero} * {j} = {numero * j}")