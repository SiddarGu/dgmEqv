

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[30, 45, 60, 90, 120],
        [15, 20, 30, 45, 60],
        [10, 15, 20, 30, 45],
        [20, 30, 45, 60, 90],
        [30, 45, 60, 75, 90]]
outliers = [[], [120], [60, 90], [120], [120]]

# Create figure before plotting
fig = plt.figure(figsize=(6, 5))

# Plot the data with the type of box plot
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5)

# Iterate through outlier list and plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, 'ro')

# Drawing techniques such as background grids
ax.grid(True)

# Adjust the label
ax.set_xticklabels(['General\nCheckup', 'Eye\nCheckup', 'Blood\nTest', 'Dental\nCheckup', 'Cardiac\nCheckup'], rotation=45, wrap=True)
ax.set_ylabel('Duration (Minutes)')

# Add title
ax.set_title('Examination Time Distribution in Healthcare Checkups (2021)')

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/25_202312251608.png')

# Clear the figure
plt.clf()