import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase
import numpy as np

data_labels = ["Market Value (Billion $)", "Internet Users (Millions)", "Profit Margin (%)", "Innovation (Score)"]
data = np.array([
    [1500, 200, 35, 9],
    [890, 250, 27, 8],
    [1750, 150, 20, 9],
    [1550, 180, 30, 8],
    [2200, 210, 35, 9],
    [130, 50, 15, 7],
    [240, 100, 20, 8]
])
line_labels = ["Google", "Facebook", "Amazon", "Microsoft", "Apple", "Twitter", "Netflix"]

cmap = get_cmap("plasma")
color_norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-data[:,2].min())/(data[:,2].max()-data[:,2].min())*4400+600, label=None, c=cmap(color_norm(data[i, 3])), alpha=1, edgecolors='w', linewidth=2)
    ax.scatter([], [], label="{} {}".format(line_label, data[i, 2]), c=cmap(color_norm(data[i, 3])), alpha=1, s=20, edgecolors='w', linewidth=2)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Technology Companies Performance and Impact on Internet Users')

ax2 = fig.add_axes([0.92, 0.15, 0.03, 0.7])
cb = ColorbarBase(ax2, cmap=cmap, norm=color_norm, orientation='vertical')
cb.set_label(data_labels[3])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/159_202312310045.png')
plt.clf()
