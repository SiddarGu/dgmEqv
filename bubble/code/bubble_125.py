import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
import pandas as pd

# Transform the data into three variables
data = np.array([
    [265595, 59531, 13, 116],
    [143015, 39240, 8, 181],
    [386064, 21903, 10, 798],
    [161857, 34359, 9, 132],
    [70697, 22225, 6, 58],
    [31536, 721, 2, 48]
])
data_labels = ["Revenue (Million $)", "Profit (Million $)", "Market Share (%)", "Employees (thousands)"]
line_labels = ["Apple", "Microsoft", "Amazon", "Alphabet", "Facebook", "Tesla"]

# Create figure 
fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot(1, 1, 1)

# Create a colormap
cmap = get_cmap('viridis')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

# plot data with type of scatter(). mapping color and size using 3rd and 4th value of each line
for i, line_label in enumerate(line_labels):
    line_label = line_label + ' (' + str(data[i, 2]) + ')'
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], alpha=0.6, edgecolors='w', label=None,
                s=600 + 4400 * (data[i, 2] / data[:, 2].max()), color=color)
    ax.scatter([], [], label=line_label, alpha=0.6, edgecolors='w',
                s=20, color=color)

# adjust the background grids or other parameter settings
ax.grid(True, linestyle='-', color='0.75')
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:1,.0f}'.format(x)))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:1,.0f}'.format(x)))
# show the labels of two axis
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
# plot the legend
ax.legend(title=data_labels[2], loc='upper left')
# set the figure title
plt.title('Financial Performance of Tech Companies', y=1.05)
# add a color bar
ax2 = fig.add_axes([0.14, 0.15, 0.8, 0.03])
cb = ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')
cb.set_label(data_labels[3])

# automatically resize the image by tight_layout() before savefig().
plt.tight_layout()
# the image must be saved with defined absolute path
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/366_202312311429.png')
# clear the current image state
plt.clf()
plt.close('all')
