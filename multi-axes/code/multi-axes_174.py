

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Sale (Dollars)', 'Average of State Bottle Retail', 'Bottles Sold']
line_labels = ['Soft Drinks', 'Juices', 'Milk', 'Water', 'Tea', 'Beer', 'Wine', 'Spirits', 'Coffee']
data = np.array([[49804, 329608, 15491, 2056],
                 [27574, 371087, 14240, 2243],
                 [45588, 356841, 12302, 797],
                 [37914, 334088, 14556, 2082],
                 [19699, 327549, 16701, 945],
                 [45268, 376511, 11088, 665],
                 [49838, 327549, 8862, 245],
                 [38799, 338029, 12260, 153],
                 [13754, 145666, 14875, 660]])
# Create figure before plotting, i.e., add_subplot(111) follows plt.figure().
# The value of figsize should be set larger than 20 to prevent content from being displayed.
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# The primary y-axis is naturally positioned on the left side of the chart,
# with other y-axes placed on the right side.
ax1.bar(np.arange(len(line_labels)), data[:, 0], width = 0.25, label = data_labels[0], color = '#146683', alpha = 0.6)
ax1.set_ylabel(data_labels[0], color='#146683')
plt.xticks(np.arange(len(line_labels)), line_labels, rotation=45, ha="right", fontsize=10)

# Then, the second column of data array, i.e. data[:,1], is plotted after using
# twinx to overlay a new ax, named as ax2 on the first plot,
# where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2 = ax1.twinx()
ax2.plot(np.arange(len(line_labels)), data[:, 1], '-v', label = data_labels[1], color = '#6f5c3d', alpha = 0.6)
ax2.set_ylabel(data_labels[1], color='#6f5c3d')

# After that, the third column of data array (if possible), i.e. data[:,2], is plotted
# after using another twinx, named as ax3 to overlay another new ax on the first plot,
# where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3 = ax1.twinx()
ax3.plot(np.arange(len(line_labels)), data[:, 2], '-*', label = data_labels[2], color = '#a5c842', alpha = 0.6)
ax3.set_ylabel(data_labels[2], color='#a5c842')

# Label all axes, and match their colors with the data plotted against them.
# Using spine() and set_position() for ax3, ax4, ... to seperate different y-axes.
# The y-axes of ax1 and ax2 should not use spine() or set_position().
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_frame_on(True)
ax3.patch.set_visible(False)

# Drawing techniques such as background grids can be used.
plt.grid(True)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes.
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())

# The title of the figure should be Beverage Industry Analysis: Volume Sold, Revenue, and Pricing Trends
plt.title("Beverage Industry Analysis: Volume Sold, Revenue, and Pricing Trends", fontsize=16)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/50_2023122261325.png.
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/50_2023122261325.png")
