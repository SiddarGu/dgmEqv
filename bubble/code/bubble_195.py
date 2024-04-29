
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import numpy as np

data_labels = ['Average Usage Time (Hour/Day)', 'User Base (Millions)', 'Data Capacity (TB)', 'Cost (USD)']
line_labels = ['YouTube', 'Instagram', 'Google', 'Amazon', 'Apple']
data = np.array([[3, 2, 1000, 0], [2.5, 1.5, 200, 0], [2, 1.2, 300, 0], [1.5, 0.8, 100, 10], [1, 0.5, 50, 20]])

fig = plt.figure()
ax = fig.add_subplot()

ax.set_title('Popular Online Platforms and their Usage Statistics')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

norm = mpl.colors.Normalize(vmin = data[:,3].min(), vmax = data[:,3].max())
cmap = cm.get_cmap('RdYlGn')
scalar_map = cm.ScalarMappable(norm=norm, cmap=cmap)

for i in range(len(data)):
    sc = ax.scatter(data[i, 0], data[i, 1], c=scalar_map.to_rgba(data[i, 3]), s=(data[i, 2]-data[:, 2].min())/(5000-600)*5000+600, label=None)
    ax.scatter([], [], c=sc.get_facecolor(), label=line_labels[i]+' '+str(data[i, 2]))

ax.legend(title=data_labels[2])

cb = plt.colorbar(scalar_map, ax=ax)
cb.set_label(data_labels[3])

ax.grid()
ax.autoscale()

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/11_2023122270050.png')

plt.close()