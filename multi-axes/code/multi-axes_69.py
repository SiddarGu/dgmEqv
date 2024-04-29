import matplotlib.pyplot as plt
import numpy as np

# Preprocess the Data
data_string = "Month,Total Deliveries, Average Cost (Millions of Dollars), Transport Time (Hours)/n January,500,13.2,47/n February,540,15.6,43/n March,590,17.8,39/n April,630,18.5,36/n May,670,20.2,33/n June,690,21.4,35/n July,710,22.8,37/n August,740,24.2,34/n September,780,25.1,31/n October,810,28.0,27/n November,820,29.2,29/n December,840,30.0,32"
raw_data = [item.split(',') for item in data_string.split('/n ')]
data_labels = raw_data[0][1:]
data = np.array([list(map(float,item[1:])) for item in raw_data[1:]])
line_labels = [item[0] for item in raw_data[1:]]

# Plot the Data
plt.figure(figsize=(20,10))
ax1 = plt.subplot(111)

# Plot Bar Chart
ax1.bar(line_labels, data[:,0], alpha=0.6, color='b', label=data_labels[0])

# Plot Line Chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'g-', label=data_labels[1])

# Plot another Line Chart
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], 'r-', label=data_labels[2])

# Formatting
ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')
ax3.spines['right'].set_position(('outward', 60))

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='center left')
ax3.legend(loc='upper right')

# Title
plt.title('Monthly Performance Analysis in Transportation and Logistics')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/258_202312311051.png')
plt.clf()
