import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# transforming the given data into x, y values and data array
x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Number of Internet Users (Billions)', 'E-commerce Sales (Trillion $)', 'Number of Online Services (Millions)']
data = np.array([[4.39, 3.53, 24], [4.66, 4.27, 28], [4.93, 5.04, 32], [5.08, 5.79, 36], [5.27, 6.56, 40]])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111,projection='3d')

colors = ['cyan', 'magenta', 'yellow']
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=15)
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Internet Usage, E-commerce and Online Services Growth 2019-2023')
ax.grid(True)

# Rotating the plot for better view
ax.view_init(elev=20, azim=-135)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/178_202312302235.png', dpi=300)
plt.clf()
