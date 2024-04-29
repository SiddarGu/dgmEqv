
import matplotlib.pyplot as plt
import numpy as np

# set data
year = np.array([2001, 2002, 2003, 2004])
grain_prod = np.array([1000, 1200, 1500, 1400])
fruit_prod = np.array([500, 600, 650, 700])
veg_prod = np.array([300, 400, 350, 380])

# set figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# plot
ax.plot(year, grain_prod, label='Grain Production (million tons)', color='blue', linestyle='-', marker='o')
ax.plot(year, fruit_prod, label='Fruit Production (million tons)', color='orange', linestyle='-', marker='o')
ax.plot(year, veg_prod, label='Vegetable Production (million tons)', color='green', linestyle='-', marker='o')

# setting label
ax.set_xlabel('Year')
ax.set_ylabel('Production (million tons)')
ax.set_title('Annual Production of Grains, Fruits and Vegetables in the USA')
ax.legend(loc='best', prop={'size': 10})

# set xticks
ax.set_xticks(year)

# set grid
ax.grid(color='gray', linestyle='-.', linewidth=0.5)

# adjust layout
fig.tight_layout()

# save figure
fig.savefig('line chart/png/255.png', dpi=255)

# clear
plt.cla()