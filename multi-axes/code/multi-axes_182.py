import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from matplotlib import colors as mcolors

# convert given data to ndarray
data_labels = ['Number of Internet Users (Millions)','E-commerce Sales (Billions of Dollars)','Average Internet Speed (Mb/s)','Number of Cyber Attacks (Thousands)']
line_labels = ['2012','2013','2014','2015','2016','2017','2018','2019','2020']
data = np.array([
    [2450,680,5,3600],
    [2700,710,6,3230],
    [3100,820,7,4380],
    [3390,900,9,5100],
    [3700,1020,12,5860],
    [4140,1260,15,7080],
    [4490,1460,18,7780],
    [4900,1765,22,8660],
    [5300,2090,25,9600]   
])

# plot settings
colors = list(mcolors.BASE_COLORS.keys())
fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.7, label=data_labels[0])
ax1.grid(True)
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params(axis='y', colors=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.tick_params(axis='y', colors=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color=colors[2], label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))  # Move third y-axis to the right
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.tick_params(axis='y', colors=colors[2])
ax3.yaxis.set_major_locator(AutoLocator())

if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], color=colors[3], alpha=0.3, label=data_labels[3])
    ax4.spines['right'].set_position(('outward', 120))  # Move fourth y-axis further to the right
    ax4.set_ylabel(data_labels[3], color=colors[3])
    ax4.tick_params(axis='y', colors=colors[3])
    ax4.yaxis.set_major_locator(AutoLocator())

# setting title, legends and saving the plot
fig.suptitle('An Overview of Internet Usage Trends, E-commerce Sales, Internet Speed and Cyberattacks', fontsize=18)
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/178_202312310150.png')
plt.clf()
