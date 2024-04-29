
import matplotlib.pyplot as plt
import numpy as np

region = ['Asia', 'North America', 'South America', 'Europe']
crops = [5000, 6000, 7000, 8000]
livestock = [3000, 4000, 5000, 6000]

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region, fontsize=15, rotation=30, wrap=True)
ax.bar(region, crops, bottom=livestock, width=0.4, label='Crops', color='#63f7b4')
ax.bar(region, livestock, width=0.4, label='Livestock', color='#ff9f43')
plt.title('Production of crops and livestock in four regions in 2021', fontsize=20)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('bar chart/png/431.png')
plt.clf()