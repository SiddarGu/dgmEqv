

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ['Productivity (Score)','Retention (Score)','Turnover (%)','Benefits (Score)']
data = np.array([[90,80,3,8],
                 [70,85,5,5],
                 [85,90,2,10],
                 [95,75,4,7],
                 [80,95,1,9],
                 [100,80,2,10]])
line_labels = ['Office','Warehouse','Manufacturing','Sales','Logistics','IT']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
norm = plt.Normalize(vmin=data[:,3].min() - 1, vmax=data[:,3].max())
scalar_map = cm.ScalarMappable(norm=norm, cmap=cm.Blues_r)
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*5000/data[:,2].max(), c=scalar_map.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=scalar_map.to_rgba(data[i, 3]), label=line_labels[i] + f' {data[i, 2]}')
ax.legend(title=data_labels[2], loc='upper left')
cbar = fig.colorbar(scalar_map, ax=ax, shrink=0.8)
cbar.set_label(data_labels[3], rotation=270, labelpad=20)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Employee Performance and Retention in Human Resources and Employee Management')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/27_2023122270050.png')
plt.clf()