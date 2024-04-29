import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_labels = ['Revenue (Million $)', 'Attendance (Millions)', 'TV Rating (Score)', 'Social Media Followers (Millions)']
data = np.array([[6000, 200, 9, 300],
                 [3000, 100, 7, 200],
                 [2000, 80, 6, 100],
                 [4000, 150, 8, 250],
                 [1000, 50, 5, 50]])
line_labels = ['Football ' + str(data[0, 2]),
               'Basketball ' + str(data[1, 2]),
               'Baseball ' + str(data[2, 2]),
               'Soccer ' + str(data[3, 2]),
               'Hockey ' + str(data[4, 2])]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

color_map = cm.get_cmap('rainbow')
norm_color = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
norm_size = Normalize(vmin=np.min(data[:, 2]), vmax=np.max(data[:, 2]))
bubble_sizes = norm_size(data[:, 2]) * 5000 + 600

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=[color_map(norm_color(data[i, 3]))], label=None)
    ax.scatter([], [], c='k', s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(cm.ScalarMappable(norm=norm_color, cmap=color_map), label=data_labels[3])
plt.grid(True)

plt.title('Performance Metrics in Sports and Entertainment Industry')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/350_202312311429.png')
plt.clf()
