
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
data = [[8000000,7000000,9000000,6000000],[25,30,20,35]]

plt.figure(figsize=(8,5))
ax = plt.subplot(111)
ax.bar(x, data[0], width=0.3, label='CO2 Emission(kg/year)')
ax.bar(x+0.3, data[1], width=0.3, label='Renewable Energy(%)')

ax.set_xticks(x+0.3/2)
ax.set_xticklabels(['North America', 'Europe', 'Asia', 'South America'], rotation=30, ha='right', wrap=True)

plt.title('CO2 emissions and renewable energy usage by region in 2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/238.png')
plt.clf()