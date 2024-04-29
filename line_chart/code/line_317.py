
import matplotlib.pyplot as plt
import numpy as np

# set up data 
year = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
average_price = [500000, 540000, 580000, 600000, 640000, 670000, 700000]
inventory = [20000, 25000, 30000, 35000, 40000, 45000, 50000]

# set up figure
plt.figure(figsize=(15, 8))
ax = plt.subplot()

# plot line chart 
ax.plot(year, average_price, label='Average Price')
ax.plot(year, inventory, label='Inventory')

# set x-ticks and y-label
ax.set_xticks(year)
ax.set_ylabel('Dollar')

# set title
plt.title('Change in average house price and inventory in the US from 2017 to 2023')

# set legend 
ax.legend(loc=2, bbox_to_anchor=(1,1), fontsize='x-large')

# set grid
ax.grid(linestyle='--')

# auto resize the image
plt.tight_layout()

# save image
plt.savefig('line chart/png/69.png')

# clear current image state
plt.clf()