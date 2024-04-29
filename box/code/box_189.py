

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[20, 40, 60, 80, 100], [25, 45, 65, 85, 105], [30, 50, 70, 90, 110], [15, 35, 55, 75, 95], [10, 30, 50, 70, 90]]
outliers = [[], [150], [20, 160], [105, 115], [130]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

# Draw background grids
ax.yaxis.grid(True)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_ylabel('Duration (Minutes)')
ax.set_xticklabels(['Basketball', 'Football', 'Soccer', 'Baseball', 'Hockey'])
ax.set_title('Event Duration Distribution in Sports and Entertainment (2020)')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/33_202312270030.png')

# Clear the current image state
plt.close(fig)