import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from matplotlib.lines import Line2D 

# data preparation
data_labels = ['Total Deliveries', 'Tons Moved(Thousands)', 'Fuel Efficiency(MPG)','On-Time Arrival Rate(%)'] 
line_labels = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([[19000,2500,13.2,86],[20000,2600,13.1,87],[20800,2800,13.2,88],
                 [21000,2850,13.4,90],[21400,2890,13.3,91],[21800,2940,13.5,92],
                 [22200,3000,13.6,94],[23000,3050,13.7,96],[24000,3100,13.7,97],
                 [24500,3150,13.8,96],[25000,3200,13.7,94],[25500,3250,13.6,90]])

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

# plot settings
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.plot(line_labels, data[:, 0], color='tab:blue', label=data_labels[0])
ax.set_xlabel('Month')
ax.set_ylabel(data_labels[0], color=colors[0])
ax.yaxis.set_major_locator(AutoLocator())
ax.tick_params(axis='y', colors=colors[0])

# add secondary y-axis
ax2 = ax.twinx()
ax2.plot(line_labels, data[:, 1], color='tab:orange', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())
ax2.tick_params(axis='y', colors=colors[1])

# add extra y-axes
ax3 = ax.twinx()
ax3.scatter(line_labels, data[:, 2], color='tab:green', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.yaxis.set_major_locator(AutoLocator())
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', colors=colors[2])

# bar chart
ax4 = ax.twinx()
ax4.bar(line_labels, data[:, 3], color='tab:red', alpha=0.3, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color=colors[3])
ax4.yaxis.set_major_locator(AutoLocator())
ax4.spines['right'].set_position(('outward', 120))
ax4.tick_params(axis='y', colors=colors[3])

# title and layout
plt.title('Annual Performance Metrics in Transportation and Logistics Industry')
fig.tight_layout()
plt.grid(True)

# legend
line = Line2D([0], [0], color='k')
legend = ax.legend([line,line,line,line], data_labels, loc='upper left', title='Performance Metrics')
for color,text in zip(colors, legend.get_texts()):
    text.set_color(color)

# save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/263_202312311051.png')

# clear the current figure
plt.clf()
