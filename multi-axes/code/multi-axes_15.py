

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Category','Number of Organizations','Number of Staffs','Total Budget (Millions of Dollars)']
line_labels = ['Education','Healthcare','Social Security','Public Safety','Public Works','Taxation','Economy','Energy and Environment','Legal Services','Transportation']
data = np.array([[50,3000,120],[20,2050,110],[30,2500,90],[40,3500,150],[40,3000,140],[20,1500,80],[25,2750,100],[30,2500,120],[60,4000,160],[45,3500,140]])

fig, ax = plt.subplots(figsize=(14,7))

bar_width = 0.2
bar_position_1 = np.arange(len(data))
bar_position_2 = [x + bar_width for x in bar_position_1] 
bar_position_3 = [x + bar_width for x in bar_position_2]

# plot the bar chart
ax.bar(bar_position_1, data[:,0], width = bar_width, label = data_labels[1], color = 'tab:blue')
ax2 = ax.twinx()
ax2.bar(bar_position_2, data[:,1], width = bar_width, label = data_labels[2], color = 'tab:orange')
ax3 = ax.twinx()
ax3.bar(bar_position_3, data[:,2], width = bar_width, label = data_labels[3], color = 'tab:green')

ax.set_xticks(np.arange(len(data)) + bar_width)
ax.set_xticklabels(line_labels, rotation=45)
ax.set_title("Government and Public Policy Performance Overview: Number of Organizations, Staffs, and Budget")
ax.set_ylabel(data_labels[1], color='#0093b9')
ax2.set_ylabel(data_labels[2], color='#ff9c00')
ax3.set_ylabel(data_labels[3], color='#fecf44')
ax.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
# set the position for the second, third, ... y-axes
ax3.spines['right'].set_position(('axes', 1.1))

# label each y-axis
ax.set_ylabel(data_labels[1], color = 'tab:blue')
ax2.set_ylabel(data_labels[2], color = 'tab:orange')
ax3.set_ylabel(data_labels[3], color = 'tab:green')

# add grids
ax.grid(True, which='major', axis='x', linestyle='--')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8.png')
plt.clf()