import matplotlib.pyplot as plt
import numpy as np

# Data preparation
data_str = """City,Number of Properties Sold,Average Sale Price (Thousands),New Listings,Unsold Inventory
New York,55000,900,70000,10000
Los Angeles,50000,750,60000,8000
Chicago,40000,415,50000,7000
Houston,38000,255,45000,6000
Phoenix,37000,280,43000,5500
Philadelphia,35000,210,41000,5000
San Antonio,34000,195,39000,4700
San Diego,33000,610,38000,6000
Dallas,32000,280,37000,4000
San Jose,31000,1030,36000,5000"""
lines = data_str.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines[1:]])

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(15, 10))

# First plot (bar)
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

# Second plot (line)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r')
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params('y', colors='r')

# Third plot (scatter)
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='g')
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params('y', colors='g')

# Fourth plot (area)
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], 0, color='c', alpha=0.4)
ax4.set_ylabel(data_labels[3], color='c')
ax4.tick_params('y', colors='c')

# Adjust the right margin and spacing of the plots
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# Set x-axis labels
ax1.set_xticklabels(line_labels, rotation=90)

# Title and legend
plt.title('Real Estate Trends in Major US Cities')

# Custom legend
fig.legend(data_labels, loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/256_202312311051.png')
plt.clf()
