

import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Number of Trees Planted (Thousands)', 'CO2 Emissions Reduction (Millions of Tons)', 'Amount of Waste Recycled (Millions of Tons)', 
               'Number of Solar Panels Installed (Millions)']
data = np.array([[200, 70, 40, 2], [100, 60, 20, 5], [50, 20, 30, 1], [25, 10, 15, 3], [60, 30, 10, 2]])
line_labels = ['Reforestation', 'Renewable Energy', 'Waste Disposal', 'Solar Power', 'Carbon Offset']

# Plot
# create figure
fig, ax1 = plt.subplots(figsize=(15, 10))

# Plot the first column data with bar chart
ax1.bar(line_labels, data[:, 0], width=0.3, color='red', alpha=1)
ax1.set_xlabel('Category')
ax1.set_ylabel('Number of Trees Planted (Thousands)', color='red')
ax1.tick_params('y', colors='red')

# Plot the second column data with line chart overlaying a new ax on ax1
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='blue', linestyle='--', marker='o', markersize=10, linewidth=3)
ax2.set_ylabel('CO2 Emissions Reduction (Millions of Tons)', color='blue')
ax2.tick_params('y', colors='blue')

# Plot the third column data with area chart overlaying a new ax on ax1
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:, 2], color='green', alpha=0.5)
ax3.set_ylabel('Amount of Waste Recycled (Millions of Tons)', color='green')
ax3.tick_params('y', colors='green')

# Plot the fourth column data with scatter chart overlaying a new ax on ax1
ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:, 3], color='orange', marker='D', s=50)
ax4.set_ylabel('Number of Solar Panels Installed (Millions)', color='orange')
ax4.tick_params('y', colors='orange')

# Separate y-axes
ax3.spines['right'].set_position(('axes', 1.05))
ax4.spines['right'].set_position(('axes', 1.1))

# Set background grids
ax1.grid(axis='y', color='black', alpha=0.3, linestyle='--')

# Set autolocator
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

# Set the title
plt.title('Environment and Sustainability: Strategies for a Sustainable Future', fontsize=20)

# Show legends
ax1.legend(data_labels, bbox_to_anchor=(0.9, 0.9))
ax2.legend(data_labels, bbox_to_anchor=(0.9, 0.85))
ax3.legend(data_labels, bbox_to_anchor=(0.9, 0.8))
ax4.legend(data_labels, bbox_to_anchor=(0.9, 0.75))

# Automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/7_2023122270030.png')

# Clear the current image state
plt.clf()