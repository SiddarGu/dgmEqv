import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import MaxNLocator
from matplotlib.cm import get_cmap

# Data transformation
data_str = '''Harvard,51,401,99,98
Stanford,53,349,94,97
MIT,40,390,96,95
Caltech,15,300,92,94
Yale,36,350,90,93
University of Pennsylvania,42,398,89,92
Columbia,33,380,91,91
Princeton,35,373,95,90
Brown,34,320,90,88
Cornell,40,330,88,89'''

data_labels = ['Enrollment (Thousands)', 'Faculties (Count)', 'Graduation Rate (%)', 'Quality Score (Range 1-100)']
data_list = [row.split(',') for row in data_str.split('\n')]
line_labels = [row[0] + ' ' + row[2] for row in data_list]
data = np.array([[float(val) for val in row[1:]] for row in data_list])

# Plotting
fig, ax = plt.subplots(figsize=(10,8))
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
sizes = 5000*(data[:,2]/data[:,2].max()) + 600

for i, line_label in enumerate(line_labels):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i,0], data[i,1], color=color, s=sizes[i], alpha=0.6, edgecolors='w', linewidth=1, label=None)
    ax.scatter([], [], color=color, s=20, label=line_label)

ax.grid(True)
ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Academics and Enrollment Data of Top US Universities')

cbar = plt.colorbar(ScalarMappable(norm=Normalize(data[:,3].min(), data[:,3].max()), cmap='viridis'), ax=ax)
cbar.set_label(data_labels[3])

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/79_202312301731.png')

plt.close(fig)
