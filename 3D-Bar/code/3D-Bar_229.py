

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[500, 400, 200, 250],
                 [800, 650, 400, 500],
                 [250, 200, 150, 100],
                 [500, 140, 130, 150]])

x_values = np.array(['India', 'China', 'USA', 'UK'])
y_values = np.array(['Internet Users (Millions)', '3G/4G Subscribers (Millions)',
                     'Broadband Connections (Millions)', 'Average Download Speed (Mbps)'])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(4):
    xs = np.array([i]*4)
    ys = np.arange(4)
    ax.bar3d(xs, ys, np.zeros(4), 1, 1, data[:, i], alpha=0.5, color='#777777')

ax.set_xticks(np.arange(4))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(4))
ax.set_yticklabels(y_values)
ax.set_zlabel('Values')
ax.set_title('Global Internet Usage and Connectivity Trends')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/21.png')
plt.clf()