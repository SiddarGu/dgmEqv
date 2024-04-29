import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# transform the given data
data_labels = ['Annual Production (Million Tonnes)', 'Recycling Rate (%)', 'Energy Saved (%)', 'Pollution Reduction (Score)']
line_labels = ['Aluminum\n68%', 'Steel\n70%', 'Paper\n67%', 'Glass\n33%', 'Plastics\n9%', 'Copper\n35%']
data = np.array([[63, 68, 95, 8], [1871, 70, 60, 6], [400, 67, 40, 7], [208, 33, 25, 7], [359, 9, 15, 3], [20, 35, 85, 9]])

# normalize color and size values to cmap and bubble size range
norm = Normalize(data[:, 3].min(), data[:, 3].max())
colors = get_cmap('viridis')(norm(data[:, 3]))
bubble_size = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# create figure
fig, ax = plt.subplots(figsize=(12, 8))
fig.suptitle("Impact of Recycling on Energy and Pollution Reduction - Global Data 2023", fontsize=16, fontweight='bold')

# scatter the points
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_size[i], c=np.array([colors[i]]), label=None)
    ax.scatter([], [], c=np.array([colors[i]]), s=20, label=line_labels[i])

# display legend
ax.legend(title=data_labels[2], loc='lower right')

# color bar
sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(min(data[:,3]), max(data[:,3])))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3], pad=0)

# axis labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# grid
ax.grid(True)

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/52_202312301731.png')

# show figure
plt.show()

# clear figure
plt.close()
