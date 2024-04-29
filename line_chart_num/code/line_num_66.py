
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

Month = ['January','February','March','April','May','June','July','August']
Electricity_Consumption = [100,90,110,105,120,110,95,100]
Renewable_Energy_Consumption = [20,25,30,35,40,45,50,55]

plt.figure(figsize=(15, 8))
plt.title('Monthly electricity and renewable energy consumption in the US, 2021')
plt.xticks(range(8), Month, rotation=45)

plt.plot(Electricity_Consumption, label='Electricity Consumption(megawatt-hours)', linestyle='solid', marker='o', color='green')
plt.plot(Renewable_Energy_Consumption, label='Renewable Energy Consumption(megawatt-hours)', linestyle='dashed', marker='^', color='blue')

plt.legend()
plt.grid(True)

for x, y in zip(range(8), Electricity_Consumption):
    plt.text(x, y+1, '%.0f' % y, ha='center', va= 'bottom')
for x, y in zip(range(8), Renewable_Energy_Consumption):
    plt.text(x, y+1, '%.0f' % y, ha='center', va= 'bottom')

plt.tight_layout()
plt.savefig('line chart/png/408.png')
plt.clf()