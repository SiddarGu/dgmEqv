

import matplotlib.pyplot as plt
import numpy as np

consumer_product = ["Smartphone", "Tablet", "Smartwatch", "Smart Speaker", "Laptop"]
min_price = [50, 100, 30, 20, 500]
first_quartile = [200, 300, 150, 50, 800]
median_price = [350, 450, 250, 100, 1000]
third_quartile = [500, 600, 350, 150, 1200]
max_price = [750, 900, 400, 200, 1400]
outlier_price = [[], [1000], [500, 600], [250, 350], [1600]]
line_labels = ['Smartphone', 'Tablet', 'Smartwatch', 'Smart Speaker', 'Laptop']

# Restructure the data into two 2D lists
data = [min_price, first_quartile, median_price, third_quartile, max_price]
data = np.array(data)

# Create figure before plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the data with the type of box plot
ax.boxplot(data, whis=1.5)

# Manually plot outliers
for i, outlier in enumerate(outlier_price):
    if len(outlier) > 0:
        ax.scatter(np.full(len(outlier), i + 1), outlier, marker='x', s=100, color='r')

# Drawing techniques such as background grids
ax.grid(axis='y', alpha=0.4)
ax.set_xticklabels(line_labels)

# Title of y-axis with its unit
plt.ylabel('Price (USD)')

# Title of the figure
plt.title('Price Distribution of Technology Consumer Products in 2021')

# Automatically resize the image by tight_layout() 
plt.tight_layout()

# Save fig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/24_202312251608.png')

# Clear the current image state
plt.clf()