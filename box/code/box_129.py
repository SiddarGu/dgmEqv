import matplotlib.pyplot as plt
import numpy as np

# restructure data
categories = ["Banking", "Insurance", "Investment", "Retail Trade", "Health Services"]
data = [[30,90,150,210,300], [45,75,130,190,280], [35,80,120,200,290], [20,60,100,150,200], [50,100,170,220,280]]
outliers = [[], [310], [10, 320], [230], [300]]

# create figure
fig, ax = plt.subplots(figsize=(10,6))

# plot the boxplot
bp = ax.boxplot(data, whis=1.5, widths=0.3, patch_artist=True, vert=0)

# plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "o", color = 'red', markersize = 5)

# customize the boxplot
colors = ['blue', 'green', 'pink', 'cyan', 'magenta']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for median in bp['medians']:
    median.set(color ='red',
               linewidth = 2)

# set the grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# set the title
plt.title("Q1 Revenue Distribution in Different Industry Sectors (2020-2021)")

# set the y-axis label
plt.ylabel("Revenue (in $ billions)")

# set the x-axis labels
ax.set_xticklabels(categories, rotation=45)

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/82_202312270030.png')

# clear the current image
plt.clf()
