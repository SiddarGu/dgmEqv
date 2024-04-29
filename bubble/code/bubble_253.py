
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Delivery Time (Hours)', 'Cost (USD)', 'Fuel Efficiency (km/l)', 'Safety Rating']
line_labels = ['Road', 'Rail', 'Sea', 'Air', 'Drone', 'Pipeline']
data = np.array([[24, 200, 8, 4], [36, 400, 10, 3], [72, 600, 12, 2],
                 [12, 800, 14, 5], [6, 1000, 16, 4], [48, 1200, 18, 3]])

fig, ax = plt.subplots(figsize=(15, 10))
norm = cm.colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
scalar_map = cm.ScalarMappable(norm=norm, cmap=cm.Accent)
s_min, s_max = 600, 5000
s_norm = lambda val: ((val - data[:, 2].min()) /
                      (data[:, 2].max()-data[:, 2].min())) * (s_max - s_min) + s_min

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=s_norm(data[i, 2]), c=scalar_map.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), label=line_label + f' {data[i, 2]}', s=20)

ax.legend(title=data_labels[2], loc='lower left')
cbar = fig.colorbar(scalar_map, ax=ax, label=data_labels[3], orientation="horizontal", fraction=0.05, pad=0.05)
ax.grid()
ax.set_title('Comparing Delivery Time, Cost and Safety of Different Modes of Transportatio')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.xticks(rotation=45, wrap=True)
plt.yticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/42_2023122261326.png')
plt.clf()