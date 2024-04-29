import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_string = "Quarter,Online Sales ($m),In-Store Sales ($m),Total Revenue ($m)/n Q1,101.5,175.2,276.7/n Q2,125.3,180.7,306/n Q3,137.6,200.4,338/n Q4,205,215.3,420.3"
data_string = data_string.replace("/n", "\n")

dataset = np.array([item.split(',') for item in data_string.split('\n')])

x_values = dataset[1:, 0]
y_values = dataset[0, 1:]
data = dataset[1:, 1:].astype(np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_bar = np.arange(len(x_values))

colors = ['b', 'g', 'r', 'purple']
for i in range(len(y_values)):
    ax.bar3d(x_bar, [i]*len(x_values), np.zeros(len(x_values)), 0.1, 0.4, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(x_bar)
ax.set_yticks(range(len(y_values)))

ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.grid(True)

ax.set_title('Quarterly Retail Sale: Online Vs In-Store (in Million Dollars)', pad=20)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/94_202312302126.png', dpi=300, bbox_inches='tight')

plt.close(fig)
