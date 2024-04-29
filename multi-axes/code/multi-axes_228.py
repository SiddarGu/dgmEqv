import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Parse the data
data_info = ["Government Body,Population Served (Millions),Budget Allocation (Billions),Programs Implemented",
             "Federal Government,331,4.8,200",
             "State Government,39,1.9,150",
             "Local Government,8.5,0.85,70",
             "Defense Department,331,3.4,180",
             "Education Department,56,1.2,210",
             "Health Department,331,1.9,320",
             "Labor Department,160,0.7,90",
             "Homeland Security,331,1.5,175",
             "Justice Department,331,2.8,205",
             "Housing and Urban Development,331,0.4,220"]

data_labels = ['Population Served (Millions)', 'Budget Allocation (Billions)', 'Programs Implemented']
data = np.array([list(map(float, x.split(',')[1:])) for x in data_info[1:]])
line_labels = [x.split(',')[0] for x in data_info[1:]]

# Create figure
fig = plt.figure(figsize=(25, 15))
ax1 = fig.add_subplot(111)

# Plot bar chart
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.6, label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r', marker='o', label=data_labels[1])

# Create another axis for the third column
if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.fill_between(line_labels, data[:, 2], color='g', alpha=0.3, label=data_labels[2])
    ax3.spines['right'].set_position(('outward', 60))  

# Setup colors and labels
colors = ['blue', 'red', 'green']
for ax, color, label in zip([ax1, ax2, ax3], colors, data_labels):
    ax.yaxis.label.set_color(color)
    ax.tick_params(axis='y', colors=color)
    ax.set_ylabel(label)
    ax.yaxis.set_major_locator(AutoLocator())

# Setup legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
if data.shape[1] > 2:
    ax3.legend(loc='center right')

plt.title('Comparative Analysis of Government Bodies: Population, Budget, and Program Implementation')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/149_202312310108.png')
plt.close()
