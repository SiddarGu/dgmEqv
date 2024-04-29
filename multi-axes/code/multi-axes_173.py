import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Transformed Data
line_labels = ["Natural Sciences", "Engineering and Technology", "Medical and Health Sciences",
               "Agricultural Sciences", "Social Sciences", "Humanities", "Mathematics",
               "Computer Sciences", "Physics", "Chemistry", "Earth and Space", "Biological Sciences",
               "Psychology", "Environmental Science", "Economics", "Environmental and Resource Management"]

data_labels = ["Research Investment (Millions of Dollars)", "Published Papers (Thousands)", 
               "Patents Awarded", "Research Institutes"]

data = np.array([
    [2000, 98, 675, 36],
    [3500, 135, 950, 44],
    [2900, 121, 800, 40],
    [1300, 76, 530, 30],
    [900, 85, 410, 18],
    [500, 32, 280, 12],
    [1000, 47, 395, 22],
    [2700, 110, 695, 35],
    [2200, 87, 655, 31],
    [1900, 84, 615, 29],
    [2100, 80, 640, 28],
    [3100, 105, 840, 38],
    [800, 70, 375, 17],
    [1500, 72, 520, 25],
    [1000, 53, 370, 15],
    [1200, 64, 455, 23]
])

# Plot Initialization
fig = plt.figure(figsize=(15,12))
ax1 = fig.add_subplot(111)

# Multi-Axes Plot
ax1.bar(line_labels, data[:, 0], label=data_labels[0], color='g')
ax1.set_ylabel(data_labels[0], color='g')
ax1.set_xlabel('Field')
ax1.tick_params(axis='y', colors='g')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], color='b')
ax2.set_ylabel(data_labels[1], color='b')
ax2.tick_params(axis='y', colors='b')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], alpha=0.4, color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')

ax4 = ax1.twinx()
sc = ax4.scatter(line_labels, data[:,3], label=data_labels[3], color='purple')
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color='purple')
ax4.tick_params(axis='y', colors='purple')

# Legends, Grids and Labels
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
ax1.grid(linestyle='-', linewidth='0.5', color='grey')
ax1.set_title('Science and Engineering Fields: Analysing Investment, Output and Infrastructure')
plt.tight_layout()

# Axis Adjustment
for ax in fig.axes:
    ax.set_xticklabels(line_labels, rotation=45, ha="right")
    ax.yaxis.set_major_locator(AutoLocator())
    fig.canvas.draw()

# Save and Clear Figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/237_202312311051.png")
plt.clf()
