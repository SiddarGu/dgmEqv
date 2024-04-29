import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Transformed data 
data_labels = ['Energy Source', 'Production (Million MWh)', 'Consumption (Million MWh)', 'Revenue (Billion $)', 'Efficiency (Score)']
line_labels = ["Oil", "Coal", "Natural Gas", "Hydropower", "Nuclear", "Wind", "Solar"]

# data
data = np.array([
    [5000, 4500, 600, 7],
    [4000, 3800, 500, 6],
    [4500, 4200, 550, 8],
    [3000, 2800, 400, 9],
    [2500, 2400, 350, 8],
    [2000, 1900, 300, 10],
    [1500, 1400, 250, 10]
])

fig, ax = plt.subplots(figsize=(16,10))

# Normalize size and color
size = 600 + 5000 * (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2]))
colors = data[:, 3]

# Create colormap
cmap = get_cmap("viridis")
norm = Normalize(vmin=np.min(colors), vmax=np.max(colors))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(norm(data[i, 3]))], s=size[i], label=None)
    ax.scatter([], [], label=line_label + f' {data[i, 2]}', color=cmap(norm(data[i, 3])), s=20)

# Colorbar
mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
plt.colorbar(mappable, ax=ax, label=data_labels[3])

ax.legend(title=data_labels[2])
ax.grid(True)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.set_title("Performance of Different Energy Sources in the Utilities Sector 2023")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/281_202312310045.png")
plt.clf()
