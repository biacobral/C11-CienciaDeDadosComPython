import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str,encoding='utf-8')

print(ds[0,:])

# 1. Porcentagem de 'Success'
print("1.")
ds_status_mission = ds[1:,7]

ds_status_mission_success = np.sum(ds_status_mission=='Success')
print(f"{(ds_status_mission_success/len(ds_status_mission))*100}%")

# 2. Media de gastos de missão
print("2.")
ds_cost = ds[1:,6]
ds_cost = ds_cost.astype(float)
ds_cost_not_zero = ds_cost[ds_cost>0]

print(f"{np.mean(ds_cost_not_zero)}")

# 3. Missões pelos EUA
print("3.")
ds_location = ds[1:,2]
ds_location_EUA = np.char.find(ds_location, "USA")>=0

print(np.sum(ds_location_EUA==True))

# 4. SpaceX
print("4.")
ds_company = ds[1:,1]
ds_company_spacex = np.char.find(ds_company, "SpaceX")>=0
ds_cost_spacex = ds_cost[ds_company_spacex]

print(np.max(ds_cost_spacex))

# 5. Quantidade de missões por empresa
print("5.")
ds_companies, cont = np.unique(ds_company, return_counts=True)
for i in range (len(cont)):
    print(f"{ds_companies[i]}: {cont[i]}")