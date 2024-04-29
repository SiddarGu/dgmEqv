
import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 80, 20],
        ['South America', 70, 25],
        ['Europe', 60, 30],
        ['Asia', 90, 15]]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

region = [i[0] for i in data]
CO2_emissions = [i[1] for i in data]
Renewable_Energy = [i[2] for i in data]

x_pos = np.arange(len(region))
width = 0.35

ax.bar(x_pos, CO2_emissions, width, label='CO2 emissions(thousand kg/year)', color='green')
ax.bar(x_pos, Renewable_Energy, width, label='Renewable Energy(%)', bottom=CO2_emissions, color='red')

ax.set_title('CO2 emissions and renewable energy use in four regions in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(region)

plt.legend(loc='upper left')
plt.tight_layout()

for i, v in enumerate(CO2_emissions):
    ax.text(i-0.2, v+7000, str(v), color='green', fontweight='bold')
for i, v in enumerate(Renewable_Energy):
    ax.text(i-0.2, v+CO2_emissions[i]+7000, str(v), color='red', fontweight='bold')

plt.savefig('bar_255.png')
plt.clf()