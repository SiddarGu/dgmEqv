import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# parse the raw data
raw_data='Category,Number of Publications,Number of Citations,Number of Authors\nPsychology,8000,23000,5000\nSociology,6000,18000,4000\nEducation,7000,19000,4500\nAnthropology,4000,15000,3500\nPolitical Science,5500,21000,3800\nHistory,5000,20000,3700\nEconomics,9000,25000,5500\nLinguistics,3500,13000,3000'
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])

# plot types
plotTypes = ['b-', 'g-', 'r-', 'c-', 'm-', 'y-', 'k-', 'w-']

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# plot the first column data
ax1.bar(line_labels, data[:,0], color='b', alpha=0.7)
ax1.set_ylabel(data_labels[0], color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()

# plot the second column data
ax2.plot(line_labels, data[:,1], 'g-')
ax2.set_ylabel(data_labels[1], color='g')
for tl in ax2.get_yticklabels():
    tl.set_color('g')

# plot the third column data data[:,2] if it exists
if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.plot(line_labels, data[:,2], 'r-')
    ax3.set_ylabel(data_labels[2], color='r')
    for tl in ax3.get_yticklabels():
        tl.set_color('r')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1.grid()
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
if data.shape[1] > 2:
    ax3.yaxis.set_major_locator(AutoLocator())

plt.title('Research Impact Analysis by Discipline')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/273_202312311430.png')
plt.clf()
