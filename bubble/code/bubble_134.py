import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

data_string = """Policy Area,Funding Allocation ($),Effectiveness Score,Public Satisfaction (%),Impact on Economy (%)
Education,500,7.5,70,3
Healthcare,800,8,75,5
Transportation,300,6.5,65,2
Environment,200,7,68,1
Defense,1000,9,80,7"""
data_list = [i.split(',') for i in data_string.split('\n')]
data_labels = data_list[0][1:]
line_labels = [f"{i[0]} {i[2]}" for i in data_list[1:]]
data = np.array([i[1:] for i in data_list[1:]], dtype=float)

fig, ax = plt.subplots(figsize=(12,8)) 
sc = plt.scatter(data[:, 0], data[:, 1], s=np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000)), 
                 c=data[:, 3], cmap=cm.viridis, edgecolors='k', label=None)

for i,line_label in enumerate(line_labels):
    plt.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

plt.legend(title=data_labels[2])

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cbar = fig.colorbar(ScalarMappable(norm=norm, cmap=cm.viridis), ax=ax)
cbar.set_label(data_labels[3])

plt.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_title('Evaluation of Government Policies by Policy Area')
plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/388_202312311429.png')
plt.clf()
