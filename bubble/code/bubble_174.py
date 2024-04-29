import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# process data
data_str = 'Company,Market Capitalization (Billion $),User Base (Millions),Profit Margin (%),Innovation Score (out of 10)\n Google,1500,2500,21,9\n Microsoft,1750,1500,33,8\n Amazon,1600,3000,28,7\n Facebook,800,2450,31,8\n Apple,2200,1000,38,9\n Netflix,250,200,27,7\n Tesla,650,25,23,10'
data_lines = data_str.split('\n')[1:]
data_labels = data_str.split('\n')[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in data_lines], dtype=float)
line_labels = [line.split(',')[0] for line in data_lines]

# normalize color and size
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
cmap = get_cmap("viridis")
size_scale = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
bubble_sizes = (size_scale(data[:,2]) * 4400) + 600  

# create figure
fig, ax = plt.subplots(figsize=(8,6))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], color=cmap(norm(data[i, 3])), s=bubble_sizes[i], label=None, alpha=0.6)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)

ax.legend(title=data_labels[2])
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax).set_label(data_labels[3])

# set labels, title and grid
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Comparative Analysis of Major Tech Companies')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/250_202312310045.png')
plt.clf()
