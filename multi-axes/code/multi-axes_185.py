import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

# Transform the data
data_labels = ['Food Sold (Tonnes)', 'Beverage Sold (Litres)', 'Daily Revenue (Thousands of Dollars)', 'Customer Visits']
line_labels = ['McDonald\'s', 'Starbucks', 'Subway', 'Burger King', 'Dunkin Donuts', 'Wendy\'s', 'Pizza Hut', 'KFC', 'Domino\'s Pizza', 'Taco Bell']
data = np.array([
    [5684, 8907, 3402, 18904],
    [1877, 4958, 2262, 28647],
    [2031, 3679, 2026, 20367],
    [2650, 4859, 1792, 11477],
    [1547, 4488, 2044, 18457],
    [2353, 4021, 1573, 11254],
    [3792, 2898, 1654, 10194],
    [3465, 4068, 1670, 13974],
    [2834, 1987, 1722, 14103],
    [2954, 4023, 1784, 14408]
])

# Create figure
fig = plt.figure(figsize=(26, 18))
ax1 = plt.subplot(111)

# Bar chart
ax1.bar(np.arange(data.shape[0])-0.2, data[:,0], width=0.2, color='b', alpha=0.7, align='center')
ax1.set_xlabel('Restaurant')
ax1.set_ylabel(data_labels[0], color='b')

# Area chart
ax2 = ax1.twinx()
ax2.fill_between(np.arange(data.shape[0]), 0, data[:,1], color='r', alpha=0.5)
ax2.set_ylabel(data_labels[1], color='r')

# Bar chart
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 80))
ax3.bar(np.arange(data.shape[0]), data[:,2], width=0.2, color='g', alpha=0.7, align='center')
ax3.set_ylabel(data_labels[2], color='g')

# Line chart
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 160))
ax4.plot(np.arange(data.shape[0]), data[:,3], color='c', linestyle='-')
ax4.set_ylabel(data_labels[3], color='c')

plt.title('Food and Beverage Sale and Customer Visits in Leading Restaurants')
plt.xticks(np.arange(data.shape[0]), line_labels, rotation=45)

# Add legends
ax1.legend([mlines.Line2D([], [], color='b')], [data_labels[0]], loc='upper left')
ax2.legend([mlines.Line2D([], [], color='r', alpha=0.5)], [data_labels[1]], loc='upper right')
ax3.legend([mlines.Line2D([], [], color='g')], [data_labels[2]], loc='center left')
ax4.legend([mlines.Line2D([], [], color='c')], [data_labels[3]], loc='center right')

plt.grid()
plt.autoscale()
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/196_202312311051.png')
plt.clf()
