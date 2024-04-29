
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# transform data
data_labels = ['Number of Citizens', 'Income per Capita (Dollars)', 'Percentage of Population Living Below Poverty Line']
line_labels = ['Education', 'Healthcare', 'Taxation', 'Public Assistance', 'Infrastructure', 'Social Welfare', 'Defense', 'Employment', 'Housing']
data = np.array([[7200, 2800, 15], [7800, 2550, 8], [9400, 3100, 17], [8100, 2300, 20], [7600, 2700, 14], [6100, 2100, 25], [8300, 3000, 19], [6700, 2500, 16], [9000, 3200, 12]])

# create figure
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)
ax1.set_title('Government and Public Policy: Citizen Income and Poverty Analysis')
ax1.set_xlabel('Category')
ax1.set_ylabel('Number of Citizens')
ax1.bar(line_labels, data[:, 0], color='g', label=data_labels[0])

# plot ax2
ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1], color='#00AEEF')
ax2.plot(line_labels, data[:, 1], color='#00AEEF', marker='o', linestyle='--', label=data_labels[1])
ax2.tick_params(axis='y', labelcolor='#00AEEF')

# plot ax3
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.set_ylabel(data_labels[2], color='#F46524')
ax3.plot(line_labels, data[:, 2], color='#F46524', marker='s', linestyle=':', label=data_labels[2])
ax3.fill_between(line_labels, 0, data[:, 2], color='#F46524', alpha=0.5)
ax3.tick_params(axis='y', labelcolor='#F46524')
ax3.yaxis.set_ticks_position('right')
ax3.yaxis.set_label_position('right')

# set legend
lns1 = mpatches.Patch(color='g', label=data_labels[0])
lns2 = mpatches.Patch(color='#00AEEF', label=data_labels[1])
lns3 = mpatches.Patch(color='#F46524', label=data_labels[2])
ax3.legend(handles=[lns1, lns2, lns3], loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=3)

# draw background grid
ax1.grid(color='gray', linestyle='--', linewidth=1)
ax2.grid(color='gray', linestyle='--', linewidth=1)
ax3.grid(color='gray', linestyle='--', linewidth=1)

# autolocate y-axis
ax1.set_ylim(auto=True)
ax2.set_ylim(auto=True)
ax3.set_ylim(auto=True)

# resize image
plt.tight_layout()

# save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/41_2023122270030.png")
plt.clf()