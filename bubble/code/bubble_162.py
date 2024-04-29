import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.cm import ScalarMappable

data = np.array([
    [2800, 70, 60, 7.5],
    [1400, 80, 20, 8.5],
    [330, 60, 5, 7],
    [600, 65, 8, 6.5],
    [700, 90, 15, 9.5],
    [400, 75, 10, 7.5],
    [300, 85, 7, 8],
    [250, 70, 5, 7.5],
    [2000, 95, 10, 9.5],
    [1100, 90, 12, 9]
])
line_labels = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'TikTok', 'Snapchat', 'Pinterest', 'Reddit', 'WhatsApp', 'WeChat']
data_labels = ['Number of Users (Millions)', 'Engagement Rate (%)', 'Advertising Revenue (Billion $)', 'Data Privacy (Score)']

fig, ax = plt.subplots(figsize=(10,10))

colormap = plt.cm.get_cmap('RdYlBu')
color_norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], alpha=0.6, s=bubble_sizes[i], c=colormap(color_norm(data[i, 3])), label=None)
    ax.scatter([], [], c=colormap(color_norm(data[i, 3])), alpha=0.3, s=20, label=f'{line_labels[i]} ({data[i, 2]})')

ax.legend(title=data_labels[2], loc='lower center')
ax.grid(True)
plt.title('Social Media and Web Statistics', fontsize=16)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

sm = ScalarMappable(cmap=colormap, norm=plt.Normalize(0, max(data[:, 3])))
sm.set_array([])

cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/384_202312311429.png')
plt.clf()
