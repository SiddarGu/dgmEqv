

import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# create data
region = ['North America','South America','Europe','Asia']
restaurants = [200,250,220,230]
supermarkets = [450,500,480,470]
grocery_stores = [100,120,140,150]

# plot data
ax.bar(region, restaurants, label='Restaurants', color='#006699')
ax.bar(region, supermarkets, label='Supermarkets', bottom=restaurants, color='#990000')
ax.bar(region, grocery_stores, label='Grocery Stores', bottom=np.array(restaurants)+np.array(supermarkets), color='#339966')

# set ticks
ax.set_xticks(region)

# set x-axis label
ax.set_xlabel('Region', fontsize=14)

# set y-axis label
ax.set_ylabel('Number of food providers', fontsize=14)

# set title
ax.set_title('Number of food providers in four regions in 2021', fontsize=16)

# show legend
ax.legend(facecolor='white', framealpha=1)

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/36.png')

# clear figure
plt.clf()