
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = np.array(['Number of Available Homes', 'Average Sale Price (Dollars)', 'Average Number of Days on Market'])
line_labels = np.array(['Single Family Homes', 'Condos', 'Townhomes', 'Multi-Family Homes', 'Mobile Homes'])
data = np.array([[7800, 170000, 60], [4500, 140000, 45], [3000, 90000, 35], [2500, 120000, 50], [1500, 60000, 40]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:, 0], color='b', width=0.15, alpha=0.8, label=data_labels[0])
ax1.set_xlabel('Category', fontsize=15)
ax1.set_ylabel(data_labels[0], color='b', fontsize=15)
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', marker='o', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g', fontsize=15)
ax2.tick_params(axis='y', labelcolor='g')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='r', marker='^', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r', fontsize=15)
ax3.tick_params(axis='y', labelcolor='r')
ax3.spines['right'].set_position(('axes', 1.15))

ax1.legend(bbox_to_anchor=(0.7, 0.75), loc='upper left', borderaxespad=0.)
ax2.legend(bbox_to_anchor=(0.7, 0.7), loc='upper left', borderaxespad=0.)
ax3.legend(bbox_to_anchor=(0.7, 0.65), loc='upper left', borderaxespad=0.)

ax1.xaxis.set_major_locator(ticker.MaxNLocator(6))
ax1.yaxis.set_major_locator(ticker.MaxNLocator(6))
ax2.yaxis.set_major_locator(ticker.MaxNLocator(6))
ax3.yaxis.set_major_locator(ticker.MaxNLocator(6))

plt.title('Real Estate and Housing Market: Inventory, Pricing, and Duration Overview', fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/4_2023122261325.png')
plt.clf()