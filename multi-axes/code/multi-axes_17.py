
import matplotlib.pyplot as plt
import numpy as np

# transform data into variables
data_labels = np.array(['Number of Patents (Units)', 'Number of Research Papers (Units)', 'Number of Products (Units)'])
line_labels = np.array(['Automotive', 'Aerospace', 'Electronics', 'Manufacturing', 'Robotics', 'Power and Energy', 'Civil Engineering', 'Biomedical', 'Information Technology',  'Materials', 'Nanotechnology'])
data = np.array([[150, 1050, 75], [210, 1320, 90], [120, 620, 50], [170, 1550, 100], [180, 1800, 120], [190, 1700, 95], [160, 1650, 85], [200, 2100, 125], [140, 1020, 70], [200, 1750, 110], [130, 630, 50]])

# create figure with larger figsize
plt.figure(figsize=(15,10))

# plot the first column data
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], width=0.2, color='b', alpha=0.8)

# plot the second column data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', marker='o', linestyle='--')

# plot the third column data
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:,2], color='r', marker='^', linestyle='-.')

# labels and title
ax1.set_xlabel('Category', fontsize=15)
ax1.set_ylabel(data_labels[0], fontsize=15, color='b')
ax2.set_ylabel(data_labels[1], fontsize=15, color='g')
ax3.set_ylabel(data_labels[2], fontsize=15, color='r')
ax1.set_title('Science and Engineering Performance Overview: Patents, Research Papers, and Products', fontsize=20)

# adjust the positions of bars and area
ax1.set_xticks(np.arange(len(line_labels)))
ax1.set_xticklabels(line_labels, rotation=90)
ax1.set_yticks(np.arange(0, max(data[:,0])+50, 50))
ax2.set_yticks(np.arange(0, max(data[:,1])+250, 250))
ax3.set_yticks(np.arange(0, max(data[:,2])+25, 25))
ax3.patch.set_alpha(0.6)

# add legends
# first chart
ax1.legend(['Patents'], loc='upper left')
# second chart
ax2.legend(['Research Papers'], loc='upper right')
# third chart
ax3.legend(['Products'], loc='center right')

# grid
plt.grid(True, which='both')

# autolocator
ax1.yaxis.set_major_locator(plt.MaxNLocator(11))
ax2.yaxis.set_major_locator(plt.MaxNLocator(11))
ax3.yaxis.set_major_locator(plt.MaxNLocator(11))

# save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/19_2023122270030.png')
plt.clf()