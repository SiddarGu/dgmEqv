import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

data="""Quarter,Revenue(Thousands),Expenses(Thousands),Net Profit (Thousands)
Q1,5820,3450,2370
Q2,6070,3580,2490
Q3,6290,3970,2320
Q4,6820,4180,2640 """
plot_types = ['bar', 'line', 'line']

data_lines = data.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines[1:]])

fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)
ax1.set_title('Quarterly Performance Analysis for Business and Finance')

if plot_types[0] == 'bar':
    ax1.bar(line_labels, data[:,0], color='c', label=data_labels[0])

ax2 = ax1.twinx()
if plot_types[1] == 'line':
    ax2.plot(line_labels, data[:,1], color='coral', label=data_labels[1])

if len(data[0]) > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60)) 
    if plot_types[2] == 'line':
        ax3.plot(line_labels, data[:,2], color='blue', label=data_labels[2])

# Set labels and legends for each axis
ax1.set_xlabel('Quarter')
ax1.set_ylabel(data_labels[0], color='c')
ax2.set_ylabel(data_labels[1], color='coral')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
if len(data[0]) > 2:
    ax3.set_ylabel(data_labels[2], color='blue')
    ax3.legend(loc='center right')

# Use AutoLocator to adjust y-axes range
mpl.ticker.AutoLocator()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/224_202312311051.png')
plt.cla()
plt.close()
