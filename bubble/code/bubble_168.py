import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = """Soccer,50,3800,20,4
Basketball,30,3800,25,7.5
Cricket,20,2400,18,3
Tennis,6,1000,12,2
Golf,5,500,30,2.5
Baseball,10.4,500,23,3.7
American Football,15,400,22,6.5
Formula 1,3,500,15,12"""
data = [row.split(',') for row in data.split('\n')]
data_labels = ['Revenue (Billion $)', 'Global Fan Base (Millions)', 'Profit Margin (%)', 'Average Player Salary (Million $)']
names = [data[i][0] for i in range(len(data))]
data = np.array([list(map(float, row[1:])) for row in data])

line_labels = [f"{row} - {d[2]}" for row, d in zip(names, data)]

norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
cmap = get_cmap("viridis")

fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(data[:, 0], data[:, 1], s=600 + 4400 * data[:, 2]/data[:, 2].max(), c=data[:, 3], cmap=cmap, norm=norm, alpha=0.6, edgecolors='w', linewidth=1, label=None)
for line_label, color in zip(line_labels, data[:, 3]):
    ax.scatter([], [], c=cmap(norm(color)), s=20, label=line_label)

ax.grid(True)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)

plt.title('Revenue and Profit Comparison Among Different Sports', fontsize=15)
legend1 = ax.legend(title=data_labels[2], loc='upper left', fontsize=10)
ax.add_artist(legend1)

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.1)
cbar = fig.colorbar(sc, cax=cax, orientation='vertical')
cbar.set_label(data_labels[3], fontsize=10)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/235_202312310045.png', format='png')
plt.clf()
