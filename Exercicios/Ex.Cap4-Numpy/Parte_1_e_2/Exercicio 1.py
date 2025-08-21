import numpy as np
arr1 = np.ones(8)
arr2 = np.random.randint(0, 9, 8)
print(arr1)
print(arr2)

arr3 = arr1 + arr2
print(arr3)

print() # pular uma linha
print(arr3.sum(axis=0)) # mostrar soma

if arr3.sum(axis=0) >= 40:
    print(arr3.reshape(4,2))
else:
    print(arr3.reshape(2,4))