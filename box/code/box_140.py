

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[4, 6, 7, 8, 10], [3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [5, 7, 9, 11, 13], [3, 5, 6, 7, 9]]
outliers = [[], [14], [1, 14], [15], [15]] 
line_labels = ['Court A', 'Court B', 'Court C', 'Court D', 'Court E']
# Plot the data with the type of box plot
fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5) 

# Manually plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, 'ro')

# Set background grids
ax.grid(True, linestyle='--', which='major',
        color='grey', alpha=.25)
ax.set_axisbelow(True)
x_range = np.arange(len(line_labels)) + 1
ax.set_xticks(x_range)
ax.set_xticklabels(line_labels)

# Set the title of y-axis
ax.set_ylabel("Ruling Time (Hours)")

# Set the title of the figure
ax.set_title('Ruling Time Distribution in Courts (2020)')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2_202312251520.png')

# Clear the current image state
plt.clf()