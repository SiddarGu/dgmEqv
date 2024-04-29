
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists. 
data = [[0.3, 2.5, 4.8, 6.5, 8.0], 
        [0.5, 3.0, 5.2, 7.5, 9.0], 
        [0.7, 3.5, 5.7, 7.9, 10.0], 
        [0.2, 2.0, 4.3, 6.0, 7.5], 
        [0.4, 2.5, 4.6, 6.2, 7.8]]
outliers = [[], [14.0], [0.2, 13.2, 14.0], [12.5, 13.8], [13.0]]

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot the data with the type of box plot.
ax = plt.subplot()
ax.boxplot(data, whis=1.5, showmeans=True)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

# Labels for x-axis
ax.set_xticklabels(['Gallery A', 'Gallery B', 'Gallery C', 'Gallery D', 'Gallery E'])

# Labels for y-axis
ax.set_ylabel('Price (USD)')

# Background grid
ax.grid(linestyle='dotted')

# Figure title
plt.title('Art Piece Price Distribution in Galleries (2021)')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/26_202312251608.png')

# Clear image
plt.clf()