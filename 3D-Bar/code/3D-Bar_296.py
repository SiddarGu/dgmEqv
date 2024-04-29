
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Average Math Score", "Average English Score", "Average Science Score"]
data = np.array([[90,87,84], [83,80,77], [76,73,70], [68,65,62]])
x_values = ["Elementary", "Middle", "High", "University"]

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(111, projection="3d")

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros_like(data[:,i]), 0.5, 0.5, data[:,i], shade = True, alpha = 0.5, color = 'g')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

ax.set_xticklabels(x_values, rotation = 45)
ax.set_yticklabels(y_values)

ax.set_title("Educational Performance by Grade Level")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/9_202312270030.png")
plt.clf()