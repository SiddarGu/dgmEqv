import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

data = np.array([
    ['New York', 820, 3.6, 7.4, 5],
    ['Los Angeles', 680, 3.2, 6.8, 7],
    ['Chicago', 270, 2.8, 2.6, 9],
    ['Houston', 210, 2.4, 2.1, 10],
    ['Phoenix', 240, 2.6, 1.6, 9],
    ['San Francisco', 1250, 3.8, 0.8, 4],
    ['Miami', 330, 2.9, 2.1, 8]
], dtype=object)

data_labels = ['Average Property Price (1000$)', 'Mortgage Rate (%)', 'Total Households (Millions)', 'Affordability (Score)']
line_labels = [f'{city} {rate}%' for city, rate in zip(data[:, 0], data[:, 2])]
data = data[:,1:].astype(float)

# Normalize size and color
size = 600 + 4400 * (data[:, 2].astype(float) - min(data[:, 2].astype(float))) / (max(data[:, 2].astype(float)) - min(data[:, 2].astype(float)))
color = (data[:, 3].astype(float) - min(data[:, 3].astype(float))) / (max(data[:, 3].astype(float)) - min(data[:, 3].astype(float)))

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

# Bubble chart
cmap = get_cmap("viridis")
ax.scatter(data[:, 1].astype(float), range(len(data[:, 0])), c=cmap(color), s=size, alpha=0.6, edgecolors="w", linewidth=1)

# Add line labels
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=cmap(color[i]), alpha=0.6, s=600, label=line_label)

# Label
ax.legend(title=data_labels[2], loc="lower left", fontsize=10)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_yticks(range(len(data[:, 1])))
ax.set_yticklabels(data[:, 1], fontsize=10)

# Color bar
norm = Normalize(vmin=min(data[:, 3].astype(float)), vmax=max(data[:, 3].astype(float)))
cbar_ax = fig.add_axes([0.93, 0.2, 0.02, 0.6])
cb = ColorbarBase(cbar_ax, cmap=cmap, norm=norm, orientation='vertical')
cbar_ax.set_title(data_labels[3], pad=15)

# Grid background
ax.set_facecolor('#f0f0f0')
ax.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

fig.suptitle('Real Estate Pricing and Affordability in Major U.S. Cities, 2023', fontsize=14, fontweight='bold')
fig.tight_layout(pad=2)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/293_202312310045.png')

plt.clf()
