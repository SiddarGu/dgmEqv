import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cmx
import numpy as np

data_labels = ["Carbon Footprint (Metric tons per capita)", "Renewable Energy Usage (%)", "Population (Millions)", "Environmental Preservation (Score)"]
data = np.array([[7.4, 20, 1415, 30],
                 [15.5, 16, 331, 40],
                 [1.9, 35, 1390, 45],
                 [11.1, 18, 145, 32],
                 [2.1, 48, 213, 55],
                 [16.2, 20, 25, 38],
                 [5.6, 33, 66, 50]], dtype=float)
line_labels = ["China", "USA", "India", "Russia", "Brazil", "Australia", "UK"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

cmap = plt.get_cmap('viridis')
c_norm = mcolors.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
scalar_map = cmx.ScalarMappable(norm=c_norm, cmap=cmap)

for i in range(len(line_labels)):
    line_label = line_labels[i] + ' ' + str(data[i, 2])
    color_val = scalar_map.to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] + 0.1) * 10, color=color_val, label=None)
    ax.scatter([], [], c=color_val, alpha=0.5, s=20, label=line_label)

ax.legend(title=data_labels[2])

plt.colorbar(scalar_map).set_label(data_labels[3])

ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], wrap=True)

plt.grid(True)
plt.title('Comparison of Carbon Footprint and Renewable Energy Usage per Country', wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/212_202312310045.png')
plt.clf()
