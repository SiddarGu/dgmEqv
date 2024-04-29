# Import necessary Python libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Data String
data_str = 'Category,Energy Generated (MW),Energy Consumed (MW),Energy Efficiency (%)\n Coal,1000,700,70\n Natural Gas,1200,900,75\n Nuclear,800,750,93\n Hydroelectric,600,550,92\n Solar,150,120,80\n Wind,400,380,95\n Biomass,200,180,90\n Geothermal,100,90,90'

# Preprocess Data
data_arr = np.array([line.split(',') for line in data_str.split('\n')]).T
line_labels, data_labels = data_arr[0,1:], data_arr[1:,0]
data = np.array(data_arr[1:,1:], dtype=float)

# Initialize Figure
fig = plt.figure(figsize=(22,12))
ax1 = fig.add_subplot(111)

# Plotting Bar Chart
ax1.bar(line_labels, data[0], width=0.2, color='b', alpha=0.5, label=data_labels[0])

# Plotting Line Chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[1], color='g', marker='o', label=data_labels[1])

# Plotting Scatter Chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[2], color='r', alpha=0.6, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))  

# Set the y-axis labels
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')

# Set title
plt.title('Energy Generation and Efficiency Comparison')

# Show Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Grid background
ax1.grid()

# Autolocator
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Save the figure
fig_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/299_202312311430.png'
plt.tight_layout()
plt.savefig(fig_path, format='png')

# Clear the figure
plt.clf()
