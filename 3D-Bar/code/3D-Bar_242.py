import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([
    [90, 400, 490],
    [120, 380, 500],
    [150, 370, 520],
    [200, 360, 560],
    [220, 350, 570]
])
y_values = ['Online Sales ($ Billion)', 'Retail Sales($ Billion)', 'Total Sales ($ Billion)']
x_values = ['2017', '2018', '2019', '2020', '2021']

num_x, num_y = data.shape
figsize = max(8, min(15, num_x, num_y))

fig = plt.figure(figsize=(figsize, figsize))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(x_values)):
    xpos = [i]*len(y_values)
    ypos = np.arange(len(y_values))
    zpos = np.zeros(len(y_values))
    dx = 0.3
    dy = 0.3
    dz = data[i, :]

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, alpha=0.8)

ax.set_xlabel('Years')
ax.set_ylabel('Sales Metrics')
ax.set_zlabel('Value in Billion $')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Analysis of Retail and E-commerce Sales from 2017 to 2021')

ax.view_init(elev=15, azim=30)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/79_202312302126.png', dpi=300)
plt.close(fig)
