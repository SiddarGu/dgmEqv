import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from matplotlib import ticker

# Transform data
data = np.array([
    [2500, 10, 5, 40],
    [2200, 15, 4, 50],
    [1500, 8, 3, 45],
    [1000, 12, 2, 35],
    [2000, 20, 6, 30]
])
data_labels = ['Number of Users (Millions)', 'Average Session Duration (Minutes)', 'Conversion Rate (%)', 'Bounce Rate (%)']
line_labels = ['Google, 5', 'Facebook, 4', 'Instagram, 3', 'Twitter, 2', 'YouTube, 6']

fig, ax = plt.subplots(figsize=(10,8))

# Normalize color and size
color = (data[:, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
size = 600 + (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 4400

scatter = ax.scatter(data[:, 0], data[:, 1], c=color, s=size, cmap='viridis', alpha=0.6, edgecolors="w", linewidth=2, label=None)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2])
ax.grid(True)

cbar = plt.colorbar(ScalarMappable(norm=mcolors.Normalize(data[:, 3].min(), data[:, 3].max()), cmap='viridis'), ax=ax)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('User Engagement and Conversion Rates of Popular Websites')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/334_202312311429.png')
plt.clf()
