import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transforming the given data
data_labels = ['Operating Profit (Millions)', 'Revenue (Billions)', 'Net Profit (Millions)']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([[2640, 58.8, 1100], [2770, 61.4, 1250], [2980, 66.1, 1360], [3200, 69.3, 1480], [3480, 72.7, 1620], [3800, 76.4, 1760], [4170, 81.2, 1930]])

fig = plt.figure(figsize=(20,7))
ax1 = fig.add_subplot(111)

ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0], alpha=0.6)
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1], alpha=0.6)
ax2.set_ylabel(data_labels[1], color='r')
ax2.yaxis.set_major_locator(AutoLocator())

if data.shape[1]>2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.bar(line_labels, data[:,2], color='g', label=data_labels[2], alpha=0.6)
    ax3.set_ylabel(data_labels[2], color='g')
    ax3.yaxis.set_major_locator(AutoLocator())

fig.suptitle('Analysis of Business Profitability and Revenue Trends', fontsize=20)
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/158_202312310108.png")
plt.show()
plt.clf()
