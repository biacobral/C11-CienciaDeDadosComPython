# DICIONÁRIO (DICTIONARY) É UM CONJUNTO KEY: VALUE MUTÁVEL

pessoa = {
    'nome': 'Goku',
    'idade': 43,
    'sexo':'masculino'
}
print(pessoa)

# adicionar elementos
pessoa['raca'] = 'Sayajin'
print(pessoa)

# atualizar elementos
pessoa['idade'] = 45
print(pessoa)

# excluir elementos
del pessoa['sexo'] # exclusão por valor
print(pessoa)

# lista no dicionario (coleções dentro de coleções)
pessoa['familia'] = ['Gohan', 'Goten', 'Chichi', 'Pan']
print(pessoa)
# acessando a Chichi
print(pessoa['familia'][2])