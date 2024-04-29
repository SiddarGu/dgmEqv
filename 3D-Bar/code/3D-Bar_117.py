
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Speed (km/h)', 'Fuel Efficiency (km/L)','Capacity (Tonnes)']
data = np.array([[80, 10, 2],
                 [120, 20, 5],
                 [200, 2, 20],
                 [50, 20, 10]])
x_values = ['Road', 'Rail', 'Air', 'Water']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.8, data[:,i], alpha=0.5, color=plt.cm.tab20(i))

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.set_title('Transportation and Logistics Performance Comparison')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/41_202312251044.png')

plt.clf()