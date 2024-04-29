import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Data
data_labels = ['Production Output (Hundred Thousand Units)', 'Products Sold (Hundred Thousand Units)', 'Average Product Price (Dollars)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([[120,110,200], [145,130,180], [150,145,190], [155,140,210], [160,157,195], [140,140,220], [150,145,215], [158,150,220], [160,155,210], [170,160,205], [175,165,215], [190,175,220]])

# Figure
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# Plot types
ax1.plot(line_labels, data[:,0], color='r', label=data_labels[0])
ax2.bar(line_labels, data[:,1], color='b', alpha=0.7, width=0.5, label=data_labels[1])
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])

# Spine position
ax3.spines['right'].set_position(('outward', 60))  

# Automatically adjust range
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Set labels
ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0], color='r')
ax2.set_ylabel(data_labels[1], color='b')
ax3.set_ylabel(data_labels[2], color='g')

# Title
plt.title('Manufacturing and Production: Output, Sales and Pricing Analysis')

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

# Grid
ax1.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/238_202312311051.png')

# Clear the current figure
plt.clf()
