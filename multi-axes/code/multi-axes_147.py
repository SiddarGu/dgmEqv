import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from matplotlib import colors
import numpy as np

# data transformation
data_str = ["2010,1334985,2278,2125,2805","2011,1349065,2382,2212,2976","2012,1363245,2486,2300,3157","2013,1377425,2590,2388,3449",
"2014,1391605,2694,2476,3751","2015,1405785,2798,2564,4073","2016,1419965,2902,2654,4415","2017,1434145,3006,2744,4787",
"2018,1448325,3110,2834,5180","2019,1462505,3214,2924,5593"]
data = np.array([list(map(float, x.split(','))) for x in data_str])

data_labels = ['Number of Nonprofits','Total Revenue (Billion Dollars)','Total Expenses (Billion Dollars)','Net Assets (Billion Dollars)']
line_labels = [str(int(x)) for x in data[:, 0]]

# create figure and axis
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0])
ax1_bar = ax1.bar(line_labels, data[:,1], color='r')

# line chart
ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1])
ax2_line, = ax2.plot(line_labels, data[:,2], linestyle='-', color='g')

ax3 = ax1.twinx()
ax3.set_ylabel(data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3_line, = ax3.plot(line_labels, data[:,3], linestyle='-', color='b')

# area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,4], color='y', alpha=0.5)
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3])

ax1.yaxis.label.set_color(ax1_bar[0].get_facecolor())
ax2.yaxis.label.set_color(ax2_line.get_color())
ax3.yaxis.label.set_color(ax3_line.get_color())
ax4.yaxis.label.set_color('y')

plt.title('Nonprofit Organizations Growth Analysis: Revenue, Expenses, and Net Asset (2010-2019)')
plt.autoscale()
fig.tight_layout()

# Legends
fig.legend([ax1_bar[0], ax2_line, ax3_line], data_labels, loc='upper right')
ax1.grid(True)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/82_2023122292141.png')
plt.clf()
