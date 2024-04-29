

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[10, 50, 100, 150, 200], [20, 60, 120, 180, 240], [40, 100, 160, 220, 280], [30, 80, 130, 180, 230], [50, 110, 170, 230, 290]]
outliers = [[], [310], [20, 350], [280, 320], [50]]
line_labels = ['Education', 'Health Care', 'Infrastructure', 'Social Services', 'Defense']

# Plot the data with the type of box plot
fig = plt.figure() 
ax = fig.add_subplot(111) 
ax.boxplot(data, whis=1.5)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'o', color='red')

# Add title, labels, grid and save the image
ax.set_title('Government Budget Distribution in Public Sectors (2021)')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Budget (USD)')
ax.yaxis.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/40_202312270030.png')

plt.clf()