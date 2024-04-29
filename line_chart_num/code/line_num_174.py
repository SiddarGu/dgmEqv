

import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(10, 8))

# set data
year = np.array([2020, 2021, 2022, 2023])
grocery = np.array([1000, 1500, 1300, 1200])
restaurant = np.array([800, 900, 1100, 1400])
food_delivery = np.array([500, 700, 900, 1100])

# create line chart
ax = plt.subplot()
plt.plot(year, grocery, label='Grocery', color='#8F9BFF')
plt.plot(year, restaurant, label='Restaurant', color='#FFE489')
plt.plot(year, food_delivery, label='Food Delivery', color='#BD9BFF')

# set xticks to prevent interpolation
plt.xticks(year)

# add legend
ax.legend(loc='best', frameon=False)

# add title
plt.title("Food Industry Sales Growth From 2020 to 2023")

# add grid
plt.grid(linestyle='--')

# label each data point
for a, b in zip(year, grocery):
    plt.annotate(str(b), xy=(a, b+50), ha='center')

for a, b in zip(year, restaurant):
    plt.annotate(str(b), xy=(a, b+50), ha='center')

for a, b in zip(year, food_delivery):
    plt.annotate(str(b), xy=(a, b+50), ha='center')

# auto resize the image
plt.tight_layout()

# save chart
plt.savefig('line chart/png/248.png')

# clear current image state
plt.clf()