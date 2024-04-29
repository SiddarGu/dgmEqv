import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# data
data_labels = ['Success Rate (%)', 'Cost (Millions)', 'Innovation Score', 'Research Duration (Years)']
line_labels = ['Gene Editing', 'Renewable Energy', 'Artificial Intelligence', 'Nanotechnology', 
               'Space Exploration', 'Biotechnology', 'Robotics', 'Data Science', 
               'Virtual Reality', '3D Printing']
data = np.array([[ 90,  50,  8, 5],
                 [ 80, 100,  7,10],
                 [ 95,  80,  9, 3],
                 [ 75, 120,  6, 8],
                 [ 85, 200,  7,15],
                 [ 70, 150,  5, 7],
                 [ 90,  70,  8, 4],
                 [ 85,  90,  7, 6],
                 [ 80, 110,  6, 9],
                 [ 75, 100,  5, 5]])

fig, ax = plt.subplots()
fig.set_size_inches(14, 10)
cmap = cm.get_cmap('viridis')

for i in range(len(line_labels)):
    line_label = line_labels[i] + ' ' + str(data[i, 2])
    size = ((data[i, 2] - data[:, 2].min()) / data[:, 2].ptp()) * (5000 - 600) + 600
    color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
    ax.scatter(data[i, 0], data[i, 1], s=size, c=[cmap(color)], label=None)
    ax.scatter([], [], label=line_label, c=[cmap(color)], s=20)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)
norm = Normalize(data[:,3].min(), data[:,3].max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3], pad=0)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Success and Cost of Various Science and Engineering Projects')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/369_202312311429.png')
plt.close(fig)
