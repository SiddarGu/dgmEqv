import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [100, 150, 500],
    [108, 180, 550],
    [115, 200, 600],
    [125, 230, 650],
    [130, 280, 700],
    [135, 320, 750]
    ], dtype=np.float32)

y_values = ['Revenue (Billion $)', 'Profit (Billion $)', 'Total Employees (In Thousands)']
x_values = ['2015', '2016', '2017', '2018', '2019', '2020']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    x = np.arange(len(x_values))
    y = [i]*len(x_values)
    z = np.zeros(len(x_values))
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:, i]
    ax.bar3d(x, y, z, dx, dy, dz, color='b', alpha=0.3)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation = 45)
ax.set_yticklabels(y_values, ha='left')

plt.title('Food and Beverage Industry Revenue, Profit and Employment Analysis from 2015 to 2020')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/224_202312302235.png')
plt.close(fig)
