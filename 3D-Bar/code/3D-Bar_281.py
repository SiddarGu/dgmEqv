import matplotlib.pyplot as plt
import numpy as np

# Convert the provided data to variables
x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Number of Internet Users (Million)', 'Mobile Phone Sales (Million)', 'E-commerce Volume (Billion $)']
data = np.array([
    [1200, 750, 1650],
    [1330, 870, 1920],
    [1490, 950, 2180],
    [1600, 1050, 2350],
    [1750, 1200, 2600]
], dtype=np.float32)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(projection='3d')
width = 0.3
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    zpos = [0]*len(x_values)
    dx = [width]*len(x_values)
    dy = [0.5]*len(x_values)
    dz = data[:, i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.5)
    ax.set_title('Technological Growth: Internet, Mobile and E-commerce - 2019 to 2023')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

ax.view_init(elev=35., azim=-65)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/127_202312302126.png')
plt.clf()

