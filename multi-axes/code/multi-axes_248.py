
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Number of Units Produced','Cost of Production (Dollars)', 'Profit Margin (Percentage)']
data = np.array([[20, 18000, 6], 
                 [50, 30000, 8], 
                 [30, 25000, 7], 
                 [10, 28000, 9], 
                 [40, 30000, 7],
                 [25, 40000, 10],
                 [35, 30000, 6],
                 [15, 45000, 12]])
line_labels = ['Automobiles','Electronics','Electrical Appliances','Pharmaceuticals','Machinery','Aircraft Parts','Industrial Components','Mining Equipment']

# Create figure before plotting, i.e., add_subplot(111) follows plt.figure(). The value of figsize should be set larger than 20 to prevent content from being displayed.
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the data with the type of multi-axes chart. The first column of data array, i.e., data[:,0] is plotted first, whose y-axis is unique to data[:,0] and defined as the primary y-axis in the multi-axes chart, while the x-axis is shared.
ax.bar(line_labels, data[:, 0], label='Number of Units Produced', color='b', alpha=0.6)
ax.set(xlabel='Category', ylabel='Number of Units Produced', title='Manufacturing and Production Performance Analysis: Volume, Cost, and Profit Margin Trends')

# Then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2 on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2 = ax.twinx()
ax2.plot(line_labels, data[:, 1], label='Cost of Production (Dollars)', color='r', alpha=0.6)
ax2.set_ylabel('Cost of Production (Dollars)')

# After that, the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx, named as ax3 to overlay another new ax on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3 = ax.twinx()
ax3.plot(line_labels, data[:, 2], label='Profit Margin (Percentage)', color='g', alpha=0.6)
ax3.set_ylabel('Profit Margin (Percentage)')
ax3.spines['right'].set_position(('axes', 1.1))

# Label all axes, and match their colors with the data plotted against them
ax.set_xticklabels(line_labels, rotation=45, ha="right", rotation_mode="anchor")

# Show the legends of all plots at different positions, ensuring it does not overlap with other legends and not interfere with data, title and axes.
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')

# Drawing techniques such as background grids can be used
ax.grid(True)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax.tick_params(axis='both', which='major')
ax2.tick_params(axis='both', which='major')
ax3.tick_params(axis='both', which='major')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1_2023122261325.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1_2023122261325.png')

# Clear the current image state at the end of the code
plt.clf()