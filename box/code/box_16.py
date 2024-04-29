
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[2.5, 3.7, 5.0, 6.2, 7.5],
        [1.2, 1.7, 2.2, 2.7, 3.2],
        [1.0, 1.5, 2.0, 2.5, 3.0],
        [0.8, 1.2, 1.7, 2.2, 2.7],
        [0.5, 1.0, 1.5, 2.0, 2.5]]
outliers = [[], [4.6], [0.02, 4.3, 6.6], [3.6, 5.5], [4.8]]
line_labels = ['Facebook', 'Twitter', 'Instagram', 'Snapchat', 'LinkedIn']

# Create figure before plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data with the type of box plot
ax.boxplot(data, whis=1.5)

# Outliers are plotted manually using ax.plot for each category
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', color='#000000')

# Drawing techniques such as background grids can be used
ax.yaxis.grid(True)

# The title of y-axis should be given with its unit
ax.set_ylabel('Users (Million)')
ax.set_xticklabels(line_labels)

# The title of the figure should be Social Media User Distribution in 2021
plt.title('Social Media User Distribution in 2021')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/8_202312251520.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/8_202312251520.png')

# Clear the current image state at the end of the code
plt.clf()