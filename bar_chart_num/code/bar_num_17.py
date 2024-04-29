

import matplotlib.pyplot as plt
import numpy as np

region = np.array(['North America', 'South America', 'Europe', 'Asia'])
electric_vehicles = np.array([500, 400, 600, 700])
renewable_energy = np.array([3000, 2500, 3500, 3750])
recycling = np.array([4500, 4000, 4750, 5000])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(region, electric_vehicles, bottom=renewable_energy+recycling, label='Electric Vehicles')
ax.bar(region, renewable_energy, bottom=recycling, label='Renewable Energy')
ax.bar(region, recycling, label='Recycling')

for i, v in enumerate(electric_vehicles):
    ax.text(i-.2, v/2+renewable_energy[i]+recycling[i], str(v), fontsize=10, color='black')
for i, v in enumerate(renewable_energy):
    ax.text(i-.2, v/2+recycling[i], str(v), fontsize=10, color='black')
for i, v in enumerate(recycling):
    ax.text(i-.2, v/2, str(v), fontsize=10, color='black')

ax.set_xlabel('Region')
ax.set_ylabel('Number')
ax.set_title('Number of electric vehicles, renewable energy, and recycling in four regions in 2021')
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region)
ax.legend()

plt.tight_layout()
plt.savefig('Bar Chart/png/326.png')
plt.clf()