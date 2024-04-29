import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data & labels
data_labels = ['Facebook active users (millions)', 'Twitter active users (millions)', 'Instagram active users (millions)', 'YouTube active users (millions)', 'LinkedIn active users (millions)']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([
    [1590, 320, 400, 1000, 400],
    [1870, 330, 600, 1100, 425],
    [2120, 340, 800, 1250, 465],
    [2390, 355, 1000, 1350, 500],
    [2690, 360, 1200, 1430, 575],
    [2940, 380, 1340, 1550, 690],
    [3190, 400, 1490, 2000, 740]
])

fig = plt.figure(figsize=(25, 15))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='C0')
ax1.yaxis.set_major_locator(AutoLocator())

# Overlapping axes for the remaining data columns
ax = [ax1]
for i in range(1, data.shape[1]):
    ax.append(ax[0].twinx())
    ax[i].plot(line_labels, data[:,i], color=f'C{i}', label=data_labels[i])
    ax[i].spines['right'].set_position(('outward', (i - 1) * 70)) 
    ax[i].set_ylabel(data_labels[i], color=f'C{i}')
    ax[i].yaxis.label.set_color(f'C{i}')
    ax[i].tick_params(axis='y', colors=f'C{i}')

# Title and x-axis label
plt.title('Active Users on Various Social Media Platforms: 2015-2021')
ax[0].set_xlabel('Year')

# Legend for all line labels
lines, labels = ax[0].get_legend_handles_labels()
for i in range(1, len(ax)):
    line, label = ax[i].get_legend_handles_labels()
    lines += line
    labels += label
plt.legend(lines, labels, loc='upper left')

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/181_202312310150.png')

# Clearing the figure
plt.clf()
