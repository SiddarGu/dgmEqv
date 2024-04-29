
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(7.5,5))

# define data
city = np.array(['Tokyo', 'Bangkok', 'Istanbul', 'Rome'])
hotel = np.array([25, 20, 30, 35])
restaurant = np.array([90, 85, 95, 100])
tourist = np.array([100, 80, 110, 120])

# plot data
x = np.arange(len(city))
width = 0.2

ax = plt.subplot()
ax.bar(x, hotel, width, label='Hotel')
ax.bar(x+width, restaurant, width, label='Restaurant')
ax.bar(x+width*2, tourist, width, label='Tourist Sites')

# set xticks and legend
ax.set_xticks(x+width)
ax.set_xticklabels(city, rotation=45, ha="right", wrap=True)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# set title and labels
plt.title('Number of Hotels, Restaurants and Tourist Sites in four major cities in 2021')
plt.xlabel('City')
plt.ylabel('Number')

# set grid
plt.grid(linestyle='--', alpha=0.3)

# adjust the figure
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/295.png')

# clear state
plt.clf()