import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

df_roscosmos = df[df['Company Name'] == 'Roscosmos']

count_success = len(df_roscosmos[df_roscosmos['Status Mission'] == 'Success'])
count_failure = len(df_roscosmos[df_roscosmos['Status Mission'] == 'Failure'])
count_partial = len(df_roscosmos) - count_success - count_failure


plt.pie([count_success, count_failure, count_partial], labels=['Success', 'Failure', 'Partial Failure'], autopct='%1.1f%%')
plt.show()