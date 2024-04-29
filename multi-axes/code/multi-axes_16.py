
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Costs (Dollars)', 'Labor Hours', 'Production Output (Units)']
line_labels = ['Automotive Parts', 'Appliances', 'Building Materials', 'Fabrics', 'Electronics', 'Glassware', 'Machinery', 'Metals', 'Plastics']

data = np.array([[2300,164500,9050],
                 [1130,26750,3300],
                 [760,12050,3300],
                 [450,25200,5500],
                 [960,49200,6100],
                 [780,19000,4500],
                 [970,16300,3600],
                 [510,21000,4400],
                 [880,23400,5700]])

# Create figure
fig = plt.figure(figsize=(15,10))

# Plot data
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,2], color='b', alpha=0.6, width=0.8)

ax2 = ax1.twinx() 
ax2.plot(line_labels, data[:,1], color='r', linestyle='-', marker='o')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,0], color='g', linestyle='-', marker='s')

# Set label for y-axes
ax1.set_ylabel(data_labels[2], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[0], color='g')

# Place different y-axes
ax3.spines['right'].set_position(('axes', 1.1))

# Adjust y-axes range
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Add title
plt.title('Manufacturing and Production: Production Output, Costs, and Labor Hours')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Show legend
ax1.legend(data_labels[2], loc=2)
ax2.legend(data_labels[1], loc=1)
ax3.legend(data_labels[0], loc=4)

# Add background grids
ax1.grid(linestyle='--', color='grey', linewidth=1)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/26_2023122261325.png')

# Clear the current image state
plt.close()