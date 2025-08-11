#07/08/2025

# Exercício 5:

numero = int(input("Digite um numero: "))

while numero < 1000 or numero > 9999:
    print("Numero invalido")
    numero = int(input("Digite um numero: "))

numero = str(numero)

unidade = numero[3]
print(f"Unidade: {unidade}")

dezena = numero[2]
print(f"Dezena: {dezena}")

centena = numero[1]
print(f"Centena: {centena}")

milhar = numero[0]
print(f"Milhar: {milhar}")