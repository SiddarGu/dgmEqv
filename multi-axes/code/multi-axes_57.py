import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator

# Prepare data
data = np.array([
    [10000, 5000000, 500],
    [5000, 10000000, 2000],
    [8000, 20000000, 2500],
    [12000, 6000000, 500],
    [15000, 4500000, 300],
    [20000, 10000000, 500],
    [10000, 8000000, 800],
    [8000, 12000000, 1500],
    [15000, 9000000, 600],
    [10000, 7000000, 700]
])
data_labels = ['Total Production (units)', 'Total Revenue (dollars)', 'Average Price per Unit']
line_labels = ['Electronics', 'Automobiles', 'Pharmaceuticals', 'Consumer Goods', 'Textiles', 'Food Products', 'Chemicals', 'Machinery', 'Construction Materials', 'Metal Products']

fig = plt.figure(figsize=(30,15))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color = 'b', alpha = 0.7)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')
ax1.tick_params(axis='y', colors='b')

if len(data[0]) > 1:
    ax2 = ax1.twinx()
    ax2.plot(line_labels, data[:, 1], 'r-')
    ax2.set_ylabel(data_labels[1])
    ax2.yaxis.label.set_color('r')
    ax2.tick_params(axis='y', colors='r')

if len(data[0]) > 2:
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:, 2], color = 'g')
    ax3.spines['right'].set_position(('outward', 60))
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color('g')
    ax3.tick_params(axis='y', colors='g')

ax1.xaxis.set_tick_params(rotation=45)
plt.title('Manufacturing and Production Performance Analysis')
plt.legend([ax1, ax2, ax3 if 'ax3' in locals() else ax1], data_labels)
ax1.grid()
ax1.yaxis.set_major_locator(AutoLocator())
if 'ax2' in locals(): ax2.yaxis.set_major_locator(AutoLocator())
if 'ax3' in locals(): ax3.yaxis.set_major_locator(AutoLocator())

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/296_202312311430.png')
plt.clf()
