import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Data Preparation
data = np.array([[22702, 333, 3.5, 65],
[16532, 1426, 3.6, 584],
[4145, 125, 2.9, 45],
[3891, 83, 3.6, 79],
[3305, 1393, 5.4, 179],
[2911, 66, 3.9, 62],
[2749, 67, 8.1, 58],
[2084, 60, 9.7, 48],
[1751, 38, 5.5, 74],
[1470, 25, 5.2, 35],
[1468, 146, 4.5, 267],
[1665, 51, 3.8, 114],
[1408, 46, 14.1, 42],
[3229, 211, 11.9, 84],
[1276, 130, 3.4, 89],
[1186, 275, 5.3, 150],
[937, 17, 3.5, 27],
[737, 8, 4.4, 10],
[940, 84, 13.7, 63],
[793, 36, 5.9, 70]])

line_labels = ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Canada', 'Australia', 'Russia', 'South Korea', 'Spain', 'Brazil', 'Mexico', 'Indonesia', 'Netherlands', 'Switzerland', 'Turkey', 'Saudi Arabia']
data_labels = ['GDP (in Billion USD)', 'Population (in Million)', 'Unemployment Rate (%)', 'Transport Infrastructure Spending (in Billion USD)']

# Plot Creation
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# Plot Data
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='b', alpha=0.7)
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='r')
ax3.scatter(line_labels, data[:,2], label=data_labels[2], color='g')

# Y-Axis Positioning for ax3
ax3.spines['right'].set_position(('outward', 60))

# Set Title
plt.title('Global Government and Public Policy Data: GDP, Population, Unemployment Rate, and Transport Infrastructure Spending')

# Set Labels
ax1.set_xlabel('Country')
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[2], color='g')

# Set AutoLocator
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Set Legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')

# Rotate X-Axis Labels
plt.xticks(rotation=90)

plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/151_202312310108.png')

# Clear the current figure's state
plt.clf()
