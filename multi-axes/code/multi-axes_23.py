

import numpy as np
import matplotlib.pyplot as plt

# transform data to variables
data_labels = ['Attendance (Thousands of Visitors)', 'Revenue (Millions of Dollars)', 'Average Ticket Price (Dollars)']
data = np.array([[190, 2250, 20], [140, 4050, 34], [590, 1250, 8], [290, 3250, 30], [95, 1750, 20], [490, 1050, 9], [290, 2050, 20], [190, 3000, 24], [80, 1900, 18], [990, 2500, 6]])
line_labels = ['Theater', 'Musical Performances', 'Museums', 'Concerts', 'Literary Readings', 'Art Exhibitions', 'Festivals', 'Operas', 'Ballet', 'Movies']

# create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# plot data
ax1.bar(line_labels, data[:, 0], width=0.3, color='b', alpha=0.6, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-', linewidth=2, label=data_labels[1])
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], 'g--', linewidth=2, label=data_labels[2])

# adjust axes position
ax3.spines['right'].set_position(('axes', 1.1))

# label axes
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[2], color='g')

# set legend
ax1.legend(loc=2)
ax2.legend(loc=1)
ax3.legend(loc=4)

# set title
ax1.set_title("Arts and Culture Performance Analysis: Visitation, Revenue, and Pricing Trends")

# draw background grids
plt.grid(True)

# autolocate axes
ax1.yaxis.set_major_locator(plt.MaxNLocator())
ax2.yaxis.set_major_locator(plt.MaxNLocator())
ax3.yaxis.set_major_locator(plt.MaxNLocator())

# save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/18_2023122270030.png')

# clear the current image state
plt.clf()