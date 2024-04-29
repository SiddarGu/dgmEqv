
import numpy as np
import matplotlib.pyplot as plt

# Restructure the data into two 2D lists.
data = [[15, 25, 35, 45, 60], [30, 50, 65, 80, 100], [20, 35, 50, 70, 90], [45, 60, 75, 90, 120], [60, 80, 95, 110, 140]]
outliers = [[], [120], [4, 120], [130], [150]]

# Create figure before plotting
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

# Plot the data with the type of box plot
ax.boxplot(data, whis=1.5, showmeans=True, meanline=True,
           labels=['Phone Interview', 'In-Person Interview', 'Remote Interview', 'Group Interview', 'Panel Interview'])

# Iterate through the outliers list
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, "o", color="k")

# Drawing techniques such as background grids
ax.yaxis.grid(True, linestyle='-', color='lightgrey', alpha=0.5)

# The title of y-axis should be given with its unit
ax.set_ylabel('Time (Minutes)')

# The title of the figure
ax.set_title('Employee Interview Duration Distribution in 2020')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/1_202312251520.png')

# Clear the current image state at the end of the code
plt.clf()