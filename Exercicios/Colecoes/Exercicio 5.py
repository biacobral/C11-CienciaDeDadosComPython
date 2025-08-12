# 14/08/25
# Exercicio 5

soma = 0
cont = 0
n = int(input())

pessoas = []

for i in range(n):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    pessoas.append(pessoa)

for i in range(n):
    soma += pessoas[i]['idade']
    if pessoas[i]['sexo'] == 'F' and pessoas[i]['idade'] < 20:
        cont += 1

print(soma / n)
print(cont)
