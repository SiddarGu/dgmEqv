
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Restructure the data into two 2D lists. 
data = [[150,250,320,400,550],
        [600,850,1000,1300,1800],
        [300,400,500,600,800],
        [50,90,120,150,200],
        [400,650,850,1000,1400]]

outliers = [[], [2100], [50, 950], [225, 300], [1600]]

# Plot the data
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

# Add box plot
box = ax.boxplot(data, whis=1.5)

# Set labels
ax.set_xticklabels(['Smartphone', 'Laptop', 'Tablet', 'Wearable', 'Smart TV'])
ax.set_ylabel('Price (USD)')

# Plot outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot( np.repeat(i+1, len(outlier)), outlier, "ro")

# Add grids
plt.grid(axis='y', alpha=0.75)

# Set title
ax.set_title('Product Price Distribution in Technology and the Internet (2021)')

# Resize and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/16_202312251608.png')

# Clear the current image state
plt.clf()