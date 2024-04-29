
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

region = ['North America', 'South America', 'Europe', 'Asia']
crops = [900, 800, 700, 600]
livestock = [700, 600, 500, 400]

rects1 = ax.bar(region, crops, label='Crops', width=0.4, color='#f9a602')
rects2 = ax.bar(np.arange(len(region))+0.4, livestock, label='Livestock', width=0.4, color='#ee7f2d')

ax.set_title('Crop and livestock production in four regions in 2021')
ax.set_ylabel('Production (tons)')
ax.set_xticks(np.arange(len(region))+0.4/2)
ax.set_xticklabels(region, rotation=45, ha='right', wrap=True)
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('bar chart/png/483.png')
plt.clf()