

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# define labels
data_labels = ["Number of Customers", "Total Revenue (Millions of Dollars)", "Average Basket Size (Dollars)", "Average Customer Spend (Dollars)"]
line_labels = ["Online Shopping", "Grocery Shopping", "Department Store", "Clothing Store", "Electronic Store", "Home Decor Store"]

# define data
data = np.array([[1000, 9000, 25, 90],
                 [1500, 7000, 20, 47],
                 [2000, 11000, 30, 55],
                 [1700, 8000, 24, 47],
                 [1000, 6000, 40, 60],
                 [1200, 3000, 20, 25]])

# Create figure
plt.figure(figsize=(15, 10))

# Create the first plot
ax1 = plt.subplot(111)
ax1.bar(np.arange(data.shape[0]), data[:, 0], label=data_labels[0], width=0.25, color='C0')
ax1.set_xticks(np.arange(data.shape[0]))
ax1.set_xticklabels(line_labels)
ax1.set_ylabel(data_labels[0], color='C0')
ax1.tick_params(axis='y', labelcolor='C0')
ax1.set_title('Retail and E-commerce Sales Performance Analysis')

# Create the second plot
ax2 = ax1.twinx()
ax2.plot(np.arange(data.shape[0]), data[:, 1], label=data_labels[1], marker='o', color='C1')
ax2.set_xlim(-0.25, data.shape[0]-0.75)
ax2.set_ylabel(data_labels[1], color='C1')
ax2.tick_params(axis='y', labelcolor='C1')

# Create the third plot
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(np.arange(data.shape[0]), data[:, 2], label=data_labels[2], marker='^', color='C2')
ax3.set_ylabel(data_labels[2], color='C2')
ax3.tick_params(axis='y', labelcolor='C2')

# Create the fourth plot
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('axes', 1.2))
ax4.plot(np.arange(data.shape[0]), data[:, 3], label=data_labels[3], marker='s', color='C3')
ax4.set_ylabel(data_labels[3], color='C3')
ax4.tick_params(axis='y', labelcolor='C3')

# Set grids
ax1.grid(axis='y')

# Set autolocator
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()
ax4.autoscale_view()

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/29_2023122261325.png')

# Clear image
plt.clf()