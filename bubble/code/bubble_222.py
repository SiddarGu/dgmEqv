

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ["Viewership (Millions)", "Tickets Sold (Millions)", "Media Coverage (Score)", "Prize Money (Billion $)"]
data = np.array([[3.2, 0.12, 9, 0.2],
                 [3, 0.08, 8, 0.15],
                 [2.5, 0.03, 7, 0.14],
                 [2, 0.02, 6, 0.12],
                 [1.5, 0.04, 5, 0.1]])
line_labels = ["Olympics_" + str(data[0,2]),
               "World Cup_" + str(data[1,2]),
               "NBA Finals_" + str(data[2,2]),
               "Super Bowl_" + str(data[3,2]),
               "Grand Slam_" + str(data[4,2])]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

for i in range(data.shape[0]):
    norm = cm.colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
    bubble_size = 600 + (5000-600)*((data[i,2] - data[:,2].min())/(data[:,2].max()-data[:,2].min()))

    ax.scatter(data[i,0], data[i,1], s=bubble_size, c=cm.jet(norm(data[i,3])), label=None)
    ax.scatter([], [], c=cm.jet(norm(data[i,3])), s=20, label=line_labels[i])

ax.legend(title=data_labels[2], fontsize=14)

sm = cm.ScalarMappable(norm=norm, cmap=cm.jet)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.06, orientation="vertical")
cbar.set_label(data_labels[3], fontsize=14)

ax.set_title("Most Popular Sports Events in Terms of Viewership and Media Coverage", fontsize=14)
ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel(data_labels[1], fontsize=14)

ax.grid(linestyle="--", alpha=0.5)

fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/44_2023122270050.png")

plt.cla()