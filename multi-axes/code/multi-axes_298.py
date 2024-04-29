import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Distance Traveled (Millions of miles)', 'Fuel Consumption (Thousands of gallons)', 'Average Speed (mph)']
data = np.array([[1457, 580, 50], [1204, 450, 60], [3278, 1500, 500], [5000, 1400, 18], [1700, 100, 1], [5, 0, 10], [2, 0, 3]])
line_labels = ['Road', 'Rail', 'Air', 'Sea', 'Pipeline', 'Bicycle', 'Walking']

fig = plt.figure(figsize=(24, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], color='b')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='g')
ax2.set_ylabel(data_labels[1], color='g')
ax2.spines['right'].set_position(('outward', 60))
ax2.tick_params(axis='y', colors='g')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.plot(line_labels, data[:,2], color='r')
    ax3.set_ylabel(data_labels[2], color='r')
    ax3.spines['right'].set_position(('outward', 120))
    ax3.tick_params(axis='y', colors='r')

plt.title('A Comparative Study of Various Transport Modes in Terms of Distance, Fuel Consumption, and Speed')

legend1 = ax1.legend(line_labels, loc='upper left')
legend2 = ax2.legend(line_labels, loc='upper right')

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/244_202312311051.png', bbox_inches='tight')

plt.show()
plt.clf()
