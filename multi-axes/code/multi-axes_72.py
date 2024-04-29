import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# process data
raw_data = 'Department,Number of Employees,Training Hours,Average Years of Service,Turnover Rate (%)\n Human Resources,75,25,6,12\n Finance,114,30,8,10\n Marketing,130,20,5,15\n Sales,200,15,3,20\n IT,85,40,9,8\n Manufacturing,500,35,10,7\n Logistics,120,25,4,18\n Customer Service,210,15,5,23'
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [l.split(',')[0] for l in lines[1:]]
data = np.array([list(map(int, l.split(',')[1:])) for l in lines[1:]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

# Plot bar chart
ax1.bar(line_labels, data[:,0], color='blue', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')

# Plot line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')

# Plot scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='green', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines["right"].set_position(("axes", 1.2))

# Plot area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color="purple", alpha=0.3, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.spines["right"].set_position(("axes", 1.4))

# Autolocator for y-axies
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

# Add grid
ax1.grid()

# Title
plt.title('Human Resources Overview: Employee Data and Management Insights')

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='center left')

# Save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/222_202312311051.png')

# Clear image
plt.clf()
