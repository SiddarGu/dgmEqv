import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from matplotlib import gridspec

# Data
data_str = """2010,20000,21000,10.2
2011,20300,21400,10.5
2012,20600,21800,10.8
2013,21000,22200,11.1
2014,21300,22600,11.4
2015,21600,22900,11.7
2016,22000,23200,12.0
2017,22400,23600,12.3
2018,22800,24000,12.6
2019,23200,24500,12.9
2020,23500,24900,13.2"""
data_lines = data_str.split('\n')
line_labels = [int(line.split(',')[0]) for line in data_lines]
data = np.array([list(map(float, line.split(',')[1:])) for line in data_lines])
data_labels = ['Total Energy Produced (Billion BTUs)', 'Total Energy Consumed (Billion BTUs)', 'Average Price of Electricity (Cents per kilowatthour)']

# Create figure
plt.figure(figsize=(20, 10))
gs = gridspec.GridSpec(1, 1)

# Primary y-axis
ax1 = plt.subplot(gs[0])
ax1.plot(line_labels, data[:,0], 'b-', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.label.set_color('b')
ax1.tick_params(axis='y', colors='b')
ax1.grid(True)
ax1.yaxis.set_major_locator(AutoLocator())

# Secondary y-axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.yaxis.label.set_color('r')
ax2.tick_params(axis='y', colors='r')
ax2.yaxis.set_major_locator(AutoLocator())

# Tertiary y-axis
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color='g', alpha=0.5, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines['right'].set_position(('outward', 60)) # offset third y-axis
ax3.yaxis.label.set_color('g')
ax3.tick_params(axis='y', colors='g')
ax3.yaxis.set_major_locator(AutoLocator())

# Legend
axes = [ax1, ax2, ax3]
labels = sum([ax.get_legend_handles_labels()[1] for ax in axes], [])
plt.legend(labels, loc='upper left')

# Title
plt.title('Temporal Analysis of Energy Production, Consumption and Cost')

# Save and show
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/85_2023122292141.png')
plt.show()
plt.clf()
