import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

data_labels = ['Total Vehicles', 'Total Employees', 'Total Revenue']
line_labels = ['Road Transport', 'Rail Transport', 'Air Transport', 'Maritime Transport', 
               'Freight Forwarding', 'Warehousing', 'Courier Services', 'Customs Clearance']

data = np.array([[1000, 3000, 5000000],
                 [500, 1000, 2000000],
                 [200, 500, 1500000],
                 [300, 800, 3000000],
                 [400, 1200, 1000000],
                 [100, 300, 500000],
                 [150, 400, 800000],
                 [80, 200, 400000]])

fig = plt.figure(figsize=(22,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='skyblue', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='skyblue')

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='olive', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='olive')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.plot(line_labels, data[:,2], color='purple', label=data_labels[2])
    ax3.spines['right'].set_position(('outward', 60))  
    ax3.set_ylabel(data_labels[2], color='purple')
    ax3.yaxis.set_major_locator(AutoLocator())

plt.grid()
plt.tight_layout()
plt.title('Transportation and Logistics Overview')

ax1.legend()
ax2.legend(loc='upper left')
if data.shape[1] > 2:
    ax3.legend(loc='lower left')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/315_202312311430.png')
plt.cla()
plt.clf()
