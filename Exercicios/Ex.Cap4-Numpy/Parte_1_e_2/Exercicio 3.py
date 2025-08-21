import numpy as np

arr = np.zeros((2, 2))

linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)
arr[linha, coluna] = 1
print(arr)  # verificando

acertos = 0

while acertos < 3:
    print("Escolha uma posição do campo minado")
    pos_linha = int(input("Linha: "))
    pos_coluna = int(input("Coluna: "))
    if arr[pos_linha, pos_coluna] == 0:
        acertos += 1
    else:
        print("Game Over! :( Try again!")
        break

print("Congratulations! You beat the game! :)")

