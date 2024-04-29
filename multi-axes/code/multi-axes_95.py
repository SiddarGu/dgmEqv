import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Attendance (millions)', 'Total Revenue (millions)', 'Average Rating out of 10']
line_labels = ['NBA Games', 'NFL Games', 'MLB Games', 'NHL Games', 'FIFA World Cup', 'Olympics', 'Tennis Grand Slams', 'Boxing Matches', 'Marathons', 'Esports Tournaments', 'Concerts', 'Movie Theater Admission']
data = np.array([
    [22, 7800, 8.5],
    [16, 9000, 8.7],
    [69, 10000, 8.3],
    [17, 4200, 8.0],
    [3.572, 6000, 8.6],
    [3.5, 5120, 8.8],
    [1.8, 2400, 8.4],
    [1.3, 7000, 7.8],
    [1, 400, 8.6],
    [0.495, 1940, 7.9],
    [22.5, 5000, 9.0],
    [1310, 42000, 7.7]
])

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

bar_width = 0.35
opacity = 0.8

ax1.bar(line_labels, data[:, 0], color='b', align='center')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

ax2 = ax1.twinx() 
ax2.plot(line_labels, data[:, 1], 'g-')
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='r')
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')
ax3.spines['right'].set_position(('outward', 60))

plt.title('Attendance, Revenue, and Popularity of Various Sports and Entertainment Events')
plt.grid(True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/206_202312311051.png')
plt.show()
plt.clf()
