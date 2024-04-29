
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Number of Organizations', 'Total Donations ($000)', 'Average Donation ($000)']
data = np.array([[250, 800, 360],
                 [280, 900, 320],
                 [210, 700, 330],
                 [220, 750, 340]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, projection='3d')

for i, y_value in enumerate(y_values):
    data_y = data[:, i]
    x_pos = np.arange(len(x_values))
    y_pos = [i] * len(x_values)
    width = depth = 1.0
    bottom = [0] * len(x_values)
    ax.bar3d(x_pos, y_pos, bottom, width, depth, data_y,
             shade=True, color='#2F4F4F')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)
plt.title('Regional Overview of Nonprofit Organizations and Donations')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/30_202312251044.png')
plt.cla()