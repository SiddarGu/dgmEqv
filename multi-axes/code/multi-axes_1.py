
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# transform data
data_labels = ['Number of Cases Handled', 'Hours Spent (in Thousands)', 'Average Court Time (in Minutes)']
line_labels = ['Civil Law', 'Criminal Law', 'Constitutional Law', 'Administrative Law', 'International Law', 'Human Rights Law', 'Tax Law', 'Business and Commercial Law', 'Family Law', 'Immigration Law']
data = np.array([[890, 3450, 56], [1020, 5060, 78], [720, 2030, 35], [650, 4500, 60], [990, 3880, 70], [1130, 2460, 43], [720, 3300, 45], [890, 4200, 60], [1010, 2580, 50], [650, 2100, 35]])

# setup plot
fig, ax1 = plt.subplots(figsize=(15, 10))

# plot data
ax1.bar(line_labels, data[:, 0], label=data_labels[0], color='tab:blue')
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='tab:green', linestyle='-')
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:, 2], label=data_labels[2], color='tab:red', linestyle='--')

# adjust positions of axis
ax1.set_xticks(np.arange(len(line_labels)))
ax1.set_xticklabels(line_labels, rotation=45, ha="right", wrap=True)
ax1.autoscale(axis='x', tight=True)
ax2.autoscale(axis='x', tight=True)
ax3.autoscale(axis='x', tight=True)

# label axes
ax1.set_ylabel(data_labels[0], color='tab:blue')
ax2.set_ylabel(data_labels[1], color='tab:green')
ax3.set_ylabel(data_labels[2], color='tab:red')

# add legends
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# draw grids
ax1.grid()

# set title
fig.suptitle('Law and Legal Affairs Case Volume and Time Analysis', fontsize=20)

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/23_2023122261325.png')

# clear figure
plt.clf()