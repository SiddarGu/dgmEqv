

import matplotlib.pyplot as plt
import numpy as np
 
# Restructure the data into 2D lists
data = [[4, 8, 14, 20, 24],
        [7, 11, 17, 23, 28],
        [12, 16, 22, 28, 32],
        [2, 5, 10, 15, 20],
        [6, 10, 16, 22, 26]]

outliers = [[], [35], [1, 45], [30], [35]]
line_labels = ['Shoes', 'Electronics', 'Automobiles', 'Textiles', 'Furniture']
# Plot the data with type of box plot
fig = plt.figure(figsize=(6, 4))

ax = fig.add_subplot(111)
ax.set_title("Production Time Distribution in Manufacturing Industries (2021)")
ax.set_ylabel("Production Time (Hours)")

ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', color='black')

# Set background grids
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_xticklabels(line_labels)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312270030.png")

# Clear the current image state
plt.clf()