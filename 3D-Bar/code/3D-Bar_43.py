

import numpy as np
import matplotlib.pyplot as plt

y_values = ['Online Sales ($Billion)', 'Retail Store Sales ($Billion)', 'Total Retail Sales ($Billion)']
data = np.array([[2.5, 3.4, 5.9], [3.7, 3.8, 7.5], [5.1, 4.2, 9.3], [6.2, 4.6, 10.8], [7.6, 4.8, 12.4]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    zs = data[:,i]
    ax.bar3d(xs, ys, np.zeros(len(xs)), 0.5, 0.5, zs, alpha=0.6)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

plt.title("Growth of Retail and E-commerce Sales - 2019 to 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/16_202312251044.png')
plt.clf()