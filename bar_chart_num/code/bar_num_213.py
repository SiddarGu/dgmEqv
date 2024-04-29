
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(10,5))

# set variables
countries = ['USA', 'UK', 'Germany', 'France']
renewable_energy = [20, 25, 30, 35]
air_pollution = [30, 35, 40, 45]
water_pollution = [40, 45, 50, 55]

# draw figure
ax = plt.subplot()
ax.bar(countries, renewable_energy, label='Renewable Energy', bottom=[i+j+k for i,j,k in zip(air_pollution, water_pollution, [0,0,0,0])])
ax.bar(countries, air_pollution, label='Air Pollution', bottom=water_pollution)
ax.bar(countries, water_pollution, label='Water Pollution')

# add title and labels
plt.title('Environmental sustainability comparison of four countries in 2021', fontsize=20)
plt.xlabel('Country', fontsize=15)
plt.ylabel('Percentage (%)', fontsize=15)

# add legend
ax.legend(loc='upper right')

# add value labels
rects = ax.patches
for rect, label in zip(rects, renewable_energy):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom', fontsize=15)
rects = ax.patches
for rect, label in zip(rects, air_pollution):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom', fontsize=15)
rects = ax.patches
for rect, label in zip(rects, water_pollution):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom', fontsize=15)

# prevent x-ticks being interpolated
plt.xticks(np.arange(len(countries)), countries)

# resize image
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/554.png')

# clear figure
plt.clf()