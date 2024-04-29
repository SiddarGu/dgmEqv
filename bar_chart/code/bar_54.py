
import matplotlib.pyplot as plt
import numpy as np

labels=['USA','UK','Germany','France']
fast_food_restaurants=[1500,900,1000,1100]
cafes=[800,500,700,600]
bars=[450,600,400,570]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(8,8))
rects1 = ax.bar(x - width, fast_food_restaurants, width, label='Fast Food Restaurants')
rects2 = ax.bar(x, cafes, width, label='Cafes')
rects3 = ax.bar(x + width, bars, width, label='Bars')

ax.set_ylabel('Number of Restaurants')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend(bbox_to_anchor=(1, 1))
ax.set_title('Number of Fast Food Restaurants, Cafes and Bars in four countries in 2021')

fig.tight_layout()
plt.savefig('bar chart/png/251.png')
plt.clf()