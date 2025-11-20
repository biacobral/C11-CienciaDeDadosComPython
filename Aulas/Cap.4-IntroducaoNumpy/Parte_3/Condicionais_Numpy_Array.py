import numpy as np

mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)

# Com 'máscara' (True e False)
print(mtz>5)

# Retornando numeros usando a 'mascara'
print(mtz[mtz>5])

# Apenas números pares
print(mtz[mtz%2==0])