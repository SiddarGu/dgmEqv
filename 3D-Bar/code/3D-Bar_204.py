
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

y_values = ['Wheat Production (Million Tonnes)', 'Corn Production (Million Tonnes)', 'Rice Production (Million Tonnes)', 'Soybean Production (Million Tonnes)']
data = np.array([[250, 300, 200, 150], [300, 350, 250, 200], [200, 250, 150, 100], [275, 325, 225, 175]])
x_values = ['North', 'South', 'East', 'West']

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:, i], alpha=0.2, color='b')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.set_title('Regional Food Production - A Comparative Analysis')
ax.set_xlabel('Regions')
ax.set_ylabel('Metrics')
ax.set_zlabel('Production (Million Tonnes)')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/14_202312251000.png')
plt.clf()