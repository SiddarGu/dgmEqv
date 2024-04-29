
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))
ax = plt.subplot()

x = np.arange(4)
width = 0.2
ax.bar(x, [700, 600, 650, 750], width, label='Crop A')
ax.bar(x + width, [800, 900, 1000, 900], width, label='Crop B')
ax.bar(x + width*2, [500, 550, 600, 650], width, label='Animal Products')

ax.set_xticks(x + width)
ax.set_xticklabels(['North America', 'South America', 'Europe', 'Asia'], rotation=50, wrap=True)
ax.legend(bbox_to_anchor=(1, 1), loc="upper left")
ax.set_title("Food production of crops and animal products in four regions in 2021")

plt.tight_layout()
plt.savefig('bar chart/png/18.png')
plt.clf()