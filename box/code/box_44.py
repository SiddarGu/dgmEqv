
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists.
data_list1 = [[2, 7, 14, 21, 30], [10, 30, 60, 90, 120], [200, 300, 400, 500, 600], [120, 240, 360, 480, 600], [15, 30, 45, 60, 90]]
data_list2 = [[],[180],[750],[720],[180]]
line_labels = ['Fresh Produce', 'Dairy Product', 'Canned Foods', 'Frozen Foods', 'Ready Meals']
# Plot the data with the type of box plot.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.boxplot(data_list1, whis=1.5)

# Set labels and titles
ax.set_xlabel('Food Type')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Shelf Life (Days)')
ax.set_title('Shelf Life Distribution of Different Types of Food Items')

# Use enumerate to iterate through the outliers list
for i, outlier in enumerate(data_list2):
    if len(outlier) != 0:
        # Plot outliers manually using ax.plot for each category
        ax.plot([i + 1] * len(outlier), outlier, 'r.')

# Drawing techniques such as background grids
ax.grid(True, linestyle='-.')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/39_202312270030.png')

# Clear the current image state
plt.clf()