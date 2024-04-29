import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Data
line_labels = ['Soft Drinks', 'Snack Foods', 'Alcoholic Beverages', 'Packaged Foods', 'Dairy Products', 'Frozen Foods', 
               'Bakery Products', 'Candy and Confections', 'Canned and Packaged Foods', 'Condiments and Sauces']
data_labels = ['Sales (Millions of Dollars)', 'Revenue (Millions of Dollars)', 'Market Share']
data = np.array([[864, 167, 28.36], [570, 285, 18.18], [510, 204, 16.36], [400, 200, 12.73],
                 [300, 150, 9.55], [240, 120, 7.64], [180, 90, 5.73], [150, 75, 4.78],
                 [120, 60, 3.82], [60, 30, 1.91]])

fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:,0], alpha=0.7, color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.set_xlabel('Category')
ax1.tick_params(axis='y', colors='b')

# Line chart 1
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'go-', alpha=0.7, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')

# Line chart 2
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], 'ro-', alpha=0.7, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')

axes = [ax1, ax2, ax3]
# Adding AutoMinorLocator
for ax in axes:
    ax.yaxis.set_minor_locator(AutoMinorLocator())  
# Adding legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Adding title and grid
plt.title('Food and Beverage Industry: Sales, Revenue, and Market Share')
plt.grid()

plt.tight_layout()

# Saving figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/271_202312311430.png')
plt.clf()
