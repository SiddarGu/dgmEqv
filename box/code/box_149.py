# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Sculpting", "Painting", "Literature", "Film", "Music"]
box_data = [[10, 20, 30, 40, 60], [12, 22, 32, 42, 52], [8, 16, 24, 32, 40], [16, 32, 48, 64, 80], [14, 28, 42, 56, 70]]
outliers = [[], [80, 100], [4, 60], [120], [90, 110]]

# Setting up the figure and axes
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111)

# Creating the boxplot
bp = ax.boxplot(box_data, whis=1.5, vert=0, patch_artist=True, widths=0.75)

# Coloring the boxes in the boxplot
colors = ["#D70060", "#FF8C00", "#FFEA00", "#004DFF", "#6F00D2"]
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

# Iterating over the outliers
for i, outlier in enumerate(outliers):
    ax.plot(outlier, [i + 1] * len(outlier), "o", color="black")

# Setting grid, labels, and title
ax.set_yticklabels(categories)
ax.set_xlabel('Creation Time (Hours)')
ax.set_title('Creation Time Distribution Based on Art Genre (2021)')
ax.grid(True)

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/80_202312270030.png', dpi=300)

# Clearing the current figure
plt.clf()
