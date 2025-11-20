import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregando o dataset
dataset = pd.read_csv('airtravel.csv', delimiter=',', index_col='Date', parse_dates=True)

# Transformando os dados de y em float
dataset['Passengers'].astype(float)

# Plotando a Time Series
plt.figure(figsize=(8, 6))
plt.plot(dataset.index, dataset['Passengers'], marker='o')
plt.title('Número de passageiros de viagens de avião')
plt.xlabel('Data')
plt.ylabel('Passageiros')
plt.grid(True)
plt.show()

# Decomposição da série temporal
decomposition = seasonal_decompose(dataset['Passengers'], model='additive', period=12)

# Plotando os componentes da decomposição
decomposition.plot()
plt.show()

# A série possui tendência e é crescente, ou seja, o número de passageiros aumenta ao longo do tempo.
# Isso é visível no gráfico de tendência, que mostra uma linha ascendente

# A série possui sazonalidade e ocorre anualmente.
# Isso é evidente no gráfico de sazonalidade, onde os picos e vales seguem um padrão regular ao longo dos anos.

# Não é possível identificar um ciclo claro na série, sendo fortemente influenciada pela sazonalidade
