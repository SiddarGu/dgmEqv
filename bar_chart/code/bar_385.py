
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

countries = ['USA','UK','Germany','France']
production = [3000, 2500, 2000, 1500]
consumption = [5000, 4500, 4000, 3500]

ax.bar(countries, production, label='Electricity Production(GWh)', color='#444444', bottom=consumption)
ax.bar(countries, consumption, label='Consumption(GWh)', color='#999999')

ax.set_title('Electricity Production and Consumption in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('GWh')
ax.legend()

plt.xticks(np.arange(len(countries)), countries, rotation=45, ha="right")

plt.tight_layout()
plt.savefig('bar chart/png/234.png')
plt.clf()