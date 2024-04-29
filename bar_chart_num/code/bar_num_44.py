
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

regions = ['Europe', 'Asia', 'Africa', 'Oceania']
hotels = [145, 180, 120, 130]
restaurants = [400, 500, 350, 380]
tourist_attractions = [600, 700, 500, 570]

ax.set_title('Number of hotels, restaurants and tourist attractions in four regions in 2021')

bar1 = ax.bar(regions, hotels, bottom=np.add(restaurants,tourist_attractions), label='Hotels')
bar2 = ax.bar(regions, restaurants, bottom=tourist_attractions, label='Restaurants')
bar3 = ax.bar(regions, tourist_attractions, label='Tourist Attractions')

ax.set_xticks(regions)
ax.set_yticks(np.arange(0, 1201, 100))
ax.set_ylabel('Number of Hotels/Restaurants/Tourist Attractions')
ax.legend()

for i, rect in enumerate(bar1):
    ax.annotate(hotels[i], xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', rotation=45)
for i, rect in enumerate(bar2):
    ax.annotate(restaurants[i], xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', rotation=45)
for i, rect in enumerate(bar3):
    ax.annotate(tourist_attractions[i], xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', rotation=45)

plt.tight_layout()
plt.savefig('Bar Chart/png/531.png')
plt.clf()