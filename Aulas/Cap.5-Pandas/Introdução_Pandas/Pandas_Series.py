import pandas as pd

indices = ['a', 'b', 'c']
valores = [10, 20, 30]

series = pd.Series(index=indices, data=valores)

# pode-se alimentar uma serie com um dicionário
# dic = {'a': 10, 'b': 20, 'c': 30}
# series = pd.Series(dic)

print(series)
print(type(series))

print(series['a'])
