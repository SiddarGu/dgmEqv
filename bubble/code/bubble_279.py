import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

data_strings = [
    "Coal,9000,37,2200,120",
    "Natural Gas,6000,42,1200,150",
    "Solar,3000,100,0,200",
    "Hydro,4000,90,50,180",
    "Wind,3500,95,20,160",
    "Nuclear,2500,99,1500,220"
]
data_labels = ["Energy Source", "Production (TWh)", "Distribution Efficiency (%)", "Carbon Footprint (Million Tonnes)", "Capital Investment (Billion $)"]

data = np.array([list(map(int, ds.split(",")[1:])) for ds in data_strings])
line_labels = [ds.split(",")[0] + " " + str(data[i, 2]) for i, ds in enumerate(data_strings)]

cmap = get_cmap("viridis")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(data[:, 0], data[:, 1], c=data[:, 3], s=(data[:, 2] - min(data[:, 2])) / (max(data[:, 2]) - min(data[:, 2])) * (5000 - 600) + 600, cmap=cmap, norm=norm, alpha=0.6, edgecolors="w", label=None)
for i in range(data.shape[0]):
    ax.scatter([], [], c=cmap(norm(data[i, 3])), alpha=0.6, s=20, label=line_labels[i])

ax.legend(title=data_labels[2])
ax.grid(True)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

plt.title('Production and Environmental Impact of Various Energy Sources - Utilities 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/71_202312301731.png')
plt.clf()
