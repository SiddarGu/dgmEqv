

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ['Research Cost (Million $)', 'Development Time (Months)', 'Usage (Million People)', 'Success Rate (%)']
data = np.array([[150, 48, 500, 85],
                 [100, 38, 100, 90],
                 [200, 36, 400, 75],
                 [50, 60, 200, 95],
                 [80, 24, 150, 80]])
line_labels = ['Artificial Intelligence', 'Quantum Computing', 'Robotics', 'Nanotechnology', 'Energy Storage']

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()
norm = cm.colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
s_m = cm.ScalarMappable(cmap=cm.RdYlGn, norm=norm)
s_m.set_array([])

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 5000 + 600,
               c=s_m.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=s_m.to_rgba(data[i, 3]), label=line_label + f' {data[i, 2]}')

ax.legend(title=data_labels[2])
cb = fig.colorbar(s_m, ticks=np.linspace(data[:, 3].min(), data[:, 3].max(), 5))
cb.ax.set_title(data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Cost and Time Investment for Advanced Science and Engineering Technologies')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/17_2023122261326.png')
plt.clf()