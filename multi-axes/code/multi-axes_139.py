import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Data
data_labels = ['Online Sales (Millions)', 'Retail Sales (Millions)', 'E-commerce Conversion Rate(%)', 'Average Order Value ($)']
line_labels = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys', 'Food and Beverage', 'Health and Beauty', 'Sports and Outdoor', 'Jewelry', 'Shoes']
data = np.array([[17, 35, 15, 120], [25, 50, 22, 75], [30, 20, 35, 20], [20, 40, 18, 200], [15, 30, 20, 50], [10, 50, 10, 60], [35, 45, 25, 80], [20, 25, 18, 100], [10, 20, 15, 150], [30, 40, 27, 70]])

# Create figure
fig = plt.figure(figsize=(28, 10))
ax1 = fig.add_subplot(111)
ax1.scatter(line_labels, data[:,0], color='g', alpha=1)
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='g')

# Overlay ax2 
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r')
ax2.set_ylabel(data_labels[1], color='r')

# Overlay ax3
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color='b', alpha=0.5)
ax3.spines["right"].set_position(("axes", 1.1))
ax3.set_ylabel(data_labels[2], color='b')

# Overlay ax4
ax4 = ax1.twinx()
ax4.bar([i-0.1 for i in range(len(line_labels))], data[:,3], width=0.2, color='purple', alpha=0.8)
ax4.spines["right"].set_position(("axes", 1.2))
ax4.set_ylabel(data_labels[3], color='purple')

# Adjusting y-axis range
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())

# Legends
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='lower right')
ax3.legend([data_labels[2]], loc='upper right')
ax4.legend([data_labels[3]], loc='lower left')

# Title
plt.title('E-commerce Vs. Retail Sales and Conversion Rates Analysis')

# Saving the figure
plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/260_202312311051.png')
plt.clf()
