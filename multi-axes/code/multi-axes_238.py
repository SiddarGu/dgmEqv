

import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Quantity Produced (Units)', 'Sales (Dollars)', 'Manufacturing Cost (Dollars)', 'Labour Cost (Dollars)']
line_labels = ['Electronics', 'Automobiles', 'Pharmaceuticals', 'Furniture', 'Textiles', 'Ceramics', 'Metals']
data = np.array([[780, 98760, 21600, 3090], 
                 [902, 87300, 24450, 3720], 
                 [1020, 100200, 18700, 3560], 
                 [1090, 71250, 14600, 3420], 
                 [964, 74150, 15400, 3180], 
                 [890, 86840, 17200, 3020], 
                 [1050, 85790, 19500, 3780]])

# create figure
plt.figure(figsize=(15, 8))

# plot the data with the type of multi-axes chart
# the first column of data array, i.e., data[:,0] is plotted first
ax1 = plt.subplot(111)
plt.bar(x=line_labels, height=data[:, 0], color=['#c34f4f', '#c38f4f', '#c3cf4f', '#83c34f', '#43c34f', '#0fc34f', '#4fc38f'])
ax1.set_ylabel(data_labels[0])
ax1.set_xlabel('Category')
ax1.set_title('Manufacturing and Production: Output and Cost Analysis')

# the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='#4f83c3', marker='o', linestyle=':')
ax2.set_ylabel(data_labels[1])

# the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:, 2], color='#c34f83', marker='x', linestyle='--')
ax3.set_ylabel(data_labels[2])

# by analogy, before plotting each column data, a new ax need to be created based on the first plot
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels, data[:, 3], color='#c38f4f', marker='s', linestyle='-.')
ax4.set_ylabel(data_labels[3])

# label all axes, and match their colors with the data plotted against them
ax1.yaxis.label.set_color('#c34f4f')
ax2.yaxis.label.set_color('#4f83c3')
ax3.yaxis.label.set_color('#c34f83')
ax4.yaxis.label.set_color('#c38f4f')

# show the legends of all plots at different positions
ax1.legend(labels=data_labels[0], loc='upper left')
ax2.legend(labels=data_labels[1], loc='upper right')
ax3.legend(labels=data_labels[2], loc='lower right')
ax4.legend(labels=data_labels[3], loc='lower left')

# drawing techniques such as background grids can be used
ax1.grid(axis='y', alpha=0.4, color='#e0e0e0')
ax2.grid(axis='y', alpha=0.4, color='#e0e0e0')
ax3.grid(axis='y', alpha=0.4, color='#e0e0e0')
ax4.grid(axis='y', alpha=0.4, color='#e0e0e0')

# use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

# automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/30_2023122270030.png')

# clear the current image state
plt.clf()