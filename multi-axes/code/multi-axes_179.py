import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import AutoLocator

# Data
data = [["Football", 200, 13, 60], ["Baseball", 110, 11, 30], ["Basketball", 120, 7, 55], ["Hockey", 100, 4, 70], ["Tennis", 90, 5, 30], ["Golf", 80, 6, 20], ["Motor Sports", 60, 2, 50], ["Boxing", 50, 1, 150], ["Wrestling", 40, 1, 50], ["E-Sports", 250, 1, 20]]
data_labels = ['Audience (Millions)', 'Revenue (Billions of Dollars)','Average Ticket Price (Dollars)']
line_labels = ['Football', 'Baseball', 'Basketball', 'Hockey', 'Tennis', 'Golf', 'Motor Sports', 'Boxing', 'Wrestling', 'E-Sports']

data = np.array(data)

# Create figure
fig = plt.figure(figsize=(30, 15))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 1], width=0.4, color='g', align='center', alpha=0.6)
ax1.set_ylabel(data_labels[0])
ax1.set_xlabel('Category')
ax1.yaxis.label.set_color('g')

# Create second axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 2], 'r-')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('r')

# Create third axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))      
ax3.plot(line_labels, data[:, 3], 'b-')
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('b')

# label
plt.title('Entertainment Category Analysis: Audience, Revenue, and Ticket Price')

# set auto locator
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Display legend
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='center right')

# Grid
ax1.grid()

# Save and clear figure
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/253_202312311051.png')
plt.clf()
