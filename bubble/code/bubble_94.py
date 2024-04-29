import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.cm import ScalarMappable
import numpy as np

# Transform the data to appropriate format
_data = '''Graphene,12,280,2.1,9
AI Technology,50,500,4.5,7
Quantum Computing,25,350,3.2,8
Biotechnology,27,410,3.8,8
Nanotechnology,15,300,2.4,9
Robotics,30,450,4,7'''

data = np.array([row.split(',') for row in _data.split('\n')])
data_vals = data[:, 1:].astype(float)
# The normalizer for color
norm = mpl.colors.Normalize(vmin=data_vals[:, -1].min(), vmax=data_vals[:, -1].max())
cmap = plt.cm.viridis

data_labels = ['Research Investment (Billion $)', 'Patent Filed', 'Jobs Generated (Millions)', 'Safety Rating (Score)']
line_labels = [f'{line[0]} {line[3]}' for line in data]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Map the third value to the bubble size, range [600, 5000]
sizes = (data_vals[:, 2] - data_vals[:, 2].min()) / (data_vals[:, 2].max() - data_vals[:, 2].min()) * 4400 + 600

# Map the fourth value to color value
colors = norm(data_vals[:, -1])

for i in range(len(data_vals)):
    line_label = line_labels[i]
    ax.scatter(data_vals[i, 0], data_vals[i, 1], s=sizes[i], c=[cmap(colors[i])], label=None)
    ax.scatter([], [], c=[cmap(colors[i])], label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(ScalarMappable(norm=norm, cmap=cmap), ax=ax).set_label(data_labels[3])

ax.grid(True)
plt.title('Investment and Output in Science and Engineering Fields')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/92_202312301731.png')
plt.clf()
