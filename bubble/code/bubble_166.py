import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = np.array([
    ['Picasso',5000,1000,20,90],
    ['Van Gogh',4000,800,30,85],
    ['Da Vinci',3000,1200,10,98],
    ['Monet',2000,700,25,95],
    ['Michelangelo',3500,900,15,90],
    ['Rembrandt',2500,600,20,88],
    ['Raphael',3000,750,18,91],
    ['Caravaggio',2300,680,16,87],
    ['Botticelli',2200,650,12,89],
    ['Vermeer',2100,600,24,86]
])

data_labels = ['Artworks Sold (Numbers)', 'Charity Donations (Thousand $)', 'Worldwide Fans (Millions)', 'Cultural Influence (Score)']

line_labels = [f"{label} {data[i, 2]}" for i, label in enumerate(data[:, 0])]
data = data[:, 1:].astype(float)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_title("Influence of Artists in Arts and Culture", fontsize=14)
ax.grid(True)

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/286_202312310045.png")
plt.close(fig)
