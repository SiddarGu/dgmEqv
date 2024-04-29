
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np

data_labels = ['Return (%)', 'Risk Level (Score)', 'Initial Capital (Million $)']
line_labels = ['Stock Market', 'Cryptocurrency', 'Mutual Funds', 'Real Estate', 'Bonds']
data = np.array([[12, 8, 100],
                [20, 10, 200],
                [7, 6, 500],
                [15, 9, 1000],
                [9, 7, 300]])

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1,1,1)

cmap = plt.get_cmap('gist_rainbow')
cnorm = colors.Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
scalar_map = cmx.ScalarMappable(norm=cnorm, cmap=cmap)

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2] * 10, c=scalar_map.to_rgba(data[i, 2]), label=None)
    ax.scatter([], [], s=20, c=scalar_map.to_rgba(data[i, 2]), label=line_labels[i] + ' ' + str(data[i, 2]))

ax.legend(title=data_labels[2])
cbar = plt.colorbar(scalar_map, ax=ax, orientation='horizontal', pad=0.03)
cbar.set_label(data_labels[2], rotation=0)

ax.set_title('Maximizing Profit Based on Investment Type and Risk Level - Business and Finance 2023')
ax.grid(linestyle='--')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/4.png')

plt.clf()