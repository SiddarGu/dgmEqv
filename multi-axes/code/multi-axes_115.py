import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Define the data
data_labels = ['Number of Houses Sold', 'Median House Price (Thousands of Dollars)', 'Percentage of Houses Sold in Urban Areas (%)', 'Percentage of Houses Sold in Rural Areas (%)']
data = np.array([[5400, 270, 70, 30], [5650, 280, 72, 28], [5900, 295, 74, 26], [6100, 310, 76, 24], [6350, 325, 78, 22], [6600, 335, 80, 20]])
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020']

# Create the figure and subplots
fig = plt.figure(figsize=[25, 15])
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

# Offset the right spine of ax3 and ax4. The ticks and label have already been placed on the right by twinx above.
ax3.spines.right.set_position(("axes", 1.1))
ax4.spines.right.set_position(("axes", 1.2))

# Plot the data
ax1.bar(line_labels, data[:,0], color='g', label=data_labels[0])
ax2.plot(line_labels, data[:,1], color='b', marker='o', label=data_labels[1])
ax3.fill_between(line_labels, data[:,2], color='y', alpha=0.6, label=data_labels[2])
ax4.scatter(line_labels, data[:,3], color='r', label=data_labels[3])

# Set the tick colors to match the line colors
ax1.yaxis.set_tick_params(colors='g')
ax2.yaxis.set_tick_params(colors='b')
ax3.yaxis.set_tick_params(colors='y')
ax4.yaxis.set_tick_params(colors='r')

# Set the axis labels
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='g')
ax2.set_ylabel(data_labels[1], color='b')
ax3.set_ylabel(data_labels[2], color='y')
ax4.set_ylabel(data_labels[3], color='r')

# Move the legends to avoid overlapping
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='lower left')
ax4.legend(loc='lower center')

# Add gridlines
ax1.grid(True)

# Use autolocator for all axes
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

# Set the title
plt.title('Analysis of Real Estate Sales in Urban and Rural Areas Over the Years')

# Automatically resize the image by tight_layout() before saving the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/118_202312310108.png')

# Clear the current figure
plt.clf()
