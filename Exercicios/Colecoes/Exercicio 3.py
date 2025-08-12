# 14/08/25
# Exercicio 3

nome = input('Nome: ')
media = float(input('Media: '))

aluno = {'Nome': nome, 'Media': media}

if media >= 50:
    aluno['SF'] = 'AP'
else:
    aluno['SF'] = 'RP'

print(aluno)