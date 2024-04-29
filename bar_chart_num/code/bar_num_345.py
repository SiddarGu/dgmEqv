
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
ax = plt.subplot(111)

region = ['North America', 'South America', 'Europe', 'Asia']
hotels = [2000, 2500, 3000, 3500]
restaurants = [3000, 3500, 4000, 4500]
tourists = [300000, 250000, 400000, 500000]

x = np.arange(len(region))  # the label locations
width = 0.25  # the width of the bars

ax.bar(x - width, hotels, width, label='Hotels')
ax.bar(x, restaurants, width, label='Restaurants')
ax.bar(x + width, tourists, width, label='Tourists')
ax.set_ylabel('Number of People')
ax.set_title('Number of Hotels, Restaurants, and Tourists in different regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region)
ax.legend()

pos = range(len(hotels))
values = [hotels[i] + restaurants[i] + tourists[i] for i in pos]

for i, v in enumerate(values):
    ax.text(i-.1, v+5000, str(v), color='black', fontsize=14)

plt.tight_layout()
plt.savefig('Bar Chart/png/593.png')

plt.clf()