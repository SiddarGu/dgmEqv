
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Painting', 'Sculpture', 'Photography', 'Music']
data = np.array([[1200, 500, 700, 500],
 [1000, 550, 650, 550],
 [1100, 600, 750, 570],
 [1050, 700, 780, 620],
 [1200, 1680, 790, 640]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
colors = ['b', 'g', 'r', 'c']

for i in range(len(y_values)):
    x_pos = np.arange(len(x_values))
    y_pos = [i]*len(x_values)
    ax.bar3d(x_pos, y_pos, np.zeros(len(x_values)), 1, 1, data[:,i], color=colors[i], alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Arts and Culture Participation Trends - 2019 to 2023')
ax.view_init(elev=30., azim=60)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/23_202312251036.png')
plt.clf()