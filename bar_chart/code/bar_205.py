
import matplotlib.pyplot as plt
import numpy as np

Region = ['East Asia', 'North America', 'South America','Europe']
Carbon_emissions = [1400, 2000, 1000, 1200]
Renewable_energy = [14, 20, 10, 16]

plt.figure(figsize=(20,10))
ax = plt.subplot()
ax.bar(Region, Carbon_emissions, label='Carbon emissions', width=0.5, color='b')
ax.bar(Region, Renewable_energy, label='Renewable energy', bottom=Carbon_emissions, width=0.5, color='g')
plt.xticks(np.arange(len(Region)), Region, rotation=45, ha='right')
plt.title('Carbon emissions and renewable energy usage in four regions in 2021')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/179.png')
plt.clf()