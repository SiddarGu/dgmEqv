
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Capacity (People)', 'Speed (km/hr)', 'Cost ($)']
x_values = ['Air', 'Train', 'Bus', 'Truck']
data = np.array([[200, 800, 1500], [2000, 200, 600], [50, 100, 100], [10, 80, 200]])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, alpha=0.8)

ax.set_title('Comparing Transportation Modes for Logistics - Capacity, Speed, and Cost')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=15)
ax.set_yticklabels(y_values)
fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/6_202312251044.png')
plt.clf()