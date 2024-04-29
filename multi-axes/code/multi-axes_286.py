
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform data
data_labels = ["Average Sales Price (Dollars)", "Number of Listings (Thousands)", "Average Days on Market (Days)"]
line_labels = ["Single Family Home", "Townhouse/Condo", "Multi-Family Home", "Vacant Land", "Short Sale", "Foreclosure"]
data = np.array([[356000, 15, 45], [259000, 7, 43], [380000, 8, 41], [132000, 3, 39], [268000, 2, 48], [265000, 1, 51]])

# Create figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Set primary y-axis
ax1.bar(line_labels, data[:, 0], width=0.2, color='b', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='b', fontsize=16)
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_title('Real Estate and Housing Market Analysis: Pricing, Listings, and Time on Market Trends', fontsize=20)

# Set second y-axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r--', marker='o', markersize=8)
ax2.set_ylabel(data_labels[1], color='r', fontsize=16)
ax2.tick_params(axis='y', labelcolor='r')

# Set third y-axis
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], 'g.-', marker='s', markersize=10)
ax3.set_ylabel(data_labels[2], color='g', fontsize=16)
ax3.tick_params(axis='y', labelcolor='g')

# Seperate multiple y-axes
ax3.spines["right"].set_position(("axes", 1.2))

# Set labels
ax1.set_xlabel("Category", fontsize=16)
ax1.set_xticklabels(line_labels, rotation=0, wrap=True)

# Show legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Automatically adjust the range of y-axes
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Draw background grids
ax1.grid(axis='y', linestyle='--', color='gray')
ax2.grid(axis='y', linestyle='--', color='gray')
ax3.grid(axis='y', linestyle='--', color='gray')

# Resize the image
fig.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/10_2023122270030.png')

# Clear current image state
plt.clf()