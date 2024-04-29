import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

raw_data = "Departments,Employee Size,Average Working Hours,Employee Satisfaction (%),Turnover Rate (%)\n IT,250,40,75,10\n Marketing,150,45,80,12\n HR,60,40,85,8\n Operations,500,45,70,15\n Sales,350,50,65,20\n Finance,200,45,80,7\n Engineering,400,50,70,15"
raw_data = raw_data.split("\n")
data_labels = raw_data[0].split(",")[1:]

data = []
line_labels = []
for row in raw_data[1:]:
    split_row = row.split(",")
    line_labels.append(split_row[0] + split_row[2])
    data.append([float(i) for i in split_row[1:]])

data = np.array(data)

fig, ax = plt.subplots(figsize=(10, 6))

cmap = plt.get_cmap("viridis")
colors = Normalize()(data[:, 3])
radii = 600 + (data[:, 2] - np.min(data[:, 2]))/(np.max(data[:, 2]) - np.min(data[:, 2])) * (5000 - 600)

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=radii[i], color=cmap(colors[i]), alpha=0.6, edgecolors="w", label=None)
    ax.scatter([], [], color=cmap(colors[i]), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

mappable = ScalarMappable(cmap=cmap)
mappable.set_array(data[:, 3])
fig.colorbar(mappable, ax=ax, label=data_labels[3])

ax.set_ylabel(data_labels[0])
ax.set_xlabel(data_labels[1])
plt.title("Implications of HR Strategies on Employee Engagement and Turnover Rates")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/242_202312310045.png")
plt.clf()
