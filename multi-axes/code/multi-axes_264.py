
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Transform the given data into three variables
data_labels = ['Number of Cases','Average Resolution Time (Weeks)','Average Settlement Amount (Dollars)']
data = np.array([[3450, 21, 19000], [5690, 17, 12500], [800, 15, 8530], [2390,14,7690], [1150, 19, 4500], [650, 25, 6500], [1050, 27, 15000], [1890, 19, 10000], [450, 29, 18000]])
line_labels = ['Civil Cases', 'Criminal Cases', 'Immigration Cases', 'Family Cases', 'Bankruptcy Cases', 'Tax Cases', 'Regulatory Cases', 'Contract Disputes', 'Intellectual Property Cases']

# Create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Set x-axis labels
ax1.set_xticks([i for i in range(len(line_labels))])
ax1.set_xticklabels(line_labels, rotation=45, fontsize=12, wrap=True)

# Plot the data
ax1.bar(np.arange(len(data)), data[:,0], color='#f9c41b', alpha=0.6)

# Set primary y-axis labels
ax1.set_ylabel(data_labels[0], fontsize=14)
ax1.tick_params('y', colors='#f9c41b')

# Create ax2
ax2 = ax1.twinx()

# Plot the data
ax2.plot(np.arange(len(data)), data[:,1], '#2d2264', linestyle='--', marker='o', linewidth=2)

# Set ax2 labels
ax2.set_ylabel(data_labels[1], fontsize=14, color='#2d2264')
ax2.tick_params('y', colors='#2d2264')

# Create ax3
ax3 = ax1.twinx()

# Move ax3 to the right side
ax3.spines['right'].set_position(('axes', 1.1))

# Plot the data
ax3.fill_between(np.arange(len(data)), data[:,2], color='#29aee4', alpha=0.6)

# Set ax3 labels
ax3.set_ylabel(data_labels[2], fontsize=14, color='#29aee4')
ax3.tick_params('y', colors='#29aee4')

# Set grids and background
ax1.grid(axis='both', alpha=.4, linestyle='--')
ax1.set_facecolor('#f0f0f0')

# Set AutoMinorLocator
ax1.yaxis.set_minor_locator(AutoMinorLocator())

# Show legends
ax1.legend(['Number of Cases'], loc=(0.01, 0.85), fontsize=14)
ax2.legend(['Average Resolution Time (Weeks)'], loc=(0.01, 0.78), fontsize=14)
ax3.legend(['Average Settlement Amount (Dollars)'], loc=(0.01, 0.71), fontsize=14)

# Set chart title
plt.title('Trends in Law and Legal Affairs Cases', fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save the figure
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/13_202312251608.png')

# Clear the current image state
plt.clf()