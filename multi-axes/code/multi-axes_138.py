import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Define the data
data_labels = ['Total Sales (in Thousands)', 'Online Sales (in Thousands)', 'Average Transaction Value (Dollars)', 'Customer Satisfaction Index (out of 10)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([
    [5120, 2530, 68, 8.2],
    [5370, 2900, 72, 8.5],
    [6030, 3310, 74, 8.6],
    [5870, 3240, 70, 8.4],
    [5990, 3110, 69, 8.3],
    [6520, 3600, 73, 8.7],
    [6930, 3850, 75, 8.6],
    [7080, 3980, 76, 8.8],
    [7180, 4160, 77, 8.9],
    [7320, 4320, 79, 8.8],
    [7890, 4700, 82, 9.1],
    [8230, 5210, 84, 9.2]
])

fig = plt.figure(figsize=(25, 15))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color='blue', alpha=0.75, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')
ax1.yaxis.set_minor_locator(AutoMinorLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='red', alpha=0.75, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')
ax2.spines['right'].set_position(('outward', 60))
ax2.yaxis.set_minor_locator(AutoMinorLocator())

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='green', alpha=0.75, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines['right'].set_position(('outward', 120))
ax3.yaxis.set_minor_locator(AutoMinorLocator())

ax4 = ax1.twinx()
sc = ax4.scatter(line_labels, data[:, 3], color='purple', alpha=0.75, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.spines['right'].set_position(('outward', 180))
ax4.yaxis.set_minor_locator(AutoMinorLocator())

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.grid(True)
plt.title('Monthy Retail Sales and E-Commerce Trends')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/147_202312310108.png')
plt.clf()
