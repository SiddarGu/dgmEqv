import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_text = "Category,Attendance (Number of People),Revenue (Millions of Dollars),Average Ticket Price (Dollars)\n Soccer,50000,125,10\n Basketball,25000,75,5\n Baseball,30000,100,7\n Hockey,20000,50,3\n Tennis,10000,25,2\n Golf,15000,50,4\nswimming,1000,2,1\n Cycling,5000,5,1"

data_lines = data_text.split('\n')
data_labels = data_lines[0].split(",")
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = [line.split(",")[0] for line in data_lines[1:]]

# Create figure
fig = plt.figure(figsize=(24, 12))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:,0], label=data_labels[1])
ax1.set_ylabel(data_labels[1])
ax1.yaxis.label.set_color('blue')

# Line chart for Revenue
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[2])
ax2.set_ylabel(data_labels[2])
ax2.yaxis.label.set_color('red')

# Line chart for Average Ticket Price
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(line_labels, data[:,2], 'g-', label=data_labels[3])
ax3.set_ylabel(data_labels[3])
ax3.yaxis.label.set_color('green')

# Set title, legend
plt.title('Sports and Entertainment: Attendance, Revenue, and Ticket Price Analysis')
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/317_202312311430.png')
plt.clf()
