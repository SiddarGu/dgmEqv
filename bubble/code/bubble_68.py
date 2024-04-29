import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import numpy as np

data_str = "Product,Production Volume (Million Units),Manufacturing Cost (Million $),Profit Margin (%),Safety Rating (Score)/n Cars,70,200,25,8/n Electronics,120,180,30,9/n Furniture,80,150,20,8/n Textiles,100,130,15,7/n Pharmaceuticals,90,120,30,10/n Cosmetics,110,140,22,7"
data_lines = [line.split(',') for line in data_str.split('/n')]
data_labels = data_lines[0][1:]
data = np.array([[float(value) for value in line[1:]] for line in data_lines[1:]])
line_labels = [f'{line[0]} ({int(data[i, 2])})' for i, line in enumerate(data_lines[1:])]

fig, ax = plt.figure(figsize=(10, 10)), plt.axes()
color_norm = Normalize(data[:, 3].min(), data[:, 3].max())
size_norm = Normalize(data[:, 2].min(), data[:, 2].max())
cmap = get_cmap("viridis")
scatter = ax.scatter(data[:, 0], data[:, 1], 
                     c=data[:, 3], s=600 + 4400*size_norm(data[:, 2]), 
                     cmap=cmap, norm=color_norm, alpha=0.6, edgecolors="w", linewidth=2, label=None)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=cmap(color_norm(data[i, 3])), alpha=0.6, s=20, label=line_label)
ax.legend(title=data_labels[2], loc="upper right")
ax.grid(True, linestyle='-', color='0.7')
ax.set_title('Manufacturing Output, Cost, and Safety in Various Industries')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.xaxis.label.set_rotation(45)

fig.colorbar(cm.ScalarMappable(norm=color_norm, cmap=cmap), 
             ax=ax, label=data_labels[3])

plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/195_202312310045.png')
plt.clf()
