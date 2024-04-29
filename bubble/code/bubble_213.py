import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

# manipulate the data
raw_data = [
    ['Truck', 3000, 5, 300, 15],
    ['Cargo Ship', 4000, 20, 200, 5000],
    ['Air Freight', 2000, 2, 1000, 150],
    ['Train', 3500, 15, 250, 500],
    ['Barge', 1500, 10, 100, 2000],
    ['Pipeline', 1000, 0, 50, 10000],
]

data = np.array([row[1:] for row in raw_data])
line_labels = [f"{row[0]} {row[2]}" for row in raw_data]
data_labels = ["Transport Volume (Million tonnes)", "Fuel Efficiency (Miles per Gallon)",
               "CO2 Emissions (Million Tonnes)", "Cargo Capacity (Tonnes)"]

# normalize bubble size and color
size_scale = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
color_scale = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
colors = cm.viridis(color_scale(data[:, 3]))
sizes = 600 + size_scale(data[:, 2]) * 4400

# create figure and subplot
fig, ax = plt.subplots(figsize=(12, 8))
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=colors[i], alpha=0.6, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], c=cm.viridis(color_scale(data[i, 3])), alpha=0.6, s=20, label=line_labels[i])

# add color bar
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

# add legend and labels
ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Transportation and Logistics Efficiency with Different Vehicle Types 2023')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/185_202312310045.png', dpi=300)
plt.clf()
