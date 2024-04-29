
import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 100, 150, 200], 
        ['Europe', 200, 250, 300], 
        ['Asia', 180, 220, 240], 
        ['South America', 130, 180, 220]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

regions = [data[x][0] for x in range(4)]
hotels = [data[x][1] for x in range(4)]
restaurants = [data[x][2] for x in range(4)]
tourist_attractions = [data[x][3] for x in range(4)]

x = np.arange(len(regions))

ax.bar(x - 0.2, hotels, width=0.2, label='Hotels')
ax.bar(x, restaurants, width=0.2, label='Restaurants')
ax.bar(x + 0.2, tourist_attractions, width=0.2, label='Tourist Attractions')

ax.set_xticks(x)
ax.set_xticklabels(regions, rotation=45, ha='right', wrap=True)

plt.title('Number of Hotels, Restaurants and Tourist Attractions in four regions worldwide in 2021')
plt.legend(bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('bar chart/png/144.png', bbox_inches='tight')

plt.clf()