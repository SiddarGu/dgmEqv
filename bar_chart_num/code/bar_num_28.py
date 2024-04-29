
import matplotlib.pyplot as plt
import numpy as np

Region = ('North America', 'South America', 'Europe', 'Asia')
Restaurants = (400, 300, 500, 700)
Fast_Food = (500, 700, 400, 600)
Cafes = (200, 250, 350, 400)

x = np.arange(len(Region))
width = 0.20

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.bar(x - width, Restaurants, width, label='Restaurants', color='r')
ax.bar(x, Fast_Food, width, label='Fast Food', color='b')
ax.bar(x + width, Cafes, width, label='Cafes', color='g')

plt.title('Number of Restaurants, Fast Food Outlets and Cafes by Region in 2021')
plt.xticks(x, Region, rotation='vertical')
plt.legend(loc='best', bbox_to_anchor=(1, 0.5))

for i in range(len(Region)):
    ax.annotate(str(Restaurants[i]), xy=(x[i] - width + 0.03, Restaurants[i]), va='center')
    ax.annotate(str(Fast_Food[i]), xy=(x[i] + 0.03, Fast_Food[i]), va='center')
    ax.annotate(str(Cafes[i]), xy=(x[i] + width + 0.03, Cafes[i]), va='center')

plt.tight_layout()
plt.savefig(r'Bar Chart/png/383.png', bbox_inches='tight')
plt.clf()