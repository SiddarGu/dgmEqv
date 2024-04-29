
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, [1000, 1200, 900, 1100], width, label='Restaurants', color = '#F08080')
rects2 = ax.bar(x, [1500, 1200, 1400, 1000], width, label='Groceries', color = '#FFC0CB')
rects3 = ax.bar(x + width, [500, 450, 400, 600], width, label='Cafes', color = '#BC8F8F')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of outlets')
ax.set_title('Number of food and beverage outlets in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['North America', 'South America', 'Europe', 'Asia'],  rotation=0, wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

plt.tight_layout()
plt.savefig('bar chart/png/329.png')
plt.clf()