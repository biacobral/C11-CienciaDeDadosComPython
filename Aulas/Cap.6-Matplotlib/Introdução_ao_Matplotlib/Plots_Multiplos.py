import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# criando valores para x e y
x = np.array([1, 2, 3, 4, 5])
y = x * 2 # broadcasting
y2 = x*x

# legenda
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# plotangem múltipla
plt.plot(x, y, '*:r', x, y2, 's--g', linewidth=3, markersize=10) # já formatado ('star pontos red', 'square traços green, largura da linha, tamanho marcador)
plt.show()