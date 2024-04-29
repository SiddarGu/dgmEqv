
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels= np.array(['Category', 'Number of Users (Millions)', 'Revenue (Billions of Dollars)', 'Average Session Length (Minutes)'])
line_labels= np.array(['Social Media', 'Video Streaming', 'Online Shopping', 'Cloud Computing', 'Digital Advertising', 'Mobile Apps', 'Online Gaming', 'E-learning', 'Cybersecurity', 'Artificial Intelligence'])
data= np.array([[2.9,7.5,41], [1.3,17.3,20], [2.3,5.7,28], [1.1,3.2,14], [1.8,80.2,14], [1.5,4.2,10], [1.2,4.7,30], [0.8,2.1,35], [0.4,1.2,20], [0.2,1.7,15]])

# Split the data array from the second dimension to get the data correpsonding to each category.
data_1, data_2, data_3= data[:,0], data[:,1], data[:,2]

# Plot the data with the type of multi-axes chart.
fig= plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

# The plot type of each category is sequentially decided by the following plot types, i.e., [ bar chart,line chart,area chart,scatter chart].
ax.bar(line_labels, data_1, label=data_labels[1], color='b')
ax.plot(line_labels, data_2, label=data_labels[2], color='r')
ax.fill_between(line_labels, data_3, color='g', alpha=0.5)
ax.scatter(line_labels, data_3, label=data_labels[3], color='g', marker='*')

# For the plot of different bar charts, set different bar positions to avoid overlapping.
ax.set_xticks(np.arange(len(line_labels))+0.2)
ax.set_xticklabels(line_labels, rotation=45, wrap=True)

# Label each axis with the name of the category it represents, matching the color of the data plotted against it.
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1], color='b')
ax.tick_params('y', colors='b')
ax2=ax.twinx()
ax2.set_ylabel(data_labels[2], color='r')
ax2.tick_params('y', colors='r')
ax3=ax.twinx()
ax3.spines["right"].set_position(("axes", 1.2))
ax3.set_ylabel(data_labels[3], color='g')
ax3.tick_params('y', colors='g')

# Add a legend to the chart that clearly identifies each data category, ensuring it does not overlap with the chart itself.
ax.legend(loc=1)

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Chart Title,Tech and Internet Usage Analysis: User Base, Revenues, and Time Spent .
plt.title('Tech and Internet Usage Analysis: User Base, Revenues, and Time Spent')

# Use Autolocator to adjust the range of each y-axis.
ax.autoscale_view()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/1.png')

# Clear the current image state at the end of the code.
plt.clf()