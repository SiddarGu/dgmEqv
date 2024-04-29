
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK', 'Germany', 'France']
fast_food = [5000, 4500, 4000, 3500]
cafes = [3000, 3500, 3700, 4000]
restaurants = [7000, 6000, 5500, 5000]

x = np.arange(len(country))
width = 0.25 

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(x - width, fast_food, width=width, label='Fast Food Outlets', color='#FFCE54', align='center')
ax.bar(x, cafes, width=width, label='Cafes', color='#41B6E6', align='center')
ax.bar(x + width, restaurants, width=width, label='Restaurants', color='#FE9929', align='center')
ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
ax.set_ylabel('Number of Outlets')
ax.set_title('Food and beverage industry outlets in four countries in 2021')
ax.grid(color='#D9D9D9', linestyle='--', linewidth=1)

for i, v in enumerate(fast_food):
    ax.text(i - width + 0.1, v + 100, str(v), color='#FFCE54')
for i, v in enumerate(cafes):
    ax.text(i + 0.1, v + 100, str(v), color='#41B6E6')
for i, v in enumerate(restaurants):
    ax.text(i + width + 0.1, v + 100, str(v), color='#FE9929')

plt.tight_layout()
plt.savefig('Bar Chart/png/278.png')
plt.clf()