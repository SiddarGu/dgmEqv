import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data = np.array([
    ["Solar", 500, 700, 300, 8],
    ["Wind", 400, 550, 250, 9],
    ["Hydro", 300, 400, 200, 10],
    ["Geothermal", 100, 150, 100, 7],
    ["Biomass", 200, 300, 150, 6]
])
data_labels = ["Generation Capacity (GW)", "Carbon Emissions Reduced (Million Tons)", "Investment (Billion $)", "Efficiency (Score)"]
line_labels = [f"{d[0]} {d[2]}" for d in data]
data = data[:, 1:].astype(float)

fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = ScalarMappable(norm=norm, cmap=cmap)

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=np.array([data[i, 3]]), cmap=cmap, s=data[i, 2] * 10, alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i])
ax.legend(title=data_labels[2])
ax.grid(True, linestyle='--', alpha=0.6)

plt.colorbar(sm, ax=ax, label=data_labels[3])
plt.title('Effects of Renewable Energy Sources on Environment Sustainability 2023')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/119_202312301731.png')
plt.clf()
