import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([
    [439, 480, 410, 433],
    [452, 493, 415, 440],
    [467, 507, 420, 447],
    [482, 522, 425, 454],
    [497, 537, 430, 461]
], dtype=np.float32)

x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Internet Users (Millions)', 'Mobile Users (Millions)', 'Software Sales ($ Billion)', 'IT Service Spending ($ Billion)']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.full(len(x_values), 0), 0.4, 0.8, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_title("Evolution of Internet and Mobile Usage, Software Sales and IT Service Spending - 2019 to 2023")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/143_202312302235.png')
plt.show()
plt.clf()
