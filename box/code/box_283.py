
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists. 
data = [[2.5,5.0,7.5,10.0,12.5], [3.0,7.5,10.0,13.0,17.0], [1.5,4.0,6.5,9.0,11.0], [2.0,5.5,8.5,11.5,15.0], [3.5,7.0,9.5,12.0,14.5]]
outliers = [[], [19.5], [0.5,15.5,17.5], [13.5,18.5], [17.0]]

# Plot the data with the type of box plot.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot Outliers
for i, outlier in enumerate(outliers):
    if len(outlier)>0:
        ax.plot([i+1]*len(outlier), outlier, c='r', marker='o', linestyle='None')

# Set Grids
ax.grid(True, linestyle='-', color='0.75')

# Set Label
ax.set_xticklabels(['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E'], fontsize=10, rotation=45)
ax.set_ylabel("Price (USD)", fontsize=12)

# Set Title
ax.set_title('Price Distribution of Food Brands in Food and Beverage Industry in 2021', fontsize=15)

# Resize
fig.tight_layout()

# Save Figure
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/7_202312251520.png')

# Clear Current Image State
plt.clf()