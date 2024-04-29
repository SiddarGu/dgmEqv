
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Market Share (%)', 'Revenue ($ Billion)', 'Growth Rate']
data = np.array([[20, 200, 300], [15, 150, 180], [10, 100, 60], [15, 50, 40], [12, 20, 20]])
x_values = ['McDonalds', 'KFC', 'Burger King', 'Starbucks', 'Subway']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(x_values))

for i in range(len(y_values)):
    y_pos = [i] * len(x_values)
    ax.bar3d(x_pos, y_pos, np.zeros(len(x_values)), 0.5, 0.5, data[:, i],
            shade=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

ax.set_xticks(x_pos)
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.grid(True, linestyle='-', color='grey')
ax.set_title('Food and Beverage Industry Market Overview')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/8.png')
plt.cla()