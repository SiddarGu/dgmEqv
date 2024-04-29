import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_string = "Category,Number of Researchers,Research Funding (Million $),Number of Patents,Research Impact (Score)/n Physics,500,100,200,8/n Chemistry,700,150,150,7/n Biology,800,200,175,9/n Engineering,1000,300,300,6"
data_string = data_string.replace('/n', '\n')
data_list = [item.split(',') for item in data_string.split('\n')]

data_labels = data_list[0][1:]
line_labels = [f'{item[0]} {item[2]}' for item in data_list[1:]]
data = np.array([list(map(float, item[1:])) for item in data_list[1:]])

fig, ax = plt.subplots(figsize=(12,12))
cmap = plt.get_cmap("viridis")

norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], alpha=0.6, edgecolors='w', label=None, 
               linewidth=2, s=600 + 4400*((data[i, 2] - min(data[:, 2]))/(max(data[:, 2]) - min(data[:, 2]))), 
               c=cmap(norm(data[i, 3])))
    ax.scatter([], [], color=cmap(norm(data[i, 3])), alpha=0.6, s=20, label=line_label)

ax.grid(True)
ax.legend(title=data_labels[2])
plt.colorbar(sm, label=data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Scientific Research and Impact in Different Fields')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/329_202312311429.png')
plt.clf()
