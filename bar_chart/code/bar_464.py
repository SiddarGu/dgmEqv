
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
width = 0.2

fig, ax = plt.subplots(figsize = (10,6))
ax.bar(x - width, [20000,22000,18000,21000], width, label = 'Restaurants')
ax.bar(x, [3000,4000,3500,3800], width, label = 'Cafes')
ax.bar(x + width, [500,600,550,650], width, label = 'Bars')

ax.set_ylabel('Number of Establishments')
ax.set_title('Number of Food and Beverage establishments in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['USA','UK','Germany','France'])
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/406.png')
plt.clf()