import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# criando valores para x e y
x = np.array([1, 2, 3, 4, 5])
y = x * 2 # broadcasting
y2 = x*x

# matriz de subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, '*:r', linewidth=3, markersize=10)
plt.subplot(1, 2, 2)
plt.plot(x, y2, 's--g', linewidth=3, markersize=10)

plt.show()