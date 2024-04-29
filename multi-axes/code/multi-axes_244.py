import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Variables
data_labels = ['Cargo Volume (Millions Tonnes)', 'Transport Revenue (Millions Dollars)', 'Fuel Consumption (Millions Litres)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([
    [265, 2400, 500],
    [258, 2300, 480],
    [304, 2680, 560],
    [316, 2890, 570],
    [280, 2600, 530],
    [325, 3000, 590],
    [330, 3200, 600],
    [343, 3350, 623],
    [310, 3050, 580],
    [290, 2800, 550],
    [275, 2700, 510],
    [355, 3450, 620]
])

# Create figure
fig = plt.figure(figsize=(30, 20))
ax1 = fig.add_subplot(111)

# Line chart
ln1 = ax1.plot(line_labels, data[:,0], label=data_labels[0], color='b')
ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True)

# Line chart
ax2 = ax1.twinx()
ln2 = ax2.plot(line_labels, data[:,1], label=data_labels[1], color='r')
ax2.set_ylabel(data_labels[1], color='r')
ax2.spines['right'].set_position(('outward', 60))
ax2.tick_params(axis='y', labelcolor='r')

# Area chart
ax3 = ax1.twinx()
ln3 = ax3.fill_between(line_labels, data[:,2], color='g', alpha=0.5, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines['right'].set_position(('outward', 120))
ax3.tick_params(axis='y', labelcolor='g')
ax3.set_ylim(bottom=0)

# Legends
lns = ln1+ln2+[ln3]
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=2)

# Autoscale yaxes
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Title
plt.title('Monthly Analysis on Volume, Revenue, and Fuel Consumption in Transportation and Logistics')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/198_202312311051.png')
plt.clf()
