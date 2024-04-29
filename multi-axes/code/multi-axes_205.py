import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import AutoLocator

# Define the data
data_labels = ['Production Volume (Units)', 'Revenue (Millions of Dollars)', 'Average Production Time (Hours)', 'Average Selling Price']
line_labels = ['Machinery', 'Chemicals', 'Automobiles', 'Electronics', 'Textiles', 'Metals', 'Plastics', 'Furniture', 'Food and Beverage', 'Paper and Packaging']
data = np.array([[5000, 1200, 30, 240], [8000, 1800, 45, 225], [6000, 1500, 35, 250], [7000, 1600, 40, 230], 
                [9000, 1300, 50, 145], [10000, 1700, 60, 170], [4000, 1400, 20, 350], [3000, 1100, 15, 367],
                [10000, 1900, 65, 190], [6000, 1700, 35, 283]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the data using different plot types
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xlabel('Category')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.tick_params(axis='y', labelcolor='r')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='g', label=data_labels[2])
ax3.set_ylabel(data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', labelcolor='g')

ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:, 3], color='purple', label=data_labels[3])
ax4.set_ylabel(data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.tick_params(axis='y', labelcolor='purple')

fig.suptitle('Manufacturing and Production Performance Analysis', fontsize=20)

fig.subplots_adjust(right=0.75)
ax2.legend(loc='upper left')
ax3.legend(loc='center left')
ax4.legend(loc='lower left')

fig.autofmt_xdate(rotation=45, ha='right')
plt.grid(True)
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/339_202312311430.png')
plt.close(fig)
