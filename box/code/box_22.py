
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
data = [[2.5, 3.3, 4.0, 4.7, 5.0],
        [2.8, 3.6, 4.2, 4.9, 5.2],
        [3.0, 3.7, 4.3, 5.0, 5.4],
        [2.4, 3.2, 3.9, 4.6, 5.1],
        [2.7, 3.5, 4.1, 4.8, 5.3]]

outliers = [[], [4.2], [4.9, 2.3], [1.5, 2.2, 4.4], [5.0]]

# Plot the data
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, patch_artist=True)

# Manually plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        y = outlier
        ax.plot(x, y, 'ro', markerfacecolor='black', alpha=0.6)

# Set x-axis label
ax.set_xticklabels(['Hotel A', 'Hotel B', 'Hotel C', 'Hotel D', 'Hotel E'], rotation=90)

# Set y-axis label
ax.set_ylabel('Rating (Out of 5)')

# Add grid
ax.grid(linestyle='--', alpha=0.6)

# Add title
ax.set_title('Hotel Ratings Distribution in Tourism and Hospitality in 2021')

# Adjust layout automatically
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/27_202312270030.png')

# Clear current image state
plt.clf()