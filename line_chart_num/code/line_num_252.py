
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 500, 5000],
        [2002, 700, 4500],
        [2003, 1000, 4000],
        [2004, 1500, 3500],
        [2005, 2000, 3000],
        [2006, 2500, 2500],
        [2007, 3000, 2000],
        [2008, 3500, 1500],
        [2009, 4000, 1000]]

x = np.array(data)[:,0]
renewable_energy = np.array(data)[:,1]
non_renewable_energy = np.array(data)[:,2]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(x, renewable_energy, color='green', label='Renewable Energy', linewidth=3)
ax.plot(x, non_renewable_energy, color='red', label='Non-Renewable Energy', linewidth=3)

ax.set_title('Comparison of Renewable and Non-Renewable Energy Consumption in the USA from 2001-2009')
ax.set_xlabel('Year')
ax.set_ylabel('Energy (kWh)')

ax.legend(loc='upper left', fontsize='large')

ax.set_xticks(x)
ax.set_xticklabels(x, fontsize='large', rotation=90, wrap=True)

for i,j in zip(x, renewable_energy):
    ax.annotate(str(j), xy=(i, j+100), fontsize='large')
for i,j in zip(x, non_renewable_energy):
    ax.annotate(str(j), xy=(i, j+100), fontsize='large')

fig.tight_layout()
plt.savefig('line chart/png/260.png', dpi=300)
plt.clf()