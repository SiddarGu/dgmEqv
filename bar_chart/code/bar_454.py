
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
region=['North America','South America','Europe','Asia']
trees=[100,120,150,130]
pollutant=[50,60,70,80]
width=0.35
ax.bar(region,trees,width,label='Number of Trees Planted(thousand)')
ax.bar(region,pollutant,width,bottom=trees,label='Number of Polluting Vehicles Removed(thousand)')
ax.set_title('Number of Trees Planted and Polluting Vehicles Removed in Four Regions in 2021')
ax.set_xticks(region)
ax.set_xticklabels(region, rotation=45, ha='right', rotation_mode="anchor")
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/368.png')
plt.clf()