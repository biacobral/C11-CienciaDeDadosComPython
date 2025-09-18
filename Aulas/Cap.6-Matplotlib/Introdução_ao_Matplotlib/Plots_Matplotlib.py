import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# criando valores para x e y
x = np.array([1, 2, 3, 4, 5])
y = x * 2 # broadcasting

# legenda
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# plotando gráfico
plt.plot(x, y, '*:r', linewidth=3, markersize=10) # já formatado ('star pontilhado red', largura da linha, tamanho marcador)
plt.show()
