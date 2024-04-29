
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Social Media Users (Million)", "Average Time Spent (Minutes)", "Internet Users (Million)"]
x_values = ["North", "South", "East", "West"]
data = np.array([[150, 160, 200], [140, 155, 190], [130, 150, 180], [120, 145, 170]])

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

for i, y in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, 0, 1, 0.5, data[:, i], color='b', alpha=0.3 * (i + 1))

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

ax.set_title("Regional Analysis of Social Media and Web Usage")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5_202312251000.png')
plt.clf()