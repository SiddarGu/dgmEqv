

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Volume Sold (Liters)', 'Sale (Dollars)', 'Average of State Bottle Retail', 'Bottles Sold']
data = np.array([[45807,435241,10603,786],[19499,382710,37567,751],[45268,376511,11088,665],[49838,327549,8862,245],[38799,338029,12260,153],[13754,145666,14875,660]])
line_labels = ['Beer', 'Wine', 'Spirits', 'Soft Drinks', 'Prepared Food', 'Miscellaneous']

# Create figure before plotting
plt.figure(figsize=(15, 10))

# Plot the data with the type of multi-axes chart
ax1 = plt.subplot(111)
plt.bar(line_labels, data[:, 0], width=0.2, color='#2E2E2E', alpha=0.8, label=data_labels[0])
ax2 = ax1.twinx()
plt.plot(line_labels, data[:, 1], '-ro', linewidth=2, markersize=10, label=data_labels[1])
ax3 = ax1.twinx()
plt.plot(line_labels, data[:, 2], '-g^', linewidth=2, markersize=10, label=data_labels[2])
ax4 = ax1.twinx()
plt.plot(line_labels, data[:, 3], '-b*', linewidth=2, markersize=10, label=data_labels[3])

# Label all axes, and match their colors with the data plotted against them
ax1.set_ylabel(data_labels[0], color='#2E2E2E')
ax2.set_ylabel(data_labels[1], color='red')
ax3.set_ylabel(data_labels[2], color='green')
ax4.set_ylabel(data_labels[3], color='blue')
ax1.set_xlabel('Category')

# Adjust the position of ax2, ax3, ax4
ax2.spines['right'].set_position(('axes', 1.))
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# Show the legends of all plots
ax1.legend(loc='upper left', fontsize='large')
ax2.legend(loc='upper center', fontsize='large')
ax3.legend(loc='upper right', fontsize='large')
ax4.legend(loc='center right', fontsize='large')

# Draw background grids
ax1.yaxis.grid(True)
ax2.yaxis.grid(True)
ax3.yaxis.grid(True)
ax4.yaxis.grid(True)

# Autolocator for all ax
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

# Set the title of the figure
plt.title('Food and Beverage Sales Analysis: Volume, Revenue, and Pricing Trends')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/15_202312251608.png')

# Clear the current image state
plt.clf()