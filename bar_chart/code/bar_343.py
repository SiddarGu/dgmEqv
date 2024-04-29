
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()

region = ['North America','South America','Europe','Asia']
hotel = [60,70,80,90]
restaurant = [200,250,300,350]

ax.bar(region, hotel, label='Hotel Occupancy Rate(%)', align='center', color='C1', bottom=0)
ax.bar(region, restaurant, label='Restaurant Revenue(million)', align='center', color='C2', bottom=hotel)

ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region, fontsize=14, rotation=45, ha="right", va="top", wrap=True)

ax.set_title('Hospitality and Tourism Performance in Different Regions in 2021', fontsize=20)
ax.legend(loc='upper right', fontsize=14)

plt.tight_layout()
plt.savefig('bar chart/png/424.png')
plt.clf()