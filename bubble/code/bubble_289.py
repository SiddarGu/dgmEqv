import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_string = 'City,CO2 Emissions (Kilotons),Waste Generated (Kilotons),Population (Millions),Green Spaces (%)\n New York,55000,16000,8.4,27\n Los Angeles,40000,14000,4,33\n London,75000,22000,8.9,47\n Beijing,110000,30000,21.5,35\n Mumbai,80000,27000,20.4,18\n Tokyo,70000,20000,37.4,30 '

data_lines = data_string.split('\n')
data_labels = data_lines[0].split(',')[1:]
data_lines = data_lines[1:]
line_labels = [line.split(',')[0] + ' ' + line.split(',')[2] for line in data_lines]
data = np.array([[float(val) for val in line.split(',')[1:]] for line in data_lines])

fig, ax = plt.subplots(figsize=(14, 8))
cmap = plt.get_cmap('viridis')
ax.set_title('Environmental Impact and Sustainability of Major Cities')

for i, line_label in enumerate(line_labels):
    size = 600 + 4400 * (data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2]))
    color = cmap((data[i, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3])))
    ax.scatter(data[i, 0], data[i, 1], s=size, c=color, label=None)
    ax.scatter([], [], c=color, alpha=0.6, s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

sm = ScalarMappable(norm=Normalize(np.min(data[:, 3]), np.max(data[:, 3])), cmap=cmap)
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/272_202312310045.png')
plt.clf()
