
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[50, 90, 150, 210, 270], [60, 100, 160, 220, 280], [55, 95, 155, 215, 275], [65, 105, 165, 225, 285], [70, 110, 170, 230, 290]]
outliers = [[], [320], [20, 310], [5, 320], []]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot the data with the type of box plot
ax.boxplot(data, whis=1.5, showmeans=True, meanline=True, labels=['Provider A', 'Provider B', 'Provider C', 'Provider D', 'Provider E'])

# Manually plot outliers with ax.plot
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        x_outlier = np.array([i + 1] * len(outlier))
        y_outlier = np.array(outlier)
        ax.plot(x_outlier, y_outlier, 'ro', ms=4)

# Drawing techniques such as background grids can be used
ax.grid(axis='y', linestyle='-', linewidth=0.5)

# The title of y-axis should be given with its unit
ax.set_ylabel('Cost(USD)')

# The title of the figure
ax.set_title('Energy Cost Distribution in Utility Providers (2021)')

# Automatically resize the image by tight_layout()
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/11_202312251608.png')

# Clean up the current image state
plt.clf()