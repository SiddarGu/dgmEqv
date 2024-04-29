import matplotlib.pyplot as plt
import numpy as np

# data
categories = ['Electronics', 'Furniture', 'Automobiles', 'Clothing', 'Food']
values = [[20,50,70,90,110], [10,40,60,80,100], [30,60,90,120,150], [5,25,45,65,85], [15,35,55,75,95]]
outliers = [[150], [2,140], [5,180], [95,105,125], [130]]

# creating figure and subplot
fig = plt.figure(figsize=(16,10))
ax = fig.add_subplot(111)

# plotting boxplot with custom parameters
bp = ax.boxplot(values, widths=0.4, notch=True, vert=True, patch_artist=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'salmon']

for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

# plotting outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# mirroring axes and activating grid
ax.grid(True)
ax.set_yticks(np.arange(0,200,10))
ax.set_yticklabels(np.arange(0,200,10))
ax.set_xticklabels(categories, rotation=30, ha='right')

# setting labels and title
ax.set_xlabel('Product Type')
ax.set_ylabel('Production Time (Days)')
plt.title('Production Time Distribution in Different Manufacturing Sectors (2022)')

# saving figure to specified path
plt.tight_layout()  
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/182_202312310058.png')

# clearing the current figure
plt.clf()
