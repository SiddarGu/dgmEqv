import matplotlib.pyplot as plt
import numpy as np

# Parse the data
data_str = """City,Total Listings,Sold Listings,Average House Price($),Average Days on Market
New York,4040,1849,725000,95
Los Angeles,3525,1724,825000,82
Chicago,2759,1440,350000,75
Houston,3298,1921,275000,60
Philadelphia,1985,1144,250000,72
Phoenix,2473,1894,325000,49
San Antonio,2133,1591,265000,55
San Diego,2964,1741,650000,67
Dallas,3121,1883,355000,57
Austin,2860,1739,400000,49"""

lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])

# Create the multi-axes charts
fig = plt.figure(figsize=(15, 10))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color = 'b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color = 'b')
ax1.yaxis.label.set_color('b')
ax1.yaxis.set_tick_params(colors='b')

ax2 = ax1.twinx() 
ax2.plot(line_labels, data[:,1], color = 'g', alpha=0.6, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color = 'g')
ax2.yaxis.label.set_color('g')
ax2.yaxis.set_tick_params(colors='g')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color = 'r', alpha=0.6, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color = 'r')
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.label.set_color('r')
ax3.yaxis.set_tick_params(colors='r')

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color = 'purple', alpha=0.3, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color = 'purple')
ax4.spines['right'].set_position(('outward', 120))
ax4.yaxis.label.set_color('purple')
ax4.yaxis.set_tick_params(colors='purple')

# Set the legend and grid
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower left')

plt.title('Real Estate Market Performance: Listings, Sales, Prices, and Market Time')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/66_2023122292141.png')
plt.cla()
