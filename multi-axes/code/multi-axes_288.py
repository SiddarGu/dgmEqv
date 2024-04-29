import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Parse the data
data_raw = "Month,Website Visits (Millions),New User Registrations (Thousands),Average Session Duration (Minutes),Bounce Rate (%)\n Jan,256,120,15,46\n Feb,273,130,14,42\n Mar,320,145,16,40\n Apr,330,160,15,38\n May,310,165,14,36\n Jun,345,175,13,34\n Jul,360,174,12,32\n Aug,370,180,13,29\n Sep,390,189,14,28\n Oct,391,195,16,26\n Nov,405,203,16,23\n Dec,422,211,15,21"
data = np.array([[float(num) for num in row.split(',')[1:]] for row in data_raw.split('\n')[1:]])
line_labels = [row.split(',')[0].strip() for row in data_raw.split('\n')[1:]]
data_labels = data_raw.split('\n')[0].split(',')[1:]

# Create figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Plot the data
ax1.plot(line_labels, data[:, 0], color='b', label=data_labels[0])
ax2 = ax1.twinx()
ax2.bar(line_labels, data[:, 1], color='g', label=data_labels[1], alpha=0.7)
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60)) 
ax4 = ax1.twinx()
ax4.fill_between(line_labels, 0, data[:, 3], color='y', alpha=0.4, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120)) 

# Set the title and labels
plt.title('Web Performance Metrics')
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')
ax4.set_ylabel(data_labels[3], color='y')

# Set the autolocator for y-axes
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

# Show the grid and legends
ax1.grid()
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# Save the image and clear the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/63_2023122292141.png')
plt.cla()
