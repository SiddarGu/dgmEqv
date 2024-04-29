import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_labels = ['Revenue (Million $)', 'Attendance (Millions)', 'Expenditures (Million $)', 'Popularity Score']

data = np.array([[2500, 200, 500, 8],
                 [1500, 150, 400, 7],
                 [1800, 170, 450, 9],
                 [1200, 100, 300, 6],
                 [800, 80, 200, 5],
                 [600, 60, 150, 4],
                 [300, 30, 100, 3],
                 [150, 15, 50, 2],
                 [100, 10, 30, 1],
                 [50, 5, 10, 1]])

line_labels = ['Music', 'Visual arts', 'Film', 'Theater', 'Literature', 'Dance', 'Painting', 'Sculpture', 'Photography', 'Poetry']

fig, ax = plt.subplots(figsize=(16, 10))
cmap = get_cmap("tab10")

normalize = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

for i, line_label in enumerate(line_labels):
    line_label = line_label + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], alpha=0.6, edgecolors='w', label=None,
               s=60 + 500 * normalize(data[i, 2]), c=cmap(normalize(data[i, 3])), linewidth=2)
    ax.scatter([], [], c=cmap(normalize(data[i, 3])), alpha=0.6, s=20, label=line_label)

ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], rotation=0, wrap=True)

ax.legend(title=data_labels[2], loc="lower right")

s_m = plt.cm.ScalarMappable(cmap=cmap, norm=normalize)
plt.colorbar(s_m, ax=ax, label=data_labels[3])

plt.title('Cultural Industries Revenue and Popularity')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/374_202312311429.png')

plt.clf()
