import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Transform the data into numpy array
data_labels = ['Revenue (Millions of Dollars)', 'Operating Expense (Millions of Dollars)', 'Net Profit (Millions of Dollars)','Total Assets (Millions of Dollars)']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']
data = np.array([[1200, 400, 400, 5000],
                 [1300, 450, 480, 5500],
                 [1250, 425, 425, 5250],
                 [1400, 475, 475, 6000]])

colors = ['r', 'b', 'g', 'y']

# Create figure
fig = plt.figure(figsize=(25, 15))
ax1 = fig.add_subplot(111)

# Draw bar chart on primary y-axis and shared x-axis
ax1.bar(line_labels, data[:, 0], color=colors[0], alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params(axis='y', colors=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(True)

# Draw line chart on secondary y-axis and shared x-axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.tick_params(axis='y', colors=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())

# Draw line chart on third y-axis with shared x-axis
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color=colors[2], label=data_labels[2])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.tick_params(axis='y', colors=colors[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.set_major_locator(AutoLocator())

# Draw area chart on fourth y-axis with shared x-axis
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], color=colors[3], alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color=colors[3])
ax4.tick_params(axis='y', colors=colors[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylim(0)
ax4.yaxis.set_major_locator(AutoLocator())

# Add legends
ax1.legend(loc='center')
ax2.legend(loc='best')
ax3.legend(loc='upper left')
ax4.legend(loc='lower right')

# Set title
plt.title('Corporate Financial Performance Analysis: Revenue, Expense, Profit, and Assets')

# Automatically adjust layout
plt.tight_layout()

# Save plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/221_202312311051.png')

# Clear plot
plt.clf()
