import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([[50, 60, 70], [65, 85, 95], [80,100,105],[90,120,130], [100,130,150]], dtype=np.float32)
y_values = ['Number of Tourists (Millions)', 'Revenue from Tourism ($ Billion)', 'Number of Hotels']
x_values = ['2020', '2021', '2022', '2023', '2024']

fig = plt.figure(figsize=(12, 8))

ax1 = fig.add_subplot(111, projection='3d')
ax1.set_title("Tourism and Hospitality Trends from 2020 to 2024")

width = depth = 0.3
color_list = ['r', 'g', 'b']
alpha = 0.7

for c in range(data.shape[1]):
    x = np.arange(data.shape[0])
    y = [c]*data.shape[0]
    z = np.zeros(data.shape[0])
    dx = [width]*data.shape[0]
    dy = [depth]*data.shape[0]
    dz = data[:, c]
    color = color_list[c]
    ax1.bar3d(x, y, z, dx, dy, dz, color=color, alpha=alpha)

ax1.set_xlabel('Year')
ax1.set_xticks(np.arange(len(x_values)))
ax1.set_xticklabels(x_values, rotation=20, va='baseline')
ax1.set_yticks(np.arange(len(y_values)))
ax1.set_yticklabels(y_values, ha='left')
ax1.view_init(azim=-50, elev=20)
ax1.grid(True)

# Rescale the axis for tight layout
plt.autoscale(tight=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/217_202312302235.png')

# Clear plot
plt.clf()
