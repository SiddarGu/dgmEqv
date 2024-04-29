
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
values = [[20,200,400,600,800], 
          [30,250,450,650,850], 
          [50,300,500,700,900], 
          [100,400,550,700,950], 
          [60,400,500,800,900]] 
outliers = [[], [1000], [5,1000], [1100], [1050]]

# Create figure before plotting
fig, ax = plt.subplots(figsize=(10,5))

# Plot the data with the type of box plot
ax.boxplot(values, whis=1.5, 
           boxprops=dict(linewidth=2, color='black'),
           whiskerprops=dict(linewidth=2, color='black'),
           capprops=dict(linewidth=2, color='black'),
           medianprops=dict(linewidth=2, color='black'),
           flierprops=dict(marker='o', markerfacecolor='black', markersize=7))

# Use enumerate to iterate through the outliers list
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, "o", markerfacecolor="black", markersize=7)

# Drawing techniques such as background grids
ax.grid(axis='y', linestyle='--', linewidth=1, alpha=0.3)

# The title of y-axis should be given with its unit
ax.set_ylabel('Value (USD)')
ax.set_xticklabels(['Company A', 'Company B', 'Company C', 'Company D', 'Company E'], rotation=45, wrap=True)
ax.set_title('Stock Value Distribution in Business and Finance Companies (2021)')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/32_202312270030.png')

# Clear the current image state at the end of the code
plt.clf()