
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Fruit Production (Tons)', 'Vegetable Production (Tons)', 'Meat Production (Tons)', 'Dairy Production (Tons)']
x_values = ['North', 'South', 'East', 'West']
data = np.array([[150, 300, 200, 400],
                 [125, 400, 220, 350],
                 [175, 325, 250, 375],
                 [200, 350, 270, 400]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for i, y in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    bottom = np.zeros(len(x_values))
    width = depth = 1
    ax.bar3d(xs, ys, bottom, width, depth, data[:, i], shade=True, color='r')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

ax.set_title('Regional Food Production Analysis - Agricultural Outputs')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/19_202312251044.png')
plt.clf()