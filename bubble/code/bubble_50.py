
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

data_labels = ['Cost (Billion $)', 'Duration (Years)', 'Energy Usage (Megawatt)', 'Risk Level (Score)']
line_labels = ['Fusion Reactor', 'Satellite Launch', 'Solar Farm', 'Earthquake Early Warning System', 'Autonomous Vehicle Network', 'Offshore Wind Farm']
data = np.array([[10, 15, 100, 7], [2, 2, 50, 9], [1, 5, 25, 6], [3, 7, 10, 8], [5, 12, 75, 10], [4, 10, 45, 7]])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

for i in range(data.shape[0]):
    cmap = cm.get_cmap('RdYlGn')
    norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
    size = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
    sc = ax.scatter(data[i, 0], data[i, 1], s=size(data[i, 2]) * 500 + 60, c=[cmap(norm(data[i, 3]))], label=None)
    ax.scatter([], [], s=20, c=sc.get_facecolors(), label=line_labels[i] + ' ' + str(data[i, 2]))
    
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

plt.title('Investment and Risk Assessment of Science and Engineering Projects')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/7_2023122270050.png')

plt.close()