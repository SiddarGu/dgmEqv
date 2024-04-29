import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
import numpy as np

data_labels = ['Production Volume (Thousand Units)', 'Revenue ($ Million)', 'Market Share (%)', 'Employee Satisfaction (/10)']
data = np.array([
    [1000, 500, 20, 8],
    [1200, 600, 15, 9],
    [800, 400, 25, 7],
    [500, 300, 10, 6],
    [900, 450, 12, 8] 
])
line_labels = ['Cars', 'Appliances', 'Electronics', 'Furniture', 'Textiles']

fig, ax = plt.subplots(figsize=(14, 10))
cmap = cm.get_cmap('viridis')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

for i in range(len(data)):
    line_label = line_labels[i] + ' ' + str(data[i, 2])
    bubble_size = np.interp(data[i, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
    bubble_color = norm(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(bubble_color)], s=bubble_size, alpha=0.5, label=None)
    ax.scatter([], [], c=[cmap(bubble_color)], s=20, label=line_label)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])    
ax.grid(True)
ax.legend(title=data_labels[2], loc='upper left')

sm = cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

plt.title('Performance Comparison of Manufacturing Industries')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/347_202312311429.png')
plt.clf()

