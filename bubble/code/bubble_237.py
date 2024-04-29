import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
# Given Data
data_labels = ['Freight Volume (Million Tonnes)','Fuel Efficiency (Km/l)','Operational Cost ($/mile)','Safety score (out of 10)']

data = np.array([
    [17000, 6, 1.2, 8],
    [30000, 15, 0.5, 9],
    [50000, 10, 0.7, 7],
    [10000, 5, 2, 10],
    [15000, np.nan, 0.3, 6]
])

line_labels = ['Trucks 6 Km/l', 'Trains 15 Km/l', 'Ships 10 Km/l', 'Airplanes 5 Km/l', 'Pipelines NA Km/l']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
colors = cmap(norm(data[:, 3]))
norm = mcolors.Normalize(vmin=colors.min(), vmax=colors.max())

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=colors[i], alpha=0.6, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], c=colors[i], alpha=0.5, s=20, label=line_labels[i]) 

# Adding color bar   
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Add in labels and legend
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Setting grid
ax.grid(True)

# Add title
plt.title('Transportation Efficiency and Costs - Logistics 2023', pad=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/255_202312310045.png')
plt.clf()
