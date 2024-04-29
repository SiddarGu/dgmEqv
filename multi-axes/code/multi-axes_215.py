import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# The following data is preprocessed
data_labels = ['Sales Volume (Units)', 'Revenue (Thousand Dollars)', 'Average Price per Unit (Dollars)']
line_labels = ['Electronics', 'Apparel', 'Home & Garden', 'Health & Beauty', 
               'Food & Beverage', 'Books', 'Office Supplies', 'Toys and games', 'Automotive']
data = np.array([(28500, 102250, 35),
                (46570, 150300, 32),
                (22700, 99800, 44),
                (39400, 163600, 41),
                (52440, 225000, 43),
                (35780, 93420, 26),
                (17350, 62740, 36),
                (23760, 105340, 44),
                (14510, 66540, 45)])

# Plotting the chart
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.bar(np.arange(len(line_labels)), data[:,0], label=data_labels[0], alpha=0.5)
ax1.set_ylabel(data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])
    ax3.spines['right'].set_position(('outward', 60))     
    ax3.set_ylabel(data_labels[2], color='g')

# Adding more y-axes as needed and adjusting their positions
for i in range(3, len(data_labels)):
    new_ax = ax1.twinx()
    new_ax.fill_between(line_labels, 0, data[:,i], alpha=0.3, label=data_labels[i])
    new_ax.spines['right'].set_position(('outward', 60*(i-1)))
    new_ax.set_ylabel(data_labels[i], color='b')
    new_ax.yaxis.set_major_locator(AutoLocator())

# Finishing touches
plt.title('Retail and E-commerce Product Category Sales Trends', fontsize=16)
plt.grid(True)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
if data.shape[1] > 2:
    ax3.legend(loc='lower left')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/81_2023122292141.png')
plt.cla()
