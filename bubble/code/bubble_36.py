
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Transform data
data_labels = ['Audience Size (Millions)', 'Revenue (Billion $)', 'Sponsorship (Score)', 'Viewership (Score)']
data = np.array([[700, 80, 90, 95], [450, 50, 80, 85], [350, 40, 75, 80], [250, 30, 70, 75], [600, 60, 85, 90]])
line_labels = ['Basketball', 'Football', 'Baseball', 'Ice Hockey', 'Soccer']

# Color mapping and normalization
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Plot
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()
for i, line_label in enumerate(line_labels):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=600 + 2000 * (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()),  color=color, label=None)
    ax.scatter([], [], s=20, color=color, label=line_label + f' {data[i, 2]}')
ax.legend(title=data_labels[2])

fig.colorbar(sm, ax=ax, label=data_labels[3])
ax.set_title('Popular Sports and Their Impact on Revenue and Viewership')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/4_2023122261326.png')
plt.clf()