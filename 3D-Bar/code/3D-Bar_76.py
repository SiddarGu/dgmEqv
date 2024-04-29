
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Research and Development Cost ($ Million)", "Engineering Cost ($ Million)", "Labor Cost ($ Million)"]
x_values = ["AI-assisted Manufacturing", "Autonomous Vehicle", "Quantum Computing", "Augmented Reality"]
data = np.array([[150, 200, 250],
                 [100, 120, 140],
                 [80, 100, 120],
                 [70, 90, 110]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(x_values))
dx = 0.2

for i in range(len(y_values)):
    ypos = [i] * len(x_values)
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, 0.8, data[:, i], alpha=0.7, label=y_values[i], zsort='average')

ax.set_title('Science and Engineering Expenditure: A Comparison of Projects')
ax.set_xticks(xpos)
ax.set_xticklabels(x_values, rotation=30, ha='right', wrap=True)
ax.set_xlabel('Project')
ax.grid(True, zorder=5)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/38.png')
plt.clf()