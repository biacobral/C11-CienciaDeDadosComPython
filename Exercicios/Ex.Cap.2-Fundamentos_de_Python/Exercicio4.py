#07/08/2025

# Exercício 4:

distancia = float(input("Distancia: "))

while distancia < 0:
    print("Distancia invalida")
    distancia = float(input("Distancia: "))

if distancia <= 200:
    total = distancia*0.5
else:
    total = distancia*0.45

print(f"Preço da passagem: R$ {total:.2f}")