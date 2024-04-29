
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Museums (No.)", "Galleries (No.)", "Theatres (No.)", "Cultural Events (No.)"]
x_values = ["North", "South", "East", "West"]
data = np.array([[20, 30, 15, 40], [25, 35, 25, 50], [15, 20, 10, 30], [30, 40, 20, 45]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    cs = ['b', 'g', 'r', 'c']
    ax.bar3d(xs, ys, [0]*len(x_values), 0.5, 0.5, data[:, i], edgecolor = cs, color = cs)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title("Cultural Landscape of Different Regions")
ax.view_init(elev=20., azim=-35)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/1.png")
plt.clf()