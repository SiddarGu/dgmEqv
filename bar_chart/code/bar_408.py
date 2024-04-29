
import matplotlib.pyplot as plt
import numpy as np

Country = np.array(['USA','UK','Germany','France'])
Renewable_Energy = np.array([30,35,40,45])
Fossil_Fuel = np.array([70,65,60,55])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

ax.bar(Country, Renewable_Energy, bottom=Fossil_Fuel, label='Renewable_Energy',width=0.4, align='center')
ax.bar(Country, Fossil_Fuel, label='Fossil_Fuel',width=0.4, align='center')

ax.set_title('Percentage of Renewable Energy and Fossil Fuel Use in Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_xticks(Country)
ax.set_ylabel('Percentage(%)')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/48.png')
plt.clf()