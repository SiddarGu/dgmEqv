
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

data_labels = ['Users (Millions)', 'Engagement (Score)', 'Revenue (Billion $)', 'Adoption Rate (%)']
line_labels = ['Facebook', 'YouTube', 'Instagram', 'Twitter', 'Snapchat', 'TikTok']
data = np.array([[2.7, 90, 70.7, 80],
                 [1.9, 75, 15.1, 75],
                 [1.1, 65, 8.0, 50],
                 [0.7, 60, 3.1, 55],
                 [0.4, 40, 0.8, 45],
                 [0.3, 30, 0.5, 30]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

cmap = plt.get_cmap('Blues')
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
scalar_map = ScalarMappable(cmap=cmap, norm=norm)

for i in range(len(line_labels)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * 5000 + 600, c=scalar_map.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), label=f'{line_labels[i]} ({data[i,2]})', s=20)

ax.legend(title=data_labels[2])

cb = fig.colorbar(scalar_map, ax=ax, shrink=0.8)
cb.set_label(label=data_labels[3], fontsize=12)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('User Engagement and Adoption of Social Media Platforms Worldwide')
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/10.png')

plt.clf()