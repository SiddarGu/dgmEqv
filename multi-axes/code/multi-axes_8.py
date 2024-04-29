

import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(['Number of Projects', 'Number of Patents', 'Number of Journals', 'Number of Researchers'])
line_labels = np.array(['Robotics', 'Biotechnology', 'Artificial Intelligence', 'Nanotechnology', 'Aerospace Engineering', 
                        'Computer Science', 'Electrical Engineering', 'Mechanical Engineering'])
data = np.array([[87, 531, 20, 450], 
                 [48, 323, 14, 681], 
                 [92, 412, 32, 580], 
                 [60, 231, 19, 510], 
                 [95, 312, 17, 570], 
                 [75, 305, 30, 590], 
                 [103, 521, 25, 620], 
                 [104, 412, 21, 550]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width = 0.15, color = 'b', alpha = 0.6)
ax1.set_ylabel(data_labels[0], color = 'b')
ax1.set_title('Innovation in Science and Engineering: Exploring Projects, Patents, Journals, and Researchers')
ax1.tick_params(axis = 'y', labelcolor = 'b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color = 'r', marker = 'o')
ax2.set_ylabel(data_labels[1], color = 'r')
ax2.tick_params(axis = 'y', labelcolor = 'r')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:, 2], color = 'g', linestyle = '-')
ax3.set_ylabel(data_labels[2], color = 'g')
ax3.tick_params(axis = 'y', labelcolor = 'g')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('axes', 1.2))
ax4.plot(line_labels, data[:, 3], color = 'y', linestyle = ':')
ax4.set_ylabel(data_labels[3], color = 'y')
ax4.tick_params(axis = 'y', labelcolor = 'y')

for ax in [ax1, ax2, ax3, ax4]:
    ax.grid(True)
    ax.autoscale()

handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
handles4, labels4 = ax4.get_legend_handles_labels()
handles.extend(handles2)
handles.extend(handles3)
handles.extend(handles4)
labels.extend(labels2)
labels.extend(labels3)
labels.extend(labels4)
ax1.legend(handles, labels, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fontsize='x-large')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/37_2023122270030.png')
plt.clf()