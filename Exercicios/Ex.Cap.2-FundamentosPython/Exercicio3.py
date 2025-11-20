#07/08/2025

# Exercício 3:

sexo = input("Digite seu sexo: ")
while sexo != "F" and sexo != "M":
    print("Sexo invalido")
    sexo = input("Digite seu sexo: ")
if sexo == "F":
    print("Feminino")
else: print("Masculino")