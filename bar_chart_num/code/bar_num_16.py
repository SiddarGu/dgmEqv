
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(['North America', 'Europe', 'Asia', 'South America'], [20000, 25000, 30000, 20000], label='Restaurants',color='#f9a602')
ax.bar(['North America', 'Europe', 'Asia', 'South America'], [15000, 20000, 25000, 15000], bottom=[20000, 25000, 30000, 20000], label='Cafes',color='#e6005c')
ax.bar(['North America', 'Europe', 'Asia', 'South America'], [6000, 10000, 15000, 10000], bottom=[35000, 45000, 55000, 35000], label='Bars',color='#00aec7')
ax.set_title('Number of restaurants, cafes and bars in four different regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Number of outlets')
ax.legend(loc='upper left')
ax.set_xticks(['North America', 'Europe', 'Asia', 'South America'])
for i in range(4):
    ax.annotate(str(ax.patches[i].get_height()), (ax.patches[i].get_x() + 0.25, ax.patches[i].get_height() + 200))
    ax.annotate(str(ax.patches[i+4].get_height()), (ax.patches[i+4].get_x() + 0.25, ax.patches[i+4].get_height() + ax.patches[i].get_height() + 200))
    ax.annotate(str(ax.patches[i+8].get_height()), (ax.patches[i+8].get_x() + 0.25, ax.patches[i+8].get_height() + ax.patches[i+4].get_height() + ax.patches[i].get_height() + 200))
plt.tight_layout()
plt.savefig('Bar Chart/png/329.png')
plt.clf()