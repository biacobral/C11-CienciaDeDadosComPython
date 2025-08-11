# CONJUNTO (SET) É NÃO ORDENADA E NÃO ADMITE ELEMENTOS DUPLICADOS {}
#OBS.: NÃO GUARDA A ORDEM DOS ELEMENTOS
#OBS.: NÃO aceita duplicidade

conjunto = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
print(conjunto)

# adicionar elementos
conjunto.add('Bulma')
print(conjunto)
conjunto.add('Goku')
print(conjunto) # não aceitou o 'Goku' duplicado

# remover elementos
conjunto.remove('Trunks') # por valor
print(conjunto)

# alterar elementos -> não há, é necessário excluir e adicionar um novo
# OBS.: ao utilizar sorted numa coleção ela é convertida em uma lista organizada
