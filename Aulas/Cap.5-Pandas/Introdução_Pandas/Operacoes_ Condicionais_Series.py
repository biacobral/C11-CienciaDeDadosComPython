import pandas as pd

# criando dois dicionarios
dic1 = {'a':10,'b':20,'c':30}
dic2 = {'a':10,'b':20,'d':30}

# criando series com dicionarios
series1 = pd.Series(dic1)
series2 = pd.Series(dic2)

# operações entre series
# pandas faz operação elemento a elemento por 'LABEL'
print(series1 + series2)
print(series1 - series2)

# operação elemento a elemento COM VALOR PADRÃO (nesse caso =0)
print(series1.add(series2, fill_value=0)) # soma
print(series1.sub(series2, fill_value=0)) # subtração

# condicionais
print(series1 <= 20) # máscara
print(series1[series1 <= 20]) # elementos