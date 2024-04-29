
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists.
data_list = [[1000, 3000, 5000, 7000, 10000], 
             [1500, 3000, 4500, 6000, 9000], 
             [2000, 4000, 6000, 8000, 12000], 
             [500, 2500, 4000, 6500, 9000], 
             [1500, 3500, 5000, 7000, 10000]]

outlier_list = [[], 
                [12000], 
                [1000, 20000], 
                [15000], 
                [11500]]
line_labels = ['Healthcare', 'Education', 'Infrastructure', 'Welfare', 'Security']

# Plot the data with the type of box plot.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.boxplot(data_list, whis=1.5)

# Plot outliers manually.
for i, outlier in enumerate(outlier_list):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

# Drawing techniques such as background grids can be used
ax.grid(color='gray', linestyle='dashed')

x_range = np.arange(len(line_labels)) + 1
ax.set_xticks(x_range)
ax.set_xticklabels(line_labels)

# Set the title of y-axis.
ax.set_ylabel('Cost (USD)')

# Set the title of figure.
ax.set_title('Program Cost Distribution in Government and Public Policy in 2020')

# Automatically resize the image by tight_layout() before savefig().
fig.tight_layout()

# Save the figure as the specified path.
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2_202312270030.png')

# Clear the current image state.
plt.clf()