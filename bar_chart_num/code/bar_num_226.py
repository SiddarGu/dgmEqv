
import matplotlib.pyplot as plt

region = ['North America', 'South America', 'Europe', 'Asia']
fast_food = [150, 200, 180, 220]
restaurants = [200, 250, 220, 270]
cafes = [100, 150, 130, 160]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(region, fast_food, label='Fast Food', color='#FFAA00', bottom=restaurants)
ax.bar(region, restaurants, label='Restaurants', color='#FF4444')
ax.bar(region, cafes, label='Cafes', color='#00AA00')
ax.set_title('Number of Food and Beverage Outlets in Four Regions in 2021')
ax.set_xticklabels(region, rotation='horizontal', wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fancybox=True, shadow=True)
for i in range(len(region)):
    ax.annotate(str(fast_food[i]), xy=(i, restaurants[i]+fast_food[i]/2), ha='center', va='center')
    ax.annotate(str(restaurants[i]), xy=(i, restaurants[i]/2), ha='center', va='center')
    ax.annotate(str(cafes[i]), xy=(i, cafes[i]/2), ha='center', va='center')
plt.tight_layout()
plt.savefig('Bar Chart/png/433.png')
plt.clf()