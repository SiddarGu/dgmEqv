
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Online Sales ($billion)', 'Retail Store Sales ($billion)', 'Total Sales ($billion)']
data = np.array([[2.5, 3.5, 6.0], [1.5, 2.5, 4.0], [2.0, 3.0, 5.0], [2.2, 3.3, 5.5]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    zs = data[:, i]
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.2, 0.2, zs, alpha=0.8, color=plt.cm.rainbow(i / len(y_values)), edgecolor='k')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

ax.set_title('Retail and E-commerce Market Performance by Region')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/25_202312270030.png')
plt.clf()