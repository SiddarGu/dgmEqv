import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# transform data 
data_labels = ['Public Spending (billions)', 'Total Federal debt (billions)', 'Policy Changes', 'Unemployment Rate (%)']
line_labels = [str(y) for y in range(2000, 2017)]
data = np.array([[1789, 5954, 12, 4.0], [1862, 6298, 15, 4.7], [2019, 6672, 22, 5.8], \
                [2159, 6921, 27, 6.0], [2305, 7372, 32, 5.5], [2478, 7746, 35, 5.1], \
                [2683, 8186, 39, 4.6], [2863, 8706, 45, 4.6], [2982, 9416, 52, 5.8], \
                [3517, 11030, 66, 9.3], [3456, 12098, 80, 9.6], [3603, 13356, 84, 8.9], \
                [3584, 14351, 92, 8.1], [3457, 15604, 99, 7.4], [3582, 16785, 107, 6.2], \
                [3863, 18120, 113, 5.3], [4054, 19572, 120, 4.9]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], 'b-', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.fill_between(line_labels, 0, data[:,1], color='green', alpha=0.5, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.yaxis.label.set_color('green')
ax2.tick_params(axis='y', labelcolor='g')
ax2.grid(False)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.bar(line_labels, data[:,2], color='red', alpha=0.5, label=data_labels[2], align='center')
ax3.set_ylabel(data_labels[2], color='r')
ax3.yaxis.label.set_color('red')
ax3.tick_params(axis='y', labelcolor='r')
ax3.yaxis.set_major_locator(AutoLocator())
ax3.grid(False)

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
scatter = ax4.scatter(line_labels, data[:,3], color='purple', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.yaxis.label.set_color('purple')
ax4.tick_params(axis='y', labelcolor='purple')
ax4.yaxis.set_major_locator(AutoLocator())
ax4.grid(False)

fig.suptitle('Analysis of Government Spending, Debt, and Policy Changes Over Time')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/160_202312310108.png')
plt.cla()
plt.clf()
