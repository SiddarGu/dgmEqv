import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transform data
data = np.array([
    [100,50,500],
    [150,120,530],
    [200,150,560],
    [250,180,590],
    [300,210,620],
    [350,240,650],
    [400,270,680],
    [450,300,710],
    [500,330,740],
    [550,360,770],
    [600,390,800],
    [650,420,830]
])
data_labels = ['Company Profits (Millions)', 'Investments (Millions)', 'Employee Count']
line_labels = ['Q1-2018', 'Q2-2018', 'Q3-2018', 'Q4-2018', 'Q1-2019', 'Q2-2019', 'Q3-2019', 'Q4-2019', 'Q1-2020', 'Q2-2020', 'Q3-2020', 'Q4-2020']

# Create figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Plot data
line1 = ax1.plot(line_labels, data[:, 0], color='r', label=data_labels[0])
ax2 = ax1.twinx()
area2 = ax2.fill_between(line_labels, data[:, 1], color='g', alpha=0.5, label=data_labels[1])
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
bar3 = ax3.bar(line_labels, data[:, 2], color='b', alpha=0.5, label=data_labels[2], width=0.5)

# Label axes
ax1.set_ylabel(data_labels[0], color='r')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='b')

# Set locators
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Set legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax3.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc=0)

# Title
plt.title("Quarterly Business Performance: Profit, Investment, and Employee Growth")

# Save figure
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/236_202312311051.png")

# Clear figure
plt.clf()
