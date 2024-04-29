import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

data_labels = ['Energy Consumption (GWh)', 'Utility Cost (Millions of Dollars)', 'Renewable Energy Percentage (%)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

data = np.array([
    [3500, 195, 23],
    [3400, 180, 25],
    [4000, 205, 26],
    [3800, 220, 28],
    [4200, 235, 30],
    [4100, 240, 32],
    [4500, 255, 34],
    [4200, 250, 33],
    [3800, 225, 32],
    [3600, 210, 31],
    [3500, 200, 29],
    [3600, 210, 27]
])

fig = plt.figure(figsize=(30,20))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.legend(loc='upper left')
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.tick_params(axis='y', colors='b')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='r', label=data_labels[1])
ax2.legend(loc='upper right')
ax2.set_ylabel(data_labels[1], color='r')
ax2.yaxis.set_major_locator(AutoLocator())
ax2.tick_params(axis='y', colors='r')

ax3 = ax1.twinx()
r = fig.canvas.get_renderer()
rspine = ax3.spines['right']
rspine.set_position(('outward', 60))
ax3.set_frame_on(True)
ax3.patch.set_visible(False)
fig.subplots_adjust(right=0.7)
ax3.bar(line_labels, data[:,2], color='g', alpha=0.5, label=data_labels[2])
ax3.legend(loc='center right')
ax3.set_ylabel(data_labels[2], color='g')
ax3.yaxis.set_major_locator(AutoLocator())
ax3.tick_params(axis='y', colors='g')

plt.title('Monthly Energy Consumption, Cost, and Renewable Energy Use in the Energy and Utilities Sector')
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/189_202312310150.png')
plt.clf()
