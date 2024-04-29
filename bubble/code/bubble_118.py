import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib import colors
import numpy as np
import pandas as pd

data_labels = ['Age', 'Gender', 'Salary', 'Performance Index']
line_labels = ['John Smith', 'Anna Johnson', 'Michael Davis', 'Sarah Anderson', 'Robert Wilson']

data = np.array([
    [35, 1, 60000, 80],
    [28, 0, 50000, 90],
    [45, 1, 80000, 75],
    [32, 0, 55000, 85],
    [40, 1, 70000, 70]
])

fig, ax = plt.subplots(figsize=(10,8))

cmap = plt.get_cmap('viridis')
color_map = colors.Normalize(data[:, 3].min(), data[:, 3].max())
for i in range(data.shape[0]):
    line_label = "{} {}".format(line_labels[i], data[i, 2])
    scatter = ax.scatter(data[i, 0], data[i, 1], c=[data[i, 3]], s=[data[i, 2]*0.075], 
                         cmap=cmap, norm=color_map, alpha=0.6, edgecolors='w', linewidth=1, label=None)
    ax.scatter([], [], c=cmap(color_map(data[i, 3])), alpha=0.3, s=20, label=line_label)
scatter.set_clim(70, 90)

ax.grid(True)
ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

norm = colors.Normalize(data[:,3].min(), data[:,3].max())
sm = ScalarMappable(norm=norm, cmap=scatter.cmap)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3], pad=0)

plt.title('Employee Details and Performance Index')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/390_202312311429.png')
plt.clf()
