import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator

# Transforming data into variables
data_labels = ["Number of Art Exhibitions", "Number of Live Performances", 
               "Number of Museums", "Number of Theaters", "Number of Art Galleries"]
line_labels = ["Music", "Dance", "Theater", "Visual Arts", "Literature", "Film", "Crafts", "Photography"]
data = np.array([[200, 300, 50, 100, 150],
                [150, 200, 40, 80, 120],
                [100, 150, 30, 60, 100],
                [250, 350, 60, 120, 200],
                [ 50, 100, 20, 40,  80],
                [ 80, 120, 25, 50, 100],
                [120, 150, 30, 60, 100],
                [100, 120, 25, 50, 80]])

color_list = plt.cm.Set3(np.linspace(0, 1, 12))
plt.figure(figsize=(25, 15))

# Create a grid : initialize it
ax1 = plt.subplot(111)

# Plots
ax1.bar(line_labels, data[:, 0], label=data_labels[0], color=color_list[0])
ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:, 1], color=color_list[1], label=data_labels[1], s=100)
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color=color_list[2], label=data_labels[2])
ax3.fill_between(line_labels, data[:, 2], alpha=0.3, color=color_list[2])
rspine = ax3.spines['right']
rspine.set_position(('axes', 1.1))
ax4 = ax1.twinx()
ax4.bar(line_labels, data[:, 3], label=data_labels[3], color=color_list[3], 
        alpha=0.4, align="center", width=0.3)
rspine = ax4.spines['right']
rspine.set_position(('axes', 1.2))

ax5 = ax1.twinx()
rspine = ax5.spines['right']
rspine.set_position(('axes', 1.3))
ax5.set_frame_on(True)
ax5.patch.set_visible(False)
ax5.bar(line_labels, data[:, 4], label=data_labels[4], color=color_list[4],
        alpha=0.4, align="edge", width=0.3)

ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color=color_list[0])
ax2.set_ylabel(data_labels[1], color=color_list[1])
ax3.set_ylabel(data_labels[2], color=color_list[2])
ax4.set_ylabel(data_labels[3], color=color_list[3])
ax5.set_ylabel(data_labels[4], color=color_list[4])

# Grid
ax1.grid()

# Legends
ax1.legend(loc="lower right")
ax2.legend(loc="upper right")
ax3.legend(loc="upper left")
ax4.legend(loc="lower left")
ax5.legend(loc="center right")

# Adjusting y-axes ranges
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())
ax5.yaxis.set_major_locator(AutoLocator())

# Title
plt.title("Arts and Culture in Numbers")

# Plotting
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/300_202312311430.png')
plt.clf()
