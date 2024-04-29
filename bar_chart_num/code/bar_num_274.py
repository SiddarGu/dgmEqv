
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()

region = ['North America','South America','Europe','Asia']
renewable_energy = [50, 40, 60, 30]
non_renewable_energy = [50, 60, 40, 70]

x = np.arange(len(region)) 

ax.bar(x, renewable_energy, bottom=non_renewable_energy, label='Renewable Energy')
ax.bar(x, non_renewable_energy, label='Non-Renewable Energy')

ax.set_xticks(x)
ax.set_xticklabels(region)
ax.set_title('Percentage of Renewable and Non-Renewable Energy in four regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Energy Percentage')
ax.legend()

for i, v in enumerate(renewable_energy):
    ax.text(i-.2, v/2 + non_renewable_energy[i], str(v)+'%', fontsize=12, color='white', horizontalalignment='center')
for i, v in enumerate(non_renewable_energy):
    ax.text(i+.2, v/2, str(v)+'%', fontsize=12, color='white', horizontalalignment='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/194.png')
plt.clf()