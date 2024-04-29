import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_str = 'Cancer,17,70,20,150/n Cardiovascular Diseases,35,60,30,90/n Diabetes,46,10,85,80/n Respiratory Diseases,30,50,40,60/n HIV/AIDS,38,60,35,100/n COVID-19,200,2,97,200'
data_str = data_str.replace("/n ", "\n")
data_lines = data_str.split("\n")
data_labels = ['Disease', 'Total cases (Million)', 'Death Rate (%)', 'Recovery Rate (%)', 'Research Investment (Billion $)']
line_labels = [row.split(',')[0] for row in data_lines]
data = np.array([list(map(float, row.split(',')[1:])) for row in data_lines])

fig, ax = plt.subplots(figsize=(10, 6))
cmap = plt.get_cmap('viridis')

for i, line_label in enumerate(line_labels):
    size = 600 + 4400 * (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())
    color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
    ax.scatter(data[i, 0], data[i, 1], label=None, s=size, c=[cmap(color)], alpha=0.6)
    ax.scatter([], [], label=line_label + "_" + str(data[i, 2]), color=cmap(color), s=20)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

norm = Normalize(data[:, 3].min(), data[:, 3].max())
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])

cbar = plt.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title('Global Impact and Research Investment in Major Diseases', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/318_202312310045.png')
plt.close()
