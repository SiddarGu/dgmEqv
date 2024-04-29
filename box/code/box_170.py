

import matplotlib.pyplot as plt
import numpy as np

# Restructure data into two 2D lists
data = [[3, 5, 7.5, 10, 15], [5, 10, 15, 20, 30], [7, 12, 17, 25, 35], [20, 35, 50, 70, 100], [3, 7, 10, 15, 20]]
outliers = [[], [50], [0.25, 45], [150], [25]]

# Plot data with box plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o')

# Add background grids
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Set labels
ax.set_xticklabels(['Fast Food', 'Cafe', 'Casual Dining', 'Fine Dining', 'Bakery'])
ax.set_ylabel('Price (USD)')
ax.set_title('Average Meal Price Range in Different Types of Restaurants (2022)')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/42_202312251608.png')

# Clear the current image state
plt.clf()