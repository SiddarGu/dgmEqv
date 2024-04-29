
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_labels = ['Units Produced (Millions)', 'Manufacturing Cost ($/Unit)', 'Profit Margin (%)', 'Sustainability Index (0-100)']
data = np.array([
    [15, 20000, 10, 75],
    [200, 500, 30, 85],
    [50, 1000, 25, 80],
    [80, 700, 35, 70],
    [100, 150, 20, 65],
    [300, 50, 40, 90],
    [40, 100, 30, 95]
])
line_labels = ['Cars - ' + str(data[0, 2]), 'Smartphones - ' + str(data[1, 2]), 'Laptops - ' + str(data[2, 2]), 'Televisions - ' + str(data[3, 2]), 'Furniture - ' + str(data[4, 2]), 'Shoes - ' + str(data[5, 2]), 'Bicycles - ' + str(data[6, 2])]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
cmap = cm.get_cmap('RdYlGn')

for i, line_label in enumerate(line_labels):
    color = cmap((data[i, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3])))
    size = 600 + (5000 - 600) * ((data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=size, alpha=0.6, edgecolors='w', linewidths=0.6, label=None)
    ax.scatter([], [], color=color, s=20, label=line_label)

ax.set_xlabel(data_labels[0], fontsize=9, wrap=True)
ax.set_ylabel(data_labels[1], fontsize=9, wrap=True)
ax.legend(title=data_labels[2], loc='upper right', fontsize=9, title_fontsize=9)

norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
plt.colorbar(sm, label=data_labels[3], pad=0.02)

plt.title('Profit, Production and Sustainability in Various Manufacturing Industries')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/53_202312301731.png')
plt.clf()
