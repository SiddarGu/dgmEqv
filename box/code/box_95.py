import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    ["Website A",5,10,15,20,30,[]],
    ["Website B",8,12,18,24,32,[48]],
    ["Website C",7,11,17,22,29,[3,35]],
    ["Website D",6,10,14,19,26,[4.5,36]],
    ["Website E",7,13,18,23,31,[41]]
]

# Restructure the data
labels = [item[0] for item in data]
stat_data = [item[1:6] for item in data]
outliers = [item[6] for item in data]

# Create the figure and a subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Create the box plot
bp = ax.boxplot(stat_data, patch_artist=True, notch=True, vert=1, whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#FFA500']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro", markersize = 4)

# Customize the chart
ax.set_title('User Visit Duration Distribution on Different Websites (2021)')
ax.set_xticks(np.arange(1, len(labels) + 1))
ax.set_xticklabels(labels, rotation=45)
ax.set_ylim([-5, 50])
ax.set_ylabel('Duration (in Minutes)')
ax.grid(alpha=0.4)

# Save the image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/165_202312310058.png", dpi=300)
plt.clf()  
