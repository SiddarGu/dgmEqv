
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Number of Laws Passed","Number of Regulations Enacted","Number of Committees Established","Number of Agencies Set Up"]
data = np.array([[7,12,2,4],[3,5,1,2],[10,20,3,4],[5,18,2,5],[4,7,1,2],[9,11,2,3],[6,9,1,2]])
line_labels = ["Taxation", "Immigration", "Education", "Health Care", "Trade", "Environment", "Defense"]

# Create figure before plotting
plt.figure(figsize=(15,10))

# Plot the data with the type of multi-axes chart
ax1 = plt.subplot(111)
ax1.bar(line_labels,data[:,0], color='b')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(line_labels,data[:,1], color='r', marker='o')
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params('y', colors='r')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(line_labels,data[:,2], color='g', marker='s')
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params('y', colors='g')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.plot(line_labels,data[:,3], color='m', marker='^')
ax4.set_ylabel(data_labels[3], color='m')
ax4.tick_params('y', colors='m')

# Adjust the positions of different bars
ax1.set_xticks(np.arange(len(line_labels)))
ax1.set_xticklabels(line_labels, rotation=30, wrap=True)

# Label all axes
ax1.set_xlabel('Category')

# Show the legends of all plots
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='lower left')
ax4.legend([data_labels[3]], loc='lower right')

# Drawing techniques such as background grids can be used
ax1.grid(axis='y', linestyle='-')

# Set title
plt.title('Government and Public Policy: Legislation, Regulation, and Agency Responsibilities')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/13_2023122270030.png')

# Clear the current image state
plt.clf()