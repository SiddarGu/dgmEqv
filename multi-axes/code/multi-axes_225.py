
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels=['Approval Rate (%)','Votes Received (Millions)','Average Spending Per Vote (Dollars)']
data=np.array([[90,3.2,1.6],[91,10.4,0.9],[89,18.2,2.3],[93,2.7,1.2],[92,5.1,1.4],[94,3.4,2.3],[95,6.8,1.7],[93,5.2,1.3],[92,2.9,1.8]])
line_labels=['Local Government','State Government','Federal Government','Public Utilities','Education','Public Safety','Health Care','Social Services','Environmental Policy']

# Create figure before plotting
plt.figure(figsize=(15,10))
ax1=plt.subplot(111)

# Plot the data with the type of multi-axes chart
# The first column of data array, i.e., data[:,0] is plotted first, whose y-axis is unique to data[:,0] and defined as the primary y-axis in the multi-axes chart, while the x-axis is shared. 
ax1.bar(line_labels, data[:,0],width=0.2,alpha=0.6,color='g')
ax1.set_ylabel(data_labels[0], color='g')
ax1.set_xlabel('Category')
ax1.tick_params(axis='y', labelcolor='g')

# Then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2 on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2=ax1.twinx()
ax2.plot(line_labels, data[:,1], linestyle='-.',marker='o', linewidth=2, color='b')
ax2.set_ylabel(data_labels[1], color='b')
ax2.tick_params(axis='y', labelcolor='b')

# After that, the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx, named as ax3 to overlay another new ax on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3=ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], color='k',alpha=0.2)
ax3.set_ylabel(data_labels[2], color='k')
ax3.spines["right"].set_position(("axes",1.05))
ax3.tick_params(axis='y', labelcolor='k')

# Label all axes, and match their colors with the data plotted against them.
# Show the legends of all plots at different positions, ensuring it does not overlap with other legends and not interfere with data, title and axes.
ax1.legend(data_labels[0],loc=(0.05,0.8),facecolor='w')
ax2.legend(data_labels[1],loc=(0.05,0.7),facecolor='w')
ax3.legend(data_labels[2],loc=(0.05,0.6),facecolor='w')

# Drawing techniques such as background grids can be used.
ax1.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes.
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()

# The title of the figure should be  Chart Title,Government and Public Policy Performance Overview
ax1.set_title('Government and Public Policy Performance Overview', fontsize=20)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8_202312251608.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8_202312251608.png')

# Clear the current image state at the end of the code.
plt.clf()