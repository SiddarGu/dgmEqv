import matplotlib.pyplot as plt
import numpy as np

# Define the data
data_str = np.array([['Quarter', 'Revenue (Millions)', 'Operating Income (Millions)', 'Net Profit (Millions)', 'Number of Employees'],
                    ['Q1', 12387, 5690, 2789, 130580], 
                    ['Q2', 16400, 8323, 4135, 131005], 
                    ['Q3', 14962, 7251, 3596, 131880],
                    ['Q4', 18880, 9412, 4704, 133090]])

# Convert data into the three variables
data_labels = data_str[0,1:]
line_labels = data_str[1:,0]
data = data_str[1:,1:].astype(float)

# Create the figure
plt.figure(figsize=(20,10))
ax1 = plt.subplot(111)

# Create the bar chart for the first column of data
ax1.bar(line_labels, data[:,0], color='b', label = data_labels[0])
ax1.set_xlabel('Quarter')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')
plt.title('Quarterly Financial Performance of the Business')

# Create the line chart for the second column of data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label = data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('red')

# Create the scatter chart for the third column of data
if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:,2], color='g', label = data_labels[2])
    ax3.spines['right'].set_position(('outward', 60)) 
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color('green')
    
# Create the area chart for the fourth column of data, 
if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], color='c', alpha=0.5, label=data_labels[3])
    ax4.spines['right'].set_position(('outward', 120)) 
    ax4.set_ylabel(data_labels[3])
    ax4.yaxis.label.set_color('cyan')   

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
if data.shape[1] > 2:
    ax3.legend(loc='lower left')
if data.shape[1] > 3:
    ax4.legend(loc='lower right')

plt.grid()
plt.autoscale(enable=True, axis='both', tight=True)
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/112_202312310108.png')
plt.clf()
