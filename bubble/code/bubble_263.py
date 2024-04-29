import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

data = np.array([
    ['Rice', 750, 200, 150, 60],
    ['Wheat', 680, 160, 130, 70],
    ['Corn', 1000, 140, 120, 65],
    ['Soybeans', 330, 100, 100, 75],
    ['Barley', 200, 80, 70, 80],
    ['Cotton', 120, 40, 60, 70],
    ['Tobacco', 80, 25, 55, 75]
])

data_labels = ['Harvest (Million Tonnes)', 'Irrigation Water (Billion Cubic Metres)', 'Fertilizer Use (Million Tonnes)', 'Appropriate Technology Adoption (%)']
line_labels = [f'{line[0]} {line[4]}' for line in data]

line_data = np.array([list(map(float, line[1:])) for line in data])
bubble_size = line_data[:, 2] / max(line_data[:, 2]) * (5000 - 600) + 600
color_value = line_data[:, 3]

norm = plt.Normalize(min(color_value), max(color_value))
cmap = plt.get_cmap("viridis")

fig, ax = plt.subplots(figsize=(10, 8))

for i in range(len(line_data)):
    ax.scatter(line_data[i, 0], line_data[i, 1], s=bubble_size[i], alpha=0.6, edgecolors='w', c=cmap(norm(color_value[i])), label=None)
    ax.scatter([], [], color=cmap(norm(color_value[i])), label=line_labels[i], alpha=0.6, edgecolors='w')

ax.legend(title=data_labels[2], loc='upper right', borderaxespad=0)
ax.grid(True)

cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap))
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_title(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Agriculture and Food Production: Resource Use and Technology Adoption')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/162_202312310045.png')
plt.clf()
