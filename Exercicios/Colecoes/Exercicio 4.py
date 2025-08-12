# 14/08/25
# Exercicio 4

pessoa1 = {
    'nome': input('Nome: '),
    'peso': int(input('Peso: '))
}
pessoa2 = {
    'nome': input('Nome: '),
    'peso': int(input('Peso: ')),
}
pessoa3 = {
    'nome': input('Nome: '),
    'peso': int(input('Peso: ')),
}

pessoas = [pessoa1, pessoa2, pessoa3]

print(max(pessoas, key=lambda x: x['peso']))
print(min(pessoas, key=lambda x: x['peso']))

