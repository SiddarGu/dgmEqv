
import matplotlib.pyplot as plt
import numpy as np

y_values = ['GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)', 'Interest Rate (%)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[1.9, -2.2, 3.1, 2.5, 3.7],
                 [3.7, 5.2, 4.3, 3.8, 3.2],
                 [2.3, 1.7, 2.1, 2.5, 2.7],
                 [1.5, 0.9, 1.2, 1.3, 1.5]])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, 0, 0.2, 1, data[i], alpha=0.7, color='b', zsort='average')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_zlim(-3, 6)
ax.set_title('Macroeconomic Trends in Business and Finance - 2019 to 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/35_202312251044.png')
plt.cla()