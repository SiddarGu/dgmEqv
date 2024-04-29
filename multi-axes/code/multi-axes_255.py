import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import AutoLocator

data_labels = ['Active Internet Users (Billions)', 'E-commerce Revenue (Trillions USD)', 'Average Internet Speed (Mbps)']
line_labels = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
data = np.array([[1.97, 0.572, 2.3], [2.27, 0.639, 3.8], [2.57, 0.853, 5.4], [2.75, 1.183, 7.6], [3.01, 1.548, 9.8], [3.36, 1.915, 12.3], [3.65, 2.304, 14.7], [3.89, 2.842, 15.3], [4.21, 3.453, 17.2], [4.54, 3.915, 19.1], [4.9, 4.476, 19.4]])

fig = plt.figure(figsize=(25,10))

plot_types = ['line', 'line', 'bar']

colors = ['r', 'g', 'b']

ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], color=colors[0], label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.spines['right'].set_position(('outward', 60))
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.bar(line_labels, data[:,2], color=colors[2], alpha=0.3, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.spines['right'].set_position(('outward', 120))
ax3.yaxis.set_major_locator(AutoLocator())

plt.title('Digitally Connected World: Internet Users, E-commerce, and Connection Speed')

leg = ax1.legend(loc='upper left')
leg = ax2.legend(loc='upper center')
leg = ax3.legend(loc='upper right')

plt.grid(True)
plt.autoscale(enable=True, axis='x', tight=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/98_2023122292141.png')
plt.cla()
plt.close(fig)
