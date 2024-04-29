import matplotlib.pyplot as plt
import numpy as np

categories = ['E-commerce', 'Social Media', 'Streaming Services', 'Online Gaming', 'EdTech']
value_lists = [[50, 70, 85, 96, 100], 
               [60, 75, 90, 98, 102], 
               [55, 76, 88, 97, 101], 
               [52, 74, 83, 95, 98], 
               [58, 79, 92, 100, 105]]
outliers_lists = [[], 
                  [55, 115], 
                  [120], 
                  [103, 110], 
                  [47]]

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Box plotting
bp = ax.boxplot(value_lists, whis=1.5, notch=True, patch_artist=True)

# Set the colors of the boxes
colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'thistle']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Outliers plotting
for i, outliers in enumerate(outliers_lists):
    if outliers:
        x = [i + 1] * len(outliers)
        ax.plot(x, outliers, 'ro')

# Adding grid
ax.grid(True)

# Set axes labels and title
ax.set_xticklabels(categories, rotation = 45, ha="right", wrap=True)
ax.set_ylabel('User Experience Score')
ax.set_title('User Experience Score Distribution in Internet Aspects (2022)')

plt.tight_layout()

# Save and show the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/151_202312310058.png')
plt.show()

# clear current image state
plt.clf()
