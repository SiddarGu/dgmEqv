
import matplotlib.pyplot as plt
import numpy as np

data = [[10, 25, 35, 45, 60],
        [20, 30, 40, 50, 70],
        [15, 25, 30, 40, 60],
        [12, 20, 30, 40, 50],
        [15, 20, 30, 35, 45]]

# outliers
outlier = [[], [90], [5, 75], [65], [50, 60]]

# create figure and subplot
fig, ax = plt.subplots(figsize=(10, 8))

# plot box plot with given data
ax.boxplot(data, whis=1.5, labels=['McDonald\'s', 'KFC', 'Pizza Hut', 'Burger King', 'Subway'])

# plot outliers if any
for i, o in enumerate(outlier):
    if len(o) > 0:
        x = np.repeat(i + 1, len(o))
        ax.plot(x, o, 'ro')

# set title
ax.set_title('Delivery Time Distribution of Popular Restaurants in 2021')

# set y label
ax.set_ylabel('Delivery Time (Minutes)')

# draw background grids
ax.grid(True, axis='y', ls='--', lw='.5')

# resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/7_202312270030.png')

# clear the current image state
plt.clf()