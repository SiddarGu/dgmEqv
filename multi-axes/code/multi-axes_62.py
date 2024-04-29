import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator 

data_labels = ['Online Sales (Millions)', 'In-store Sales (Millions)', 'Returned Items (%)', 'Items Sold (Millions)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([[45, 55, 3, 40], [46, 57, 2, 42], [49, 59, 3, 45], [52, 54, 4, 47], [55, 58, 5, 50], [57, 56, 6, 52], [59, 60, 5, 55], [61, 62, 4, 57], [63, 64, 3, 59], [65, 66, 3, 61], [68, 70, 2, 64], [75, 80, 2,72]])

fig = plt.figure(figsize=(24, 12))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='red', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='red')
ax1.yaxis.set_tick_params(labelcolor='red')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='blue', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='blue')
ax2.yaxis.set_tick_params(labelcolor='blue')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='green', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60)) 
ax3.set_ylabel(data_labels[2], color='green')
ax3.yaxis.set_tick_params(labelcolor='green')
ax3.yaxis.set_major_locator(AutoLocator())

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color='purple', alpha=0.5, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color='purple')
ax4.yaxis.set_tick_params(labelcolor='purple')
ax4.yaxis.set_major_locator(AutoLocator())

fig.suptitle('Retail and E-commerce: A Comparative Analysis of Online and In-store Sales', fontsize=20)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.1))
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/129_202312310108.png")
plt.clf()
