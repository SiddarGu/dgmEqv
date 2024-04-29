
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Production Output (Units)', 'Revenue (Dollars)', 'Cost of Goods Sold (Dollars)', 'Gross Profit (Dollars)']
line_labels = ['Automotive', 'Electronics', 'Pharmaceuticals', 'Aerospace', 'Machinery', 'Mining', 'Textiles']
data = np.array([[149075,542790,289000,253790], [20750,560090,232000,328090], [80320,456320,370000,86320], [70000,890000,780000,110000], [50000,720000,480000,240000], [60000,720000,550000,170000], [40000,450000,370000,80000]])

# Create figure and set fig size
fig = plt.figure(figsize=(15, 10))

# Create primary axes
ax1 = fig.add_subplot(111)
ax1.set_title('Manufacturing and Production Output Performance Analysis')

# Plot first column data
ax1.bar(line_labels, data[:, 0], label=data_labels[0], color='blue')
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create ax2
ax2 = ax1.twinx()

# Plot second column data
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='green')
ax2.set_ylabel(data_labels[1], color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Create ax3
ax3 = ax1.twinx()

# Plot third column data
ax3.scatter(line_labels, data[:, 2], label=data_labels[2], color='red', marker='*')
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params(axis='y', labelcolor='red')

# Create ax4
ax4 = ax1.twinx()

# Plot fourth column data
ax4.fill_between(line_labels, data[:, 3], label=data_labels[3], color='orange', alpha=0.3)
ax4.set_ylabel(data_labels[3], color='orange')
ax4.tick_params(axis='y', labelcolor='orange')

# Set position of ax3, ax4, ...
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# Show legends of all plots
ax1.legend(bbox_to_anchor=(1, 0.5))
ax2.legend(bbox_to_anchor=(1, 0.6))
ax3.legend(bbox_to_anchor=(1, 0.7))
ax4.legend(bbox_to_anchor=(1, 0.8))

# Set background grid
ax1.grid(True)

# Use Autolocator for all ax
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()
ax4.autoscale_view()

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/11_2023122261325.png')

# Clear the current image state
plt.clf()