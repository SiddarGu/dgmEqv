import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.collections import PathCollection
import numpy as np

data_labels = ['Student Enrollment', 'Teacher-Student Ratio', 'Graduation Rate (%)', 'Research Funding (Millions)']
data = np.array([
 [100, 20, 95, 5],
 [500, 25, 90, 8],
 [1000, 30, 85, 12],
 [2000, 40, 80, 20],
 [5000, 50, 75, 50]
])
line_labels = ['Primary School', 'Secondary School', 'High School', 'College', 'University']

fig, ax = plt.subplots(figsize=(10,10))

cmap = plt.get_cmap("cool")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

for i in range(len(data)):
    # considering data[i, 2] = bubble size, data[i, 3] = color
    line_label = f"{line_labels[i]} ({data[i, 2]})"
    ax.scatter(data[i, 0], data[i, 1], s=(data[i,2]-min(data[:,2]))/(max(data[:,2])-min(data[:,2]))*4400+600, c=cmap(norm(data[i, 3])), label=None, edgecolors='none', alpha=0.8)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)

leg = ax.legend(title=data_labels[2], fontsize=8)
ax.grid(True)

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Academic Performance and Enrollment - Education Data')

sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3], rotation='vertical', labelpad=15)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/391_202312311429.png")
plt.close()
