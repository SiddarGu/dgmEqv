import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data = np.array([
      [10, 200, 20],
      [12, 225, 27],
      [15, 250, 37.5],
      [18, 275, 49.5],
      [20, 300, 60]
])

x_values = ['2018', '2019', '2020', '2021', '2022']
y_values = ['Profit Margin (%)','Revenue (Million $)','Net Income (Million $)']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r','b','g']
yticks = np.arange(len(y_values))

for c, k in zip(colors, yticks):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    ax.bar(xs, ys, zs=k, zdir='y', color=c, alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Financial Performance Trends of a Company - 2018 to 2022')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/270_202312310050.png')
plt.clf()
