
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

data_labels = ['Revenue (Billion $)', 'Cost (Billion $)', 'Efficiency (Score)', 'Safety (Score)']
data = np.array([[120, 100, 8, 9], [200, 150, 9, 8], [400, 300, 10, 10], [600, 400, 7, 9], [50, 30, 10, 7]])
line_labels = ['Road', 'Rail', 'Air', 'Maritime', 'Drone']

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range (len(data)):
    norm = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
    cmap = cm.ScalarMappable(norm=norm, cmap=cm.RdYlGn)
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - data[:,2].min())/(data[:,2].max() - data[:,2].min())*2000 + 600, c=cmap.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=cmap.to_rgba(data[i, 3]), label=line_labels[i] + ' ' + str(data[i, 2]))

ax.legend(title=data_labels[2])
cb = cmap.to_rgba(data[:,3])
cb1 = fig.colorbar(cmap, ax=ax)
cb1.ax.set_ylabel(data_labels[3], rotation=270, labelpad=20)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Assessing the Value of Different Transportation Modes')
plt.grid(True)
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/31_2023122270050.png')
plt.close()