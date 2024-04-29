

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

#transform data
data_labels = ['Subscribers (Millions)', 'Average View Time (Minutes)', 'Online Revenues (Billions of Dollars)', 'Number of Services']
line_labels = ['Fixed Broadband', 'Mobile Broadband', 'Video Streaming', 'Online Advertising', 'Cloud Computing', 'Social Media', 'Online Shopping', 'Voice Services', 'Enterprise Solutions']
data = np.array([[415, 30, 69, 14],
[582, 20, 54, 12],
[312, 45, 32, 9],
[801, 15, 190, 6],
[579, 20, 90, 7],
[854, 45, 58, 10],
[936, 20, 110, 8],
[708, 25, 55, 11],
[741, 30, 71, 10]])

#create figure
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)

#plot data
ax.bar(line_labels, data[:,0], width=0.2, color='#ff9999', alpha=1, label=data_labels[0])
ax2 = ax.twinx()
ax2.plot(line_labels, data[:,1], marker='o', color='#00b3b3', linestyle='--', linewidth=2, label=data_labels[1])
ax3 = ax.twinx()
ax3.spines['right'].set_position(('axes',1.1))
ax3.plot(line_labels, data[:,2], marker='^', color='#ffcc99', linestyle=':', linewidth=3, label=data_labels[2])
ax4 = ax.twinx()
ax4.spines['right'].set_position(('axes',1.2))
ax4.plot(line_labels, data[:,3], marker='s', color='#99ccff', linestyle='-.', linewidth=4, label=data_labels[3])

#label axes and show legend
ax.set_xlabel('Category', fontsize=15)
ax.set_ylabel(data_labels[0], fontsize=15, color='#ff9999')
ax2.set_ylabel(data_labels[1], fontsize=15, color='#00b3b3')
ax3.set_ylabel(data_labels[2], fontsize=15, color='#ffcc99')
ax4.set_ylabel(data_labels[3], fontsize=15, color='#99ccff')
ax.legend(loc='upper right', bbox_to_anchor=(1,1))
ax2.legend(loc='upper right', bbox_to_anchor=(1.0,0.95))
ax3.legend(loc='upper right', bbox_to_anchor=(1.0,0.9))
ax4.legend(loc='upper right', bbox_to_anchor=(1.0,0.85))

#adjust the range of all y-axes
ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.grid(which='minor', axis='y', color='gray', linestyle='dashed', linewidth=1)
ax2.yaxis.set_minor_locator(AutoMinorLocator(2))
ax2.grid(which='minor', axis='y', color='gray', linestyle='dashed', linewidth=1)
ax3.yaxis.set_minor_locator(AutoMinorLocator(2))
ax3.grid(which='minor', axis='y', color='gray', linestyle='dashed', linewidth=1)
ax4.yaxis.set_minor_locator(AutoMinorLocator(2))
ax4.grid(which='minor', axis='y', color='gray', linestyle='dashed', linewidth=1)

#set title
ax.set_title('Technology and Internet Usage Statistics: Subscribers, View Time, Revenues, and Services', fontsize=20)

#auto resize image
plt.tight_layout()

#save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/11_2023122270030.png')

#clear current image state
plt.clf()