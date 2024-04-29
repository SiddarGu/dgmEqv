
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(20,10))
ax = plt.subplot()

region = ['North America','South America','Europe','Asia']
hospitals = [200,100,150,180]
doctors = [15000,10000,12000,13000]
nurses = [30000,25000,27000,29000]

x = np.arange(len(region))
width = 0.2

ax.bar(x-width, hospitals, width=width, label='Hospitals')
ax.bar(x, doctors, width=width, label='Doctors')
ax.bar(x+width, nurses, width=width, label='Nurses')

plt.xticks(x, region)
plt.title('Healthcare resources in four regions in 2021')
ax.set_ylabel('Number')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/189.png')

plt.clf()