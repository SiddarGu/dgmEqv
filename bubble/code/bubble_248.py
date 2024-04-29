

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np

data_labels = ['Popularity (Score)', 'Revenue (Billion $)', 'Attendance (Millions)', 'Viewership (Millions)']
line_labels = ['Football', 'Basketball', 'Baseball', 'Hockey', 'Soccer', 'Golf']
data = np.array([[90, 30, 4, 1.5], 
                 [80, 25, 3, 2], 
                 [70, 15, 2.5, 1], 
                 [60, 10, 1.8, 0.8], 
                 [50, 8, 1.2, 0.6], 
                 [40, 5, 1, 0.4]])

fig, ax = plt.subplots(figsize=(15, 10))

norm = colors.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
scalarMap = cm.ScalarMappable(norm=norm, cmap=cm.RdYlGn)

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - min(data[:, 2])) / (max(data[:, 2]) - min(data[:, 2])) * 5000 + 600,
               c=scalarMap.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=scalarMap.to_rgba(data[i, 3]), s=20, label=line_labels[i] + f': {data[i, 2]}')

cbar = fig.colorbar(scalarMap, ax=ax, pad=0.04)
cbar.ax.set_title(data_labels[3], fontsize=15)
ax.legend(title=data_labels[2], loc='lower right')

ax.set_xlabel('Popularity (Score)', fontsize=15)
ax.set_ylabel('Revenue (Billion $)', fontsize=15)
ax.grid(True)
ax.set_title('Popularity and Profitability of Sports and Entertainment Events', fontsize=20)

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/12_2023122261326.png')
plt.clf()