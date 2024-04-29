
import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 3000, 2000, 5000], 
        ['Europe', 3500, 2500, 4500], 
        ['Asia', 4000, 3000, 5500], 
        ['South America', 2000, 1800, 4000]]

region, restaurants, cafes, grocery_stores = zip(*data)

x = np.arange(len(region))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width, restaurants, width, label='Restaurants')
rects2 = ax.bar(x, cafes, width, label='Cafes')
rects3 = ax.bar(x + width, grocery_stores, width, label='Grocery Stores')

ax.set_xticks(x)
ax.set_xticklabels(region, rotation=45, ha='right', wrap=True)
ax.set_title('Number of Food and Beverage Outlets in Four Regions in 2021')
ax.legend()

fig.tight_layout()
plt.savefig('bar chart/png/338.png')
plt.clf()