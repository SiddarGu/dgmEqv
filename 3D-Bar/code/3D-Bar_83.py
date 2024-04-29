
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Number of Law Firms", "Average Cost per Hour (USD)", "Number of Cases"]
x_values = ["North", "South", "East", "West"]
data = np.array([[400,150,250],
                [500,120,300],
                [600,140,350],
                [700,160,400]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for i, y_value in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros_like(data[:, i]), 0.8, 0.8, data[:, i], color=plt.cm.jet(xs/len(x_values)))

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.view_init(30, -15)

ax.set_title('Law and Legal Affairs - An Analysis of Regional Variability')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/28_202312270030.png')
plt.clf()