

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data_list1 = [[2.0,2.7,3.0,3.4,4.0],
              [2.2,2.8,3.2,3.6,4.2],
              [2.4,3.0,3.4,3.8,4.4],
              [2.1,2.6,3.1,3.5,4.1],
              [2.3,2.9,3.3,3.7,4.3]]
data_list2 = [[],
              [4.5],
              [1.2,4.3,4.5],
              [3.9,4.2],
              [4.1]]

# Create figure before plotting
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Plot the data with the type of box plot
ax.boxplot(data_list1, labels=["University A", "University B", "University C", "University D", "University E"], whis=1.5)

# Iterate through the outliers list, which gives both the outlier values and their corresponding category index i
for i, outlier in enumerate(data_list2):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Drawing techniques such as background grids can be used
ax.yaxis.grid(True)

# The title of y-axis should be given with its unit
ax.set_ylabel('GPA (Grade)')

# The title of the figure should be  Academic Performance Distribution in Universities in 2021
ax.set_title('Academic Performance Distribution in Universities in 2021')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/30_202312270030.png')

# Clear the current image state
plt.clf()