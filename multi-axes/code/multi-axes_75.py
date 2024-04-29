import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

data_labels = ['Internet Users (Millions)', 'Smartphone Users (Millions)', 
               'Social Media Users (Millions)', 'E-Commerce Sales (Billion Dollars)']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020']
data = np.array([[2800, 2250, 2100, 1800],
                 [2950, 2400, 2250, 2000],
                 [3100, 2600, 2420, 2200],
                 [3250, 2800, 2600, 2400],
                 [3450, 3000, 2775, 2650],
                 [3600, 3200, 3000, 2900]])

plt.figure(figsize=(20,10))
ax1 = plt.subplot(111)
ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color='y', alpha=0.3, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='y')
ax3.spines['right'].set_position(('outward', 70))

ax4 = ax1.twinx()
b = ax4.bar(line_labels, data[:,3], alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='r')
for i in range(len(b)):
    b[i].set_x(b[i].get_x() + 0.25)
ax4.spines['right'].set_position(('outward', 35))

plt.grid()
ax1.xaxis.set_major_locator(plt.AutoLocator())
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

ax1.set_xlabel('Year')
ax1.set_title('Technology and Internet Trends: User and Sales Data')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower left')
ax4.legend(loc='lower right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/62_2023122292141.png')
plt.cla()
