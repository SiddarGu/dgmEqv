import numpy as np
import matplotlib.pyplot as plt

data=np.array([
    [3000, 4000, 3500],
    [3200, 4200, 3700],
    [3400, 4500, 3900],
    [3700, 4600, 4000],
    [4000, 4800, 4300]
], dtype=np.float32)

x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Smartphone Users (millions)', 'Internet Users (millions)', 'Social Media Users (millions)']

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')

_x = np.arange(data.shape[0])
_y = np.arange(data.shape[1])
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

ax.bar3d(x, y, np.zeros_like(x), dx=0.5, dy=0.5, dz=data.ravel(), color='b', alpha=0.8)

ax.set_yticks(np.arange(data.shape[1]))
ax.set_xticks(np.arange(data.shape[0]))
ax.set_yticklabels(y_values, ha='left')
ax.set_xticklabels(x_values, rotation=45)

fig.suptitle('Trend of Technology and Internet Usage from 2019 to 2023') 
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/60_202312302126.png')
plt.clf()
