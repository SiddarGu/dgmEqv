import matplotlib.pyplot as plt
import numpy as np

# Pre-process the data
raw_data = 'Month,Trucks Shipped,Revenue (Millions),Average Shipping Time (Days)\n January,200,15,7\n February,180,14,7\n March,210,17,6\n April,230,19,5\n May,220,18,6\n June,240,20,7\n July,250,21,6\n August,240,20,7\n September,230,19,6\n October,220,17,7\n November,210,16,7\n December,200,15,7'
raw_lines = raw_data.split('\n')

data_labels = raw_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in raw_lines[1:]]
data = np.array([line.split(',')[1:] for line in raw_lines[1:]], dtype=float)

fig = plt.figure(figsize=(12, 9))
ax1 = fig.add_subplot(111)

# Plot the bar chart for the first column of the data
ax1.bar(line_labels, data[:,0], color='b', label=data_labels[0], alpha=0.7)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Plot the line chart for the second column of the data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Plot the line chart for the third column of the data
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(line_labels, data[:,2], color='g', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', labelcolor='g')

fig.autofmt_xdate()  # Rotate x-labels if too long

plt.title('Yearly Shipping Performance in Transportation and Logistics')
plt.grid()

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/136_202312310108.png')
plt.clf()
