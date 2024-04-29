
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

data_labels = ['Workers per Facility (Thousands)', 'Revenue (Millions of Dollars)', 'Average Cost per Unit (Dollars)', 'Units Produced']
line_labels = ['Automotive Parts', 'Aircraft Parts', 'Electronics', 'Appliances', 'Home Supplies', 'Machinery', 'Furniture', 'Pharmaceuticals']
data = np.array([[2.5, 5460, 23.5, 35000], [1.3, 7200, 100, 3000], [4.1, 8200, 32.5, 25000], [3.2, 2400, 150, 800], [1.4, 1700, 17, 9500], [3.8, 6000, 90, 4500], [2.6, 3700, 60, 2500], [3.9, 11000, 20, 40000]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.set_xticks(np.arange(len(line_labels)))
ax1.set_xticklabels(line_labels)
ax1.bar(line_labels, data[:, 0], color='blue', alpha=0.8, label=data_labels[0])

ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(color='gray', linestyle='-', linewidth=0.5)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='red', marker='o', linestyle='--', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')
ax2.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.bar(line_labels, data[:, 2], color='green', alpha=0.4, label=data_labels[2], width=0.3, bottom=data[:, 0])
ax3.set_ylabel(data_labels[2], color='green')
ax3.tick_params(axis='y', labelcolor='green')
ax3.spines['right'].set_position(('axes', 1.1))

ax4 = ax1.twinx()
ax4.plot(line_labels, data[:, 3], color='orange', marker='o', linestyle='--', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='orange')
ax4.tick_params(axis='y', labelcolor='orange')
ax4.spines['right'].set_position(('axes', 1.2))

plt.title('Manufacturing and Production Performance Overview')
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3 + lines4, labels + labels2 + labels3 + labels4, loc='upper left', bbox_to_anchor=(0.02, 0.9))

ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()
ax4.autoscale_view()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/7_202312251608.png')
plt.clf()