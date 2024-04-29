
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform data
data_labels = ['Usage (Watt-hours)', 'Cost (Dollars)', 'Average Bill (Dollars)', 'Customers']
line_labels = ['Electricity', 'Natural Gas', 'Renewable Energy', 'Solar Power',
               'Wind Power', 'Hydropower', 'Nuclear Energy']

data = np.array([[4500, 7000, 150, 2000], [3500, 4500, 110, 1500],
                 [2800, 4000, 90, 1200], [1700, 2500, 60, 900],
                 [1200, 3000, 70, 1100], [900, 2000, 50, 800],
                 [2100, 3500, 80, 1000]])

# Create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot first column data
x_range = np.arange(len(line_labels))
bar_width = 0.8
ax1.bar(x_range, data[:, 0], bar_width, color='#0093b9', label=data_labels[0])
ax1.set_xticks(x_range)
ax1.set_xticklabels(line_labels)
ax1.set_xlabel('Category')

# Plot second column data
ax2 = ax1.twinx()
ax2.plot(x_range, data[:, 1], color='#ff9c00', marker='o', label=data_labels[1])

# Plot third column data
ax3 = ax1.twinx()
ax3.plot(x_range, data[:, 2], color='#fecf44', marker='o', label=data_labels[2])

# Plot fourth column data
ax4 = ax1.twinx()
ax4.plot(x_range, data[:, 3], color='#6f3c00', marker='o', label=data_labels[3])

# Position of ax2, ax3, ax4
ax2.spines['right'].set_position(('axes', 1.0))
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# Autolocator for all ax
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax3.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax4.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Label all axes
ax1.set_ylabel(data_labels[0], color='#0093b9')
ax2.set_ylabel(data_labels[1], color='#ff9c00')
ax3.set_ylabel(data_labels[2], color='#fecf44')
ax4.set_ylabel(data_labels[3], color='#6f3c00')

# Show legend
ax1.legend(loc='lower left')
ax2.legend(loc='upper left')
ax3.legend(loc='upper center')
ax4.legend(loc='upper right')

# Set title
plt.title('Energy and Utilities Usage and Cost Analysis')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/6_202312251608.png')

# Clear the current image state
plt.cla()