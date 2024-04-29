
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Crops = [4000,3500,4500,4700]
Livestock = [3000,3500,4000,3700]
Fruits = [5000,4500,5000,4800]

x = np.arange(len(Country))
width = 0.2

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x-width, Crops, width, label='Crops', color='#FFC300')
ax.bar(x, Livestock, width, label='Livestock', color='#58508D')
ax.bar(x+width, Fruits, width, label='Fruits', color='#EE5A24')

ax.set_ylabel('Tons', fontsize=15)
ax.set_title('Agricultural production in four countries in 2021', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(Country, fontsize=15, rotation=45, ha='right', wrap=True)
ax.legend(fontsize=15)

plt.tight_layout()
plt.savefig('bar chart/png/263.png')

plt.clf()