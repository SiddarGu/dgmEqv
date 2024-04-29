import matplotlib.pyplot as plt
import numpy as np
import random

data = np.array([
    [10000, 500000, 100],
    [15000, 750000, 150],
    [5000, 750000, 300],
    [2000, 200000, 100],
    [10000, 500000, 50],
    [5000, 250000, 50],
    [8000, 800000, 100],
    [3000, 300000, 100],
    [6000, 600000, 100],
    [4000, 400000, 100]
])
line_labels = ['Electronics', 'Automotive', 'Pharmaceuticals', 'Furniture', 'Food and Beverage', 'Clothing and Textiles', 'Machinery and Equipment', 'Chemicals', 'Metal and Mining', 'Paper and Packaging']
data_labels = ['Production Quantity (Units)', 'Production Cost (Dollars)', 'Average Sale Price']

fig = plt.figure(figsize=(24, 12))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], alpha=0.8, color='r', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='r')
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'g-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='b', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='b')

fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.grid()
plt.title('Manufacturing and Production Analysis: Quantity, Cost, and Sale Price')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/274_202312311430.png')
plt.close(fig)
