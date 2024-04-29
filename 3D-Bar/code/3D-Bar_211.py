
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Revenue ($ Billion)', 'Profit ($ Million)', 'Number of Employees']
x_values = ['2019', '2020', '2021', '2022','2023']
data = np.array([[120, 300, 300], [100, 250, 270], [130, 280, 320], [140, 310, 340], [150, 320, 350]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0] * len(x_values), 0.5, 0.5, data[:, i], shade=True)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.set_title("Business and Finance Summary - 2019 to 2023")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/9_202312251044.png')

plt.clf()