
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ["Volume Handled (Millions of Tonnes)", "Revenue (Billions of Dollars)", "Average Delivery Time (Minutes)"]
line_labels = ["Freight", "Passenger Transport", "Warehousing", "Shipping", "Courier Services", "Air Transport", "Rail Transport", "Trucking", "Pipeline Transport", "Logistics Services"]
data = np.array([[7.2, 79.9, 330],
                 [10.9, 31.1, 234],
                 [5.0, 65.9, 300],
                 [6.5, 30.4, 198],
                 [14.9, 27.0, 396],
                 [7.1, 72.5, 186],
                 [11.3, 81.8, 204],
                 [12.2, 30.0, 330],
                 [6.0, 72.5, 420],
                 [6.0, 76.3, 300]])

# Create figure
plt.figure(figsize = (15,10))

# Plot data
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], width = 0.2, color = 'blue', alpha = 0.7)
ax1.set_ylabel(data_labels[0], color = 'blue')
ax1.set_xlabel("Category")
ax1.set_title("Transportation and Logistics Performance Analysis: Volume, Revenue, and Delivery Time")
ax1.grid()
ax1.tick_params(axis = 'y', colors = 'blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], linestyle = '-', marker = 'o', color = 'red')
ax2.set_ylabel(data_labels[1], color = 'red')
ax2.tick_params(axis = 'y', colors = 'red')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], linestyle = '-', marker = 'o', color = 'green')
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylabel(data_labels[2], color = 'green')
ax3.tick_params(axis = 'y', colors = 'green')

# Adjust the range of all axes
for ax in [ax1, ax2, ax3]:
    ax.locator_params(axis = 'y', nbins = 5)

# Show the legends
ax1.legend(labels = [data_labels[0]], loc = 'upper left')
ax2.legend(labels = [data_labels[1]], loc = 'upper right')
ax3.legend(labels = [data_labels[2]], loc = 'upper right')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/12_202312251608.png", dpi = 300)

# Clear current image state
plt.clf()