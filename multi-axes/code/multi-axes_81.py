import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator

# Transform data
data_labels = ['Wheat Production (Million Tonnes)',
               'Corn Production (Million Tonnes)',
               'Rice Production (Million Tonnes)']

data = np.array([
    [648, 844, 464],
    [662, 879, 479],
    [681, 892, 487],
    [704, 907, 495],
    [721, 923, 504],
    [735, 938, 511],
    [749, 953, 519],
    [766, 969, 527],
    [782, 984, 535],
    [799, 999, 542]
])

line_labels = range(2010, 2020)

# Create multi-axes chart
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# Plot data
ax1.bar(line_labels, data[:,0], alpha=0.7, color='g', label=data_labels[0])
ax2.fill_between(line_labels, data[:,1], color='b', 
                 alpha=0.3, label=data_labels[1])
ax3.plot(line_labels, data[:,2], color='r', label=data_labels[2])

ax3.spines['right'].set_position(('outward', 60))

ax1.set_ylabel(data_labels[0], color='g')
ax2.set_ylabel(data_labels[1], color='b')
ax3.set_ylabel(data_labels[2], color='r')

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

plt.grid(True, which='both')
plt.title('Annual Global Food Production: Wheat, Corn, Rice')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/201_202312311051.png')
plt.clf()
