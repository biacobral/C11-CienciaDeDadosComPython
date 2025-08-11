import math
#07/08/2025

# Exercício 6:

numero = float(input("Digite um numero: "))

raiz = numero ** (1/2)
print(f"Raiz: {raiz:.2f}")

teto = math.ceil(numero)
print(f"Função Teto {teto}")

chao = math.floor(numero)
print(f"Função Chão: {chao}")

inteiro = numero // 1
print(f"Parte Inteira: {inteiro:.0f}")