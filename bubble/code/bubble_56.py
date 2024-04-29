import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.patches import Patch

data_full = [
    ['Philosophy', 15, 200, 70, 80],
    ['Sociology', 25, 300, 75, 85],
    ['Psychology', 30, 250, 80, 85],
    ['Linguistics', 10, 150, 80, 82],
    ['Anthropology', 20, 180, 85, 90],
    ['History', 18, 220, 75, 88],
    ['Literature', 12, 190, 70, 92]
]

data_labels = ['Number of Research (Thousand)', 'Research Funding (Million $)', 'Social Impact Score', 'Humanities Appreciation Score']
line_labels = ['Philosophy', 'Sociology', 'Psychology', 'Linguistics', 'Anthropology', 'History', 'Literature']

data = np.array([row[1:] for row in data_full])

fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.get_cmap('viridis')
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
colors = cmap(norm(data[:, 3]))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=np.array([colors[i]]), s=(data[i, 2]-min(data[:, 2]))/(max(data[:, 2])-min(data[:, 2]))*4400+600, label=None, alpha=0.7)
    ax.scatter([], [], c=colors[i], alpha=0.7, s=20, label=f"{line_label} {data[i, 2]}")

ax.set_xlabel(data_labels[0], fontsize=10, wrap=True)
ax.set_ylabel(data_labels[1], fontsize=10, wrap=True)
plt.title('Research Impact in Social Sciences and Humanities Fields', fontsize=12)
legend1 = ax.legend(loc='upper left', title=data_labels[2], fontsize=9)
ax.add_artist(legend1)
scalarmappaple = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
plt.colorbar(scalarmappaple, ax=ax, orientation='vertical', label=data_labels[3])
plt.grid(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/288_202312310045.png')
plt.clf()
