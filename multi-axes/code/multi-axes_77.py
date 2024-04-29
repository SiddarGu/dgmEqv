import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Prepare the data
raw_data = "Month,Trucks Dispatched,Revenue (in $000s),Fuel Consumed (in Gallons),Miles Covered (in 000s)/n January,220,5390,13000,357/n February,239,5850,13990,387/n March,268,6620,14540,405/n April,283,7020,15200,430/n May,330,7530,16500,450/n June,358,8260,17230,480/n July,372,9000,17980,495/n August,402,9450,18920,520/n September,425,9600,20000,543/n October,450,10200,21300,578/n November,480,10800,22500,600/n December,510,11300,23450,625"
lines = raw_data.split('/n')
data_labels = lines[0].split(',')
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])

# Create figure
fig = plt.figure(figsize=(25, 20))
ax1 = fig.add_subplot(111)

# Line Chart
ax1.plot(line_labels, data[:, 0], label=data_labels[1], color='red')

# Bar Chart
ax2 = ax1.twinx()
width = 0.3
ax2.bar(line_labels, data[:, 1], width=-width, align='edge', label=data_labels[2], color='blue', alpha=0.75)

# Area Chart
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:, 2], label=data_labels[3], color='green', alpha=0.5)

# Scatter Chart
ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:, 3], label=data_labels[4], color='purple')

# Label axises
ax1.set_xlabel(data_labels[0])
ax1.set_ylabel(data_labels[1], color='red')
ax2.set_ylabel(data_labels[2], color='blue')
ax3.set_ylabel(data_labels[3], color='green')
ax4.set_ylabel(data_labels[4], color='purple')

# Adjust the position of extra y-axes - ax3, ax4
ax3.spines['right'].set_position(('outward', 60))
ax4.spines['right'].set_position(('outward', 120))

# Auto adjust the y-axes using AutoLocator
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())

# Set the title
plt.title('Trucks Dispatched, Revenue, Fuel Consumption and Miles Covered Monthly Analysis')

# Arrange legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='center left')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/228_202312311051.png')
plt.clf()
