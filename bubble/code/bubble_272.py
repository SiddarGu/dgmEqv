
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.patches as mpatches

data_labels = np.array(['Consumption (kWh/month)', 'Cost (USD)', 'Reliability (Score)', 'Efficiency (Score)'])
data = np.array([[6500, 500, 9, 7],
                 [3500, 400, 8, 9],
                 [2500, 300, 10, 10],
                 [1500, 250, 9, 8],
                 [1000, 200, 8, 7],
                 [500, 150, 7, 6]])
line_labels = np.array(['Electricity', 'Gas', 'Solar', 'Wind', 'Hydro', 'Nuclear'])

fig, ax = plt.subplots(figsize=(10,8))
for i in range(data.shape[0]):
    cmap = cm.get_cmap('RdYlGn')
    norm = colors.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
    size_norm = colors.Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-min(data[:, 2]))/(max(data[:, 2])-min(data[:, 2]))*5000+600, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

ax.legend(title=data_labels[2])
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

ax.set_title('Energy Consumption and Cost Analysis - Utilities 2023', fontsize=20)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

ax.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/24_2023122270050.png')
plt.clf()