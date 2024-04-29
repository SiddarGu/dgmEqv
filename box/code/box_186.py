

import matplotlib.pyplot as plt
import numpy as np

# restructure data into 2D lists
data = [[5,7.5,9,10.5,12],
        [10,17.5,25,32.5,40],
        [7,12.5,17,22.5,27],
        [25,37.5,50,62.5,75],
        [3,5.5,7,8.5,10]]
outliers = [[], [50], [30,45], [85], [15]]

# create figure and plotting
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot data with box plot
ax.boxplot(data, whis=1.5, labels=["Fast Food", "Diners", "Cafes", "Fine Dining", "Street Food"])

# plot outliers
for i, outlier in enumerate(outliers):
    if len(outlier) != 0:
        ax.plot([i+1]*len(outlier), outlier, "o")

# background grids
ax.yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)

# set y-axis title with unit
ax.set_ylabel("Price ($)", fontsize=14)

# set figure title
ax.set_title("Meal Price Distribution at Different Types of Restaurants in 2021", fontsize=18)

# adjust figure
fig.tight_layout()

# save figure
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/41_202312251608.png")

# clear figure
plt.clf()