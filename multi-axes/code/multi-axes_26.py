
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Number of Stores', 'Sales (Millions of Dollars)', 'Average Customer Spend']
data = np.array([[4500, 78800, 400], [2500, 36000, 450], [650, 17500, 650], [3000, 90000, 500], [5500, 70000, 200], [800, 24000, 750], [4000, 80000, 400]])
line_labels = ['Grocery Stores', 'Department Stores', 'Specialty Stores', 'Online Retailers', 'Discount Stores', 'Boutiques', 'E-commerce Platforms']

# Create figure before plotting
plt.figure(figsize=(15, 10))
ax1 = plt.subplot(111)

# Plot the data with the type of multi-axes chart
# Plot the first column of data array, i.e., data[:,0]
ax1.bar(line_labels, data[:,0], width=0.8, color='#FFC222', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='#FFC222')
ax1.tick_params(axis='y', labelcolor='#FFC222')

# Plot the second column of data array, i.e. data[:,1], after using twinx to overlay a new ax, named as ax2 on the first plot
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], marker='o', linestyle='-', color='#4A90E2')
ax2.set_ylabel(data_labels[1], color='#4A90E2')
ax2.tick_params(axis='y', labelcolor='#4A90E2')

# If possible, plot the third column of data array, i.e. data[:,2], after using another twinx, named as ax3 to overlay another new ax on the first plot
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='#9013FE')
ax3.set_ylabel(data_labels[2], color='#9013FE')
ax3.tick_params(axis='y', labelcolor='#9013FE')

# Seperate different y-axes
ax3.spines['right'].set_position(('axes', 1.1))

# Show the legends of all plots at different positions
ax1.legend(['Number of Stores'], loc='upper left')
ax2.legend(['Sales (Millions of Dollars)'], loc='upper right')
ax3.legend(['Average Customer Spend'], loc='lower right')

# Drawing techniques such as background grids can be used
ax1.grid(linestyle='--', alpha=0.6)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax1.autoscale(enable=True, axis='y', tight=True)
ax2.autoscale(enable=True, axis='y', tight=True)
ax3.autoscale(enable=True, axis='y', tight=True)

# Label all axes
ax1.set_xlabel('Categories')
ax1.set_title('Retail and E-commerce Performance Analysis: Store Counts, Sales, and Customer Spend')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/25_2023122261325.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/25_2023122261325.png')

# Clear the current image state at the end of the code
plt.clf()