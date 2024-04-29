import matplotlib.pyplot as plt
import numpy as np

#Transform the data
data_string = 'Month,Number of Deliveries,Total Distance Covered (in KM),Fuel Consumption in Liters,Delivery Efficiency (in %)\n January,570,9500,4500,85\n February,600,9750,4250,87\n March,650,11000,4650,84\n April,700,10875,4750,86\n May,750,11125,4810,87\n June,810,11850,5010,83\n July,870,12750,5340,82\n August,920,13250,5600,80\n September,890,12900,5400,81\n October,810,12500,5005,82\n November,780,11750,4700,85\n December,630,10000,4200,88'
data_lines = data_string.split('\n')
line_labels = [line.split(',')[0].strip() for line in data_lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in data_lines[1:]])
data_labels = data_lines[0].split(',')[1:]

# Create figure
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

# Plot first column
line1 = ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0],color='b')

# Plot second column
ax2 = ax1.twinx()
bar1 = ax2.bar(line_labels, data[:,1], color='g', alpha=0.6, label=data_labels[1])
ax2.set_ylabel(data_labels[1],color='g')

# Plot third column
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], alpha=0.4, color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2],color='r')

# Plot fourth column
ax4 = ax1.twinx()
scatter1 = ax4.scatter(line_labels, data[:,3], color='black', label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3],color='black')

# Set Title
plt.title('Month-wise Delivery Performance and Efficiency')

# Set Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
fig.legend(loc='upper left', bbox_to_anchor=(0.5, 0.9))
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
fig.legend(loc='upper right', bbox_to_anchor=(1.0, 0.9))

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/74_2023122292141.png')
plt.clf()
