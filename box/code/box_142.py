

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[1.5, 4.0, 7.5, 12.0, 20.0],
        [2.5, 5.0, 9.5, 14.0, 25.0],
        [5.0, 9.0, 14.0, 20.0, 30.0],
        [3.0, 7.0, 11.0, 16.0, 27.0],
        [2.0, 4.5, 8.0, 12.5, 20.0]]

outliers = [[], [30.0], [1.0, 2.0, 3.0], [35.0], [25.0]]
line_labels = ['Twitter', 'Instagram', 'YouTube', 'Facebook', 'TikTok']

# Create figure before plotting
fig = plt.figure(figsize=(20, 10))

ax = fig.add_subplot(111)
ax.set_title('Viewership Distribution on Popular Social Media Platforms in 2021')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Viewership (Millions)')
ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(list(np.repeat(i + 1, len(outlier))), outlier, 'bx')

# Draw background grids
ax.grid(axis='y', alpha=0.75)

# Resize the image
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/31_202312270030.png')

# Clear the current image state
plt.clf()