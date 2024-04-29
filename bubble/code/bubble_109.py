import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = np.array([
    ['Facebook', 2770, 86, 58, 7],
    ['YouTube', 2000, 20, 40, 2],
    ['WhatsApp', 2000, 5, 23, 61],
    ['WeChat', 1100, 12, 32, 9],
    ['Instagram', 1120, 20, 28, 13],
    ['Twitter', 330, 3.46, 31, 37]
], dtype=object)

data_labels = ['Active Users (Millions)', 'Revenue (Billion $)', 'Time Spent per Day (Minutes)', 'Website Rank (Global)']
line_labels = [f'{row[0]} {row[2]}' for row in data]
data = np.array(data[:, 1:], dtype=float)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

size = (600 - 5000) * (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) + 5000
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

for i in range(len(data)):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=size[i], color=color, alpha=0.6, ec="black", linewidth=2, label=None)
    ax.scatter([], [], color=color, alpha=0.6, s=20, label=line_labels[i])

plt.gca().set(title='Influence and Popularity of Social Media Platforms on the Web 2023', xlabel=data_labels[0], ylabel=data_labels[1])
plt.legend(title=data_labels[2], loc='best')
plt.grid(True)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm, label=data_labels[3])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/103_202312301731.png', dpi=300)
plt.clf()

