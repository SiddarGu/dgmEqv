import matplotlib.pyplot as plt
import numpy as np

# data
categories = ["Amazon", "eBay", "Alibaba", "Walmart", "Asos"]
data_quantile = [[20, 65, 100, 155, 215], [30, 75, 115, 175, 230], 
                [23, 70, 110, 165, 210], [28, 83, 115, 170, 225], 
                [15, 62, 92, 132, 170]]
data_outliers = [[], [10, 260], [270], [], [12, 220]]

fig = plt.figure(figsize=(10,6))  # larger figure size for clarity
ax = fig.add_subplot(111)

# boxplot with exception of 'whis' customised
ax.boxplot(data_quantile, notch=True, vert=True, patch_artist=True, whis=1.5)

# iterate outlier data using enumerate for index
for i, cat in enumerate(categories):
    y = data_outliers[i]
    if y:  # if list is not empty
        x = [i + 1] * len(y)  # i + 1 because boxplot indexing starts at 1
        ax.plot(x, y, "ro")  # red circle for outliers

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.6)
ax.set_title('Page View Distribution for E-commerce Websites in 2022')
ax.set_xlabel('E-commerce Website')
ax.set_ylabel('Page View (Thousands)')
ax.set_xticklabels(categories,rotation=45)
plt.tight_layout()  # fit subplot in to figure area.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/215_202312310058.png')
plt.clf()  # clear figure after saving
