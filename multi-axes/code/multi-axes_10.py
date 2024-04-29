

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_labels = ['Sale (Dollars)', 'Average of State Bottle Retail', 'Bottles Sold']
line_labels = ['Soft Drinks', 'Fruit Juice', 'Alcoholic Beverages', 'Milk', 'Tea and Coffee', 'Dairy Products', 'Water', 'Energy Drinks', 'Ready to Drink Beverages']
data = np.array([[76000, 94500, 14453, 595],
                 [56600, 89000, 16876, 634],
                 [84400, 100000, 25600, 767],
                 [98000, 115000, 19082, 742],
                 [59900, 110000, 14834, 786],
                 [45800, 98700, 17660, 848],
                 [89000, 98000, 19000, 741],
                 [69600, 70000, 9456, 452],
                 [60000, 70000, 14500, 750]])

plot_types = ['bar', 'line', 'area', 'scatter']

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(111)

ax1.bar(x=line_labels, height=data[:, 0], color='b', width=0.2, alpha=1.0, label=data_labels[0])
ax1.set_xlabel('Category', fontsize=14)
ax1.set_ylabel(data_labels[0], fontsize=14, color='b')
ax1.set_title('Food and Beverage Industry: Volume, Revenue, and Pricing Trends', fontsize=16)
ax1.tick_params(axis='y', labelcolor='b', labelsize=13)
ax1.grid(axis='y')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], fontsize=14, color='r')
ax2.tick_params(axis='y', labelcolor='r', labelsize=13)

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], 'g-', label=data_labels[2])
ax3.set_ylabel(data_labels[2], fontsize=14, color='g')
ax3.tick_params(axis='y', labelcolor='g', labelsize=13)
ax3.spines['right'].set_position(('outward', 60))

ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 1))
ax2.legend(loc='upper left', bbox_to_anchor=(0.4, 1))
ax3.legend(loc='upper left', bbox_to_anchor=(0.8, 1))

ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/4_2023122270030.png')
plt.clf()