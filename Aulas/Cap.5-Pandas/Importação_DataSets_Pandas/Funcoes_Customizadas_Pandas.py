import pandas as pd

ds = pd.read_csv('paises.csv', sep=';')

# função para dar desconto de 10% em x
def tenpercent(x):
    return x * 0.9

# taxa de mortalidade do dataset
taxa_mort = ds['Deathrate'] # series

# taxa de mortalidade com desconto
taxa_mort_tenpercent = taxa_mort.apply(tenpercent) # series

# criando dataframe com as duas series
df2 = pd.concat([taxa_mort, taxa_mort_tenpercent], axis=1) #axis=1 -> colunas
df2.columns = ['Taxa Mort', 'Taxa Mort c/ Desconto'] # dando nome às colunas
print(df2)