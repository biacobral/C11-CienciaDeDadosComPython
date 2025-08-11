# LISTA É UMA COLEÇÃO MUTÁVEL, DINÂMICA []

lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# mostrar elementos
print(lista)

# inserir elementos
lista.append('Bulma') # adiciona no final
lista.insert(1, 'Kuririn') # adiciona no índice
print(lista)

# alterar elementos
lista[0] = 'Piccolo'
print(lista)

# excluir elementos
del lista[0] # remoção pelo índice
lista.remove('Bulma') # remoção por valor
print(lista)




