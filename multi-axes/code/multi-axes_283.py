import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

data_labels = ["Number of Art Exhibitions", "Attendance (in thousands)", 
               "Ticket Revenue (in millions)", "Visitor Satisfaction Rating"]

line_labels = ["Paintings", "Sculptures", "Photography", "Performing Arts", 
               "Music Concerts", "Dance Performances", "Theater Shows", 
               "Film Screenings", "Literary Events", "Craft Exhibitions"]

data = np.array([[250, 1250, 25, 4.5],
                 [150, 750, 15, 4.2],
                 [200, 1000, 20, 4.6],
                 [300, 1500, 30, 4.8],
                 [350, 1750, 35, 4.7],
                 [250, 1250, 25, 4.4],
                 [400, 2000, 40, 4.9],
                 [300, 1500, 30, 4.3],
                 [200, 1000, 20, 4.5],
                 [150, 750, 15, 4.1]])

x = np.arange(data.shape[0])

fig = plt.figure(figsize=(24, 12))

ax1 = fig.add_subplot(111)
ax1.bar(x, data[:, 0], color='blue', alpha=0.75, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params(axis='y', colors='blue')
ax1.set_xticks(x)
ax1.set_xticklabels(line_labels, rotation=45, ha='right')

ax2 = ax1.twinx()
ax2.plot(x, data[:, 1], color='red', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')
ax2.tick_params(axis='y', colors='red')

ax3 = ax1.twinx()
ax3.scatter(x, data[:, 2], color='green', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', colors='green')

ax4 = ax1.twinx()
ax4.fill_between(x, 0, data[:, 3], color='purple', alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.spines['right'].set_position(('outward', 120))
ax4.tick_params(axis='y', colors='purple')

fig.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.)
ax1.grid()
ax1.xaxis.set_ticks(x)
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

fig.suptitle('Arts and Culture Event Analysis: Attendance, Revenue, and Visitor Satisfaction', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/307_202312311430.png')
plt.clf()
