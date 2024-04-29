
import matplotlib.pyplot as plt
import numpy as np

Country = ('USA','UK','Germany','France')
Renewable_Energy = np.array([25,30,40,55])
Fossil_Fuel = np.array([75,70,60,45])

fig,ax = plt.subplots(figsize=(15,10))
ax.bar(Country, Renewable_Energy, bottom=Fossil_Fuel, align='center', width=0.5, label='Renewable Energy %')
ax.bar(Country, Fossil_Fuel, align='center', width=0.5, label='Fossil Fuel %')

ax.set_title('Renewable and Fossil Fuel Energy Mix in Four Countries in 2021')
ax.set_xticks(Country)
ax.set_xlabel('Country')
ax.set_ylabel('%')
ax.legend(loc='upper left', frameon=False)
ax.set_facecolor('white')
ax.grid(True, axis='y', alpha=0.5)

plt.tight_layout()
plt.savefig('bar chart/png/509.png')
plt.clf()