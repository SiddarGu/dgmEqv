import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_content = [['Law Firm','Revenue (Billion $)','Number of Lawyers','Cases Won (%)','Client Satisfaction (Score)'],
                ['Baker McKenzie',19,4800,70,8],
                ['DLA Piper',18,4200,68,7],
                ['Kirkland & Ellis',15,3900,75,9],
                ['Latham & Watkins',14,3700,72,8],
                ['Dentons',12,3500,65,7],
                ['Skadden',11,3300,70,8],
                ['Clifford Chance',10,3100,68,7],
                ['Allen & Overy',9,2900,67,7],
                ['Linklaters',8,2700,65,6],
                ['Freshfields',7,2500,63,6]]

data_labels = data_content[0][1:]
line_labels = [x[0] + ' ' + str(x[2]) for x in data_content[1:]]
data = np.array([x[1:] for x in data_content[1:]])


norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])
cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
cbar.set_label(data_labels[3], rotation=270, labelpad=20)
plt.title('Performance of Major Law Firms - Legal Affairs 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/307_202312310045.png')
plt.clf()
