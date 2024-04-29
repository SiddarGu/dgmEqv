import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Data
data_str = '2010,1300,500,700,10 2011,1320,510,710,12 2012,1350,520,720,13 2013,1360,530,730,14 2014,1380,540,740,15 2015,1400,550,750,17 2016,1420,560,760,19 2017,1440,570,770,20 2018,1460,580,780,22 2019,1480,590,790,23 2020,1500,600,800,25'
data_str = data_str.split()
data = np.array([item.split(',') for item in data_str], dtype=float)
line_labels = data[:, 0]
data = data[:, 1:]

data_labels = ['Movie Ticket Sales (Millions)', 'Concert Ticket Sales (Millions)', 'Sports Event Ticket Sales (Millions)', 'Average Ticket Price']

# Plotting
fig = plt.figure(figsize=(11,7))
ax1 = fig.add_subplot(111)
line1 = ax1.plot(line_labels, data[:, 0], color='r', label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax2 = ax1.twinx()
bar1 = ax2.bar(line_labels, data[:, 1], alpha=0.6, label=data_labels[1], color='blue')
ax2.set_ylabel(data_labels[1])
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
scatter1 = ax3.scatter(line_labels, data[:, 2], color='g', label=data_labels[2])
ax3.set_ylabel(data_labels[2])
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
plot4 = ax4.fill_between(line_labels, 0, data[:, 3], alpha=0.4, label=data_labels[3], color='purple')
ax4.set_ylabel(data_labels[3])

ax1.xaxis.set_ticks(line_labels)
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.title('Evolution of Sports and Entertainment Ticket Sales and Prices')
plt.grid(axis='both', color='0.95')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/167_202312310108.png')
plt.clf()
