

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Number of Schools', 'Number of Students', 'Average School Cost (USD)']
data = np.array([[980, 23500, 3000], [781, 18000, 5000], [432, 8100, 10000], [530, 23750, 2000], [240, 6000, 1000], [150, 3000, 4500]])
line_labels = ['Primary Education', 'Secondary Education', 'Higher Education', 'Vocational Education', 'Distance Education', 'Special Education']

# Create figure before plotting, i.e., add_subplot(111) follows plt.figure().
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# Plot the data with the type of multi-axes chart. 
# The first column of data array, i.e., data[:,0] is plotted first, 
# whose y-axis is unique to data[:,0] and defined as the primary y-axis in the multi-axes chart, while the x-axis is shared.
ax1.bar(line_labels, data[:,0], color='#008080', width=0.2, alpha=0.8, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='#008080')
ax1.tick_params(axis='y', labelcolor='#008080')

# Then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2 on the first plot, 
# where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', marker='o', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')
 
# After that, the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx, named as ax3 to overlay another new ax on the first plot, 
# where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], facecolor='#008080', alpha=0.3, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='#008080')
ax3.tick_params(axis='y', labelcolor='#008080', labelleft=False)

# Label all axes, and match their colors with the data plotted against them. 
# Using spine() and set_position() for ax3, ax4, ... to seperate different y-axes. 
# The y-axes of ax1 and ax2 should not use spine() or set_position().
ax3.spines['right'].set_position(('axes', 1.1))

# Show the legends of all plots at different positions, ensuring it does not overlap with other legends and not interfere with data, title and axes.
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')

# Drawing techniques such as background grids can be used. 
# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes.
ax1.grid(True, linestyle='-.', linewidth=0.5, color='black')
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# The title of the figure should be Education and Academics in the US: Analyzing School Distribution, Enrollment and Cost.
plt.title('Education and Academics in the US: Analyzing School Distribution, Enrollment and Cost', fontsize=14)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1_2023122270030.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1_2023122270030.png')

# Clear the current image state at the end of the code.
plt.clf()