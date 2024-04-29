import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import cm
from matplotlib.ticker import NullFormatter

# create data array
data_labels = ['Revenue (Billion $)', 'Global Fanbase (Millions)', 'Endorsement Deals (Millions $)', 'Popularity (Score)']
data = np.array([[50, 300, 200, 90], 
                 [32, 250, 150, 85], 
                 [15, 200, 100, 80], 
                 [45, 600, 120, 95], 
                 [80, 800, 500, 100], 
                 [150, 1000, 300, 98]])
line_labels = ['Football', 'Basketball', 'Tennis', 'Music Concerts', 'Film Industry', 'Video Games']

fig, ax = plt.subplots(figsize=(10, 6))

# normalize bubble size to range [600, 5000]
bubble_sizes = 600 + (data[:, 2] / np.max(data[:, 2])) * 4400

# normalize color values to range [0, 1]
color_values = (data[:, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3]))

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=[cm.viridis(color_values[i])],
               s=[bubble_sizes[i]], label=None, alpha=0.6)
    ax.scatter([], [], c=cm.viridis(color_values[i]), alpha=0.4, s=20, label="{:s}".format(line_labels[i]) + f' {data[i, 2]}')

# set legend title
legend = ax.legend(title=data_labels[2], loc="upper left")

# add colorbar
sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])))
sm._A = []
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

# show grid
ax.grid(True)

# set title and axis labels
ax.set_title("Revenue and Popularity of Sports and Entertainments Across the Globe")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# format tick labels
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

# save and show figure
plt.tight_layout()

path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/316_202312310045.png"
plt.savefig(path, dpi=300)

plt.clf()
