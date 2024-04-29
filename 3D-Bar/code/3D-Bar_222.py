
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Revenue ($ million)', 'Net Profit ($ million)', 'Number of Stores']
data = np.array([[27000, 5250, 20000], [17000, 2700, 15000], [11000, 1800, 12000], [9000, 1200, 10000], [8000, 2100, 25000]])
x_values = ['McDonalds', 'Burger King', 'KFC', 'Subway', 'Starbucks']

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, alpha=0.8, color=plt.cm.tab10(i))

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Financial Performance of Major Food and Beverage Chains')

plt.tight_layout()
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/11_202312251000.png')
plt.clf()