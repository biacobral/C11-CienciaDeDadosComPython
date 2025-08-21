import numpy as np
from numpy.ma.core import concatenate

arr1 = np.arange(0,51,2)
arr2 = np.arange(100,50,-2)

print(arr1)
print(arr2)

print(np.sort(np.concatenate((arr1, arr2))))