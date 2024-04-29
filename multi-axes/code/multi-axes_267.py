

import matplotlib.pyplot as plt 
import numpy as np 

# transform data into three variables
data_labels = ['Number of Active Users (Millions)', 'Number of Devices (Millions)', 'Average Usage Time (Minutes)']
line_labels = ['Smartphones', 'Home Computers', 'Tablets', 'Wearable Technology', 'Connected Home Devices', 'Gaming Consoles', 'Smart TVs', 'Smart Speakers', 'Virtual Reality']
data = np.array([[960, 1150, 100],
                 [200, 450, 60],
                 [650, 450, 90],
                 [210, 850, 50],
                 [180, 750, 30],
                 [120, 400, 120],
                 [180, 350, 80],
                 [150, 400, 45],
                 [110, 420, 90]])

# create a figure
plt.figure(figsize=(15,12))

# plot the first column of data array
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:, 0], color='b', width=0.3, alpha=0.7)
ax1.set_title('Technology and the Internet Usage Overview')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

# plot the second column of data array
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r', linestyle='--', marker='o')
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', colors='r')

# plot the third column of data array
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:, 2], color='g', alpha=0.3)
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', colors='g')
ax3.spines['right'].set_position(('axes', 1.1))

# adjust the range of all y-axes
ax1.set_ylim(0, 1400)
ax2.set_ylim(0, 1200)
ax3.set_ylim(0, 130)

# show the legends of all plots
ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)
ax3.legend(loc='center right', frameon=False)

# draw the background grids
ax1.grid(color='gray', alpha=0.3, linestyle=':', linewidth=1.5)

# save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/14_202312251608.png')

# clear the current image state
plt.cla()
plt.clf()
plt.close()