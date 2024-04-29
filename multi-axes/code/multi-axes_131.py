import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# transform data
data_str = '''Physics,200,180,7
Chemistry,220,154,10
Biology,210,189,9
Aerospace Engineering,185,201,15
Computer Science,245,219,23
Electrical Engineering,210,182,18
Mechanical Engineering,188,175,14
Civil Engineering,195,155,12
Environmental Science,220,210,6
Mathematics,242,200,5'''
data_lines = data_str.split('\n')
line_labels = [line.split(',')[0] for line in data_lines]
data = np.array([list(map(int, line.split(',')[1:])) for line in data_lines])
data_labels = ['Number of Students', 'Number of Research Papers Published', 'Number of Patents Registered']

# create figure
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], alpha=0.6, label=data_labels[0], color='b')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='g')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('g')
ax2.tick_params(axis='y', colors='g')
ax2.yaxis.set_major_locator(AutoLocator())

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.fill_between(line_labels, data[:, 2], alpha=0.3, label=data_labels[2], color='orange')
    ax3.spines['right'].set_position(('outward', 60))
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color('orange')
    ax3.tick_params(axis='y', colors='orange')
    ax3.yaxis.set_major_locator(AutoLocator())

# add legends, title and grid
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.title('Analysis of Student Numbers, Research Publications, and Patent Registration in Various Fields of Science and Engineering')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/93_2023122292141.png')
plt.clf()
