import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm

data_labels = ['Revenue (Million $)', 'Market Share (%)', 'Profit Margin (%)', 'Number of Employees']
line_labels = ['Bakery - 50', 'Beverages - 100', 'Dairy - 75', 'Meat and Poultry - 80', 'Snacks - 60']

data = np.array([
    [500, 10, 15, 50],
    [1000, 20, 20, 100],
    [750, 15, 18, 75],
    [800, 16, 21, 80],
    [600, 12, 17, 60]
])

fig, ax = plt.subplots(figsize=(14, 10))
fig.suptitle('Financial Performance and Employment in Food and Beverage Industry')

colors = data[:, 3]
cm = plt.cm.get_cmap('RdYlBu_r')
sc = ax.scatter(data[:, 0], data[:, 1], c=colors, cmap=cm, s=(data[:, 2]-data[:, 2].min()) * 5000 + 600, label=None)

for i in range(len(data)):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_labels[i])

norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = plt.cm.ScalarMappable(norm=norm, cmap=cm)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3])

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/371_202312311429.png', dpi=300)
plt.show()

plt.clf()
