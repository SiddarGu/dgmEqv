import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib import cm

# Data Processing
data_labels = ['Number of Cases', 'Settled Cases', 'Dismissed Cases', 'Judgement in Favor (%)']
line_labels = ['Civil Litigation', 'Criminal', 'Corporate Law', 'Family Law', 'Environmental Law', 'Intellectual Property', 'Property Disputes']
data = np.array([
    [1200, 900, 250, 70],
    [2000, 1500, 400, 60],
    [800, 600, 100, 80],
    [1500, 1100, 350, 73],
    [500, 300, 100, 60],
    [700, 550, 120, 65],
    [1800, 1450, 300, 76]
])

# Plotting
fig, ax = plt.subplots(figsize=(16, 8))
cmap = get_cmap("Spectral")

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
colors = cmap(norm(data[:, 3]))

bubbles = ax.scatter(data[:, 0], data[:, 1], linewidth=1, edgecolor='black', s=(data[:, 2] / data[:, 2].max()) * 5000, c=colors)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=colors[i], s=20, label=f'{line_label} ({data[i, 2]})')

ax.legend(title=data_labels[2], loc='center left')
plt.title('Overview of Legal Cases in Different Fields of Law', fontsize=22)
plt.xlabel(data_labels[0],fontsize=16)
plt.ylabel(data_labels[1],fontsize=16)

# Colorbar
fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, label=data_labels[3])

plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/230_202312310045.png')
plt.clf()
