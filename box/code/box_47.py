

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Restructure the data into two 2D lists
data = [[0.2, 1.2, 2.5, 3.9, 6.5], [2.4, 5.6, 9.1, 13.0, 17.2], [11.8, 17.4, 23.2, 30.1, 38.5], 
        [8.2, 14.6, 19.8, 26.0, 33.6], [3.4, 7.8, 11.5, 16.2, 21.5]]
outliers = [[], [21.2], [36.2, 41.2], [35.9, 40.2], [34.2]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, whis=1.5, patch_artist=True)

# Adjust parameters in ax.boxplot
for box in bp['boxes']:
    box.set(color='#1f77b4', linewidth=2)
    box.set(facecolor='#1f77b4', alpha=0.2)
for whisker in bp['whiskers']:
    whisker.set(color='#1f77b4', linewidth=2)
for cap in bp['caps']:
    cap.set(color='#1f77b4', linewidth=2)
for median in bp['medians']:
    median.set(color='#ff7f0e', linewidth=2)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro', markersize=6)

# Add grid and axis label
ax.set_xticklabels(['Household', 'Transportation', 'Manufacturing', 'Agriculture', 'Waste'])
ax.set_ylabel('Carbon Footprint (KgCO2)', rotation=90, fontsize=12, labelpad=20)
ax.yaxis.set_label_coords(-0.08, 0.5)
ax.yaxis.grid(True)

# Set title of figure
plt.title('Carbon Footprint Distribution of Different Sectors in 2021', fontsize=14)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/37_202312251608.png')

# Clear current image
plt.clf()