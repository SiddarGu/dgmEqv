import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

data = np.array([
    [70.5, 140.2, 98.94],
    [72.3, 145.4, 105.14],
    [75.9, 150.7, 114.43],
    [76.8, 158.3, 121.57],
    [77.9, 164.2, 127.87],
    [80.2, 171.2, 137.3],
    [82.1, 178.7, 146.68],
    [83.7, 185.2, 154.94],
    [81.4, 194.1, 158.02],
    [78.6, 201.3, 158.22],
    [74.3, 207.8, 154.19],
    [71.7, 214.3, 153.62]
])

data_labels = ['Hotel Occupancy Rate (%)', 'Average Daily Rate ($)', 'Revenue Per Available Room ($)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# initiate chart size
plt.figure(figsize=(20,10))
# create subplot
ax1 = plt.subplot(111)
# plot line chart
ax1.plot(line_labels, data[:,0], label = data_labels[0], color = 'blue')
# set y-axis label
ax1.set_ylabel(data_labels[0], color = 'blue')
ax1.yaxis.set_major_locator(AutoLocator())
# create second ax
ax2 = ax1.twinx()
# plot second line chart
ax2.plot(line_labels, data[:,1], label = data_labels[1], color = 'green')
# set second y-axis label
ax2.set_ylabel(data_labels[1], color = 'green')
ax2.yaxis.set_major_locator(AutoLocator())
# create third ax
ax3 = ax1.twinx()
# shift the third ax to the right
ax3.spines['right'].set_position(('axes', 1.2))
# plot area chart
ax3.fill_between(line_labels, data[:,2], color = 'red', alpha = 0.4)
# set third y-axis label
ax3.set_ylabel(data_labels[2], color = 'red')
ax3.yaxis.set_major_locator(AutoLocator())
# create fourth ax
ax4 = ax1.twinx()
# shift the fourth ax to the right
ax4.spines['right'].set_position(('axes', 1.4))
# plot bar chart
ax4.bar(line_labels, data[:,2], alpha = 0.6, color = 'purple', width = 0.4)
# set fourth y-axis label
ax4.set_ylabel(data_labels[2], color = 'purple')
ax4.yaxis.set_major_locator(AutoLocator())
# set x-axis grid
plt.grid(axis = 'x')
# set title
plt.title('An Overview of Hospitality Revenue and Occupancy Trends')
# set legend
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'lower left')
ax3.legend(loc = 'upper right')
ax4.legend(loc = 'lower right')
# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/72_2023122292141.png')
# clear
plt.clf()
