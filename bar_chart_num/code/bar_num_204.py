
import matplotlib.pyplot as plt
import numpy as np

region = ['North', 'South', 'East', 'West']
fast_food = [50, 60, 65, 55]
cafes = [30, 40, 35, 45]
bars = [20, 25, 15, 30]

x = np.arange(len(region))
width = 0.25

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x - width, fast_food, width, label='Fast food restaurants', color='#f08080')
ax.bar(x, cafes, width, label='Cafes', color='#87ceeb')
ax.bar(x + width, bars, width, label='Bars', color='#ffa500')

ax.set_ylabel('Number of establishments')
ax.set_title('Number of food and beverage establishments by region in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), 
          fancybox=True, shadow=True, ncol=5)

for i, v in enumerate(fast_food):
    ax.text(x[i] - width/2., v + 0.25, str(v), fontsize=11, color='black')
for i, v in enumerate(cafes):
    ax.text(x[i] + width/2., v + 0.25, str(v), fontsize=11, color='black')
for i, v in enumerate(bars):
    ax.text(x[i] + (width+width/2.), v + 0.25, str(v), fontsize=11, color='black')

plt.tight_layout()
plt.savefig('Bar Chart/png/338.png', bbox_inches='tight', pad_inches=0.2)
plt.clf()