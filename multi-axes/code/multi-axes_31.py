
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = np.array(['Number of Homes Sold','Average Sale Price (Dollars)','Average Days on Market'])
line_labels = np.array(['Single Family Homes', 'Townhouses', 'Condos', 'Multi-Family Homes', 'Mobile Homes', 'Vacant Land'])
data = np.array([[86000, 347000, 54], [12000, 202000, 41], [19000, 183000, 36], [9000, 420000, 49], [3000, 150000, 33], [6000, 60000, 60]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:, 0], width=0.2, color='red', alpha=0.8, label=data_labels[0])
ax1.set_ylim(0, max(data[:, 0] + 1000))
ax1.set_ylabel('Number of Homes Sold', color='red', fontsize=14)
ax1.tick_params(axis='y', labelcolor='red')
ax1.set_title('Real Estate and Housing Market: Sales Figures and Price Analysis', fontsize=20)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], linestyle='--', marker='o', color='blue', label=data_labels[1])
ax2.set_ylabel('Average Sale Price (Dollars)', color='blue', fontsize=14)
ax2.tick_params(axis='y', labelcolor='blue')
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('data', 1.5))
ax3.plot(line_labels, data[:, 2], linestyle='-', marker='s', color='green', label=data_labels[2])
ax3.set_ylabel('Average Days on Market', color='green', fontsize=14)
ax3.tick_params(axis='y', labelcolor='green')

ax1.legend(loc='lower left', fontsize=13)
ax2.legend(loc='upper left', fontsize=13)
ax3.legend(loc='upper right', fontsize=13)

ax1.grid(True, linestyle='-.')
ax1.set_xlabel('Type of Property', fontsize=14)

for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_ticks_position('bottom')
    ax.autoscale(enable=True, axis='x', tight=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/49_2023122261325.png')
plt.cla()