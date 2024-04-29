

import matplotlib.pyplot as plt
import numpy as np

# restructure the data into two 2D lists
data = [[1000, 3000, 5000, 7000, 10000],
        [2500, 4000, 5500, 7500, 9000],
        [2000, 3500, 5000, 7500, 9500],
        [1500, 3000, 4500, 7000, 8000],
        [1000, 4000, 6000, 8000, 10000]]
outliers = [[], [12000], [1000, 14000], [12000, 13000], [11500]]

# plot the data with the type of box plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5, labels=['Stadium A', 'Stadium B', 'Stadium C', 'Stadium D', 'Stadium E'])
ax.set_title('Capacity Distribution in Sports Venues in 2021')
ax.set_ylabel('Capacity (People)')

# plot the outlier
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i + 1), outlier, 'ro')

# drawing techniques
ax.grid(linestyle='--')

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/10_202312270030.png')

# clear the current image state
plt.clf()