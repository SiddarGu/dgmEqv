import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

data_labels = ["Crop", "Production Volume (Million Tonnes)", "Land Used (Million Hectares)", "Profit Margin (%)", "Sustainability (Score)"]
data = np.array([
    [730, 220, 20, 8],
    [1150, 180, 25, 6],
    [490, 160, 15, 10],
    [350, 120, 30, 7],
    [370, 100, 18, 10],
    [120, 70, 12, 9],
    [250, 90, 22, 8],
    [180, 80, 17, 9],
    [200, 75, 16, 7],
    [100, 50, 11, 9]
])
line_labels = ["Wheat", "Corn", "Rice", "Soybeans", "Potatoes", "Apples", "Grapes", "Bananas", "Tomatoes", "Carrots"]

fig, ax = plt.subplots(figsize=(10, 6))
cmap = cm.get_cmap('viridis')
colors = Normalize(min(data[:, 3]), max(data[:, 3]))
sizes = Normalize(min(data[:, 2]), max(data[:, 2]))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(colors(data[i, 3])),
               s=600 + sizes(data[i, 2]) * 5000, alpha=0.6, edgecolors='w', 
               label=None)
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=f'{line_labels[i]} {data[i, 2]}')

ax.legend(title=data_labels[2])
ax.grid(True)

ColorbarBase(plt.gcf().add_axes([0.95, 0.2, 0.03, 0.6]), cmap=cmap,
             norm=Normalize(min(data[:, 3]), max(data[:, 3])),
             orientation='vertical').set_label(data_labels[3])

ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.set_title('Crop Production and Land Use - Agriculture 2023')
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/346_202312311429.png')
plt.close()
