
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
store = ['Department Store', 'Grocery Store', 'Online Store', 'Boutique', 'Discount Store']
min_price = [5, 7, 12, 10, 3]
Q1_price = [20, 25, 30, 35, 15]
median_price = [50, 60, 70, 60, 40]
Q3_price = [90, 100, 110, 80, 70]
max_price = [120, 150, 160, 130, 100]
outliers = [[], [200], [2, 180], [170], [200, 220]]

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Product Price Distribution in Different Types of Stores in 2021')
ax.set_ylabel('Price (USD)')
ax.set_xlabel('Type of Store')
ax.set_xticklabels(store, rotation=45, wrap=True)

# Transform the data into a 2D list
data = np.array([min_price, Q1_price, median_price, Q3_price, max_price])

# Plot the box plot
ax.boxplot(data, showmeans=True)

# Plot the outlier
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro', alpha=0.5)

# Add background grids
ax.yaxis.grid(True)
ax.xaxis.grid(False)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/4_202312251315.png')

# Clear the current image state
plt.clf()