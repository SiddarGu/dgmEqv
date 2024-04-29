
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Vegetable Production (Tonnes)', 'Fruit Production (Tonnes)', 'Grain Production (Tonnes)', 'Poultry Production (Tonnes)']
data = np.array([[4500, 6000, 7000, 8000],
                 [3000, 5000, 8000, 9500],
                 [4500, 4800, 6500, 7500],
                 [5500, 6600, 7500, 8500]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0] * len(x_values), 0.5, 0.5, data[:, i], alpha=0.5, color='#FFA500')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left', rotation=-15)
ax.set_title('Regional Analysis of Food Production in Agriculture')

plt.tight_layout()
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/4_202312251044.png')
plt.clf()