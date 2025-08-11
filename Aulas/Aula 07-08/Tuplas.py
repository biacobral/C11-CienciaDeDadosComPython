# TUPLA É UMA COLEÇÃO IMUTÁVEL ()

tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

# mostrar elementos da tupla
print(tupla)

# alterar tupla
# tupla[0] = 'Bulma'
# print(tupla)
# erro: tupla é uma coleção imutável
# segurança, acessibilidade

# slicing de elementos
print(tupla[1:3]) # Vegeta e Trunks
# OBS.:[X:X] a primeira posição é incluída e a segunda excluída
print(tupla[2:]) # Trunks e Gohan
# OBS.:[X:] a partir de X
print(tupla[-2]) # Trunks com índice negativo
# OBS.:[-X] de trás pra frente

# leitura de elementos
for i in range (len(tupla)):
    print(f"Na posição {i}: {tupla[i]}")

# funções
print(len(tupla)) #quantidade
print(max(tupla)) #string -> ordem alfabética
print(min(tupla)) #string -> ordem alfabética


