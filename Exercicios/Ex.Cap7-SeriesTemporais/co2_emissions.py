import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregando o dataset
dataset = pd.read_csv('co2_emissions.csv', delimiter=',', index_col='Year', parse_dates=True)

# Transformando os dados de y em float
dataset['CO2_Emissions'].astype(float)

# Plotando a Time Series
plt.figure(figsize=(8, 6))
plt.plot(dataset.index, dataset['CO2_Emissions'], marker='o')
plt.title('CO2_Emissions')
plt.xlabel('Data')
plt.ylabel('CO2_Emissions')
plt.grid(True)
plt.show()

# Decomposição da série temporal
decomposition = seasonal_decompose(dataset['CO2_Emissions'], model='additive', period=12)

# Plotando os componentes da decomposição
decomposition.plot()
plt.show()

# A série possui tendência e é decrescente, ou seja, as emissões de CO₂ diminuem ao longo do tempo.
# Isso é visível no gráfico de tendência, que mostra uma linha descendente.

# A série possui sazonalidade e ocorre anualmente.
# Isso é evidente no gráfico de sazonalidade, onde os padrões se repetem de forma consistente ao longo dos anos.

# Não é possível identificar um ciclo claro na série, pois as variações de longo prazo são explicadas pela tendência e pela sazonalidade.