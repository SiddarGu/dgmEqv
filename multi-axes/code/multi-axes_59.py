import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# transforming data
data_labels = ["Number of Deliveries", "Revenue (Millions of Dollars)", 
               "Average Delivery Time (Days)", "Average Distance (Miles)", 
               "Customer Satisfaction Score"]
line_labels = ["Air Freight", "Trucking", "Rail Freight", "Warehousing", 
               "Shipping", "Courier Services", "Logistics Services"]
data = np.array([[1000, 150, 1.5, 500, 80],
                 [5000, 300, 3, 200, 75],
                 [3000, 200, 2.5, 400, 85],
                 [2000, 250, 1, 100, 90],
                 [4000, 350, 2, 300, 85],
                 [7000, 400, 1.5, 150, 80],
                 [2500, 200, 2.5, 200, 85]])

plot_types = ['bar', 'line', 'line', 'line', 'line']

# begin creating multi-axes chart
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.grid(linestyle='--', alpha=0.6)

x = np.arange(data.shape[0])

# plot bar chart as the first column data
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax1.bar(x, data[:, 0], color='b', alpha=.7)
ax1.tick_params('y', colors='b')

# plot other data sequentially in the loop
colors = ['r', 'g', 'm', 'y']
for i in range(1, data.shape[1]):
    ax = ax1.twinx()
    color = colors[i-1]
    ax.plot(x, data[:, i], color=color)
    ax.set_ylabel(data_labels[i], color=color)
    ax.tick_params('y', colors=color)

    if i>1:
        ax.spines['right'].set_position(('outward', (i-1)*60))

plt.title('Performance Metrics of Transportation and Logistics Industry')
plt.xticks(x, line_labels, rotation=30)

# organize the legends
lines, labels = ax1.get_legend_handles_labels()
for ax in fig.axes[1:]:
    line, label = ax.get_legend_handles_labels()
    lines += line
    labels += label

ax1.legend(lines, labels, loc=0) 

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/316_202312311430.png')

# clear the current image state
plt.clf()
