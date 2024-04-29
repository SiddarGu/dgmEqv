import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Transformed given data into three variables
line_labels = ['Educational Organizations', 'Health Organizations', 'Environmental Organizations', 'Animal Welfare Organizations', 'Social Service Organizations', 'Arts and Cultural Organizations', 'International Aid Organizations', 'Community Development Organizations', 'Religious Organizations', 'Youth and Sports Organizations', 'Other Nonprofit Organizations']
data_labels = ['Total Donations (Millions of Dollars)', 'Number of Volunteers', 'Program Expenses (Millions of Dollars)', 'Operational Expenses (Millions of Dollars)']
data = np.array([[500, 10000, 350, 150], [750, 15000, 500, 200], [250, 5000, 200, 100], [400, 8000, 300, 100],
                 [650, 12000, 400, 300], [300, 6000, 250, 100], [600, 11000, 450, 250], [350, 7000, 300, 150],
                 [700, 14000, 600, 200], [450, 9000, 350, 150], [550, 10000, 400, 200]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.plot(line_labels, data[:, 0], color='b', label=data_labels[0])
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='r', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')
ax3.yaxis.set_major_locator(AutoLocator())
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.plot(line_labels, data[:, 3], color='m', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='m')
ax4.tick_params(axis='y', colors='m')
ax4.yaxis.set_major_locator(AutoLocator())
ax4.spines['right'].set_position(('outward', 120))

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.title('Charity and Nonprofit Organizations Performance Analysis')
fig.autofmt_xdate(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/278_202312311430.png')
plt.clf()
