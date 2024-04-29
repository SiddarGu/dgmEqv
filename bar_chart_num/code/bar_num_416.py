
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    ["North America", 2400, 20],
    ["South America", 3200, 30],
    ["Europe", 2700, 35],
    ["Asia", 4200, 15]
])

x = np.arange(data.shape[0])
co2 = data[:,1].astype(int)
renewable = data[:,2].astype(int)

plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.bar(x, co2, label='CO2 Emission(tonnes)', bottom=renewable)
ax.bar(x, renewable, label='Renewable Energy(%)')
ax.xaxis.set_ticks(x)
ax.set_xticklabels(data[:,0], fontsize=10)

for i, v in enumerate(co2):
    ax.text(i - 0.15, v/2 + renewable[i], str(v), color='white', fontweight='bold', fontsize=10)

for i, v in enumerate(renewable):
    ax.text(i - 0.15, v/2, str(v), color='white', fontweight='bold', fontsize=10)

plt.title('CO2 Emission and Renewable Energy Usage in Four Continents in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/168.png')
plt.clf()