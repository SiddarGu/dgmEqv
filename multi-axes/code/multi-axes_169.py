import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Transform the data into the necessary formats
data_labels = ['Amount of Recyclable Waste (Metric Tons)', 'CO2 Emissions Reduction(Metric Tons)', 'Number of Tree Plantings']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020']
data = np.array([[450000, 1100000, 23000], [460000, 1450000, 25000], [500000, 1650000, 30000],
                 [550000, 1800000, 35000], [580000, 2000000, 36000], [600000, 2200000, 38000]])

colors = ['tab:blue', 'tab:orange', 'tab:green']

plt.figure(figsize=(24,12))
ax1 = plt.subplot(111)
ax1.plot(line_labels, data[:,0], color=colors[0], marker='o', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())
ax1.tick_params(axis='y', colors=colors[0])

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], alpha=0.5, color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())
ax2.tick_params(axis='y', colors=colors[1])

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color=colors[2], alpha=0.4, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel(data_labels[2], color=colors[2])

plt.title('Environmental Sustainability Progress: Recycling, Emissions, and Reforestation')

fig = plt.gcf()
fig.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/150_202312310108.png', dpi=300)

plt.clf()
