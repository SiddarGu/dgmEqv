import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([[15, 20, 30],
                 [20, 22, 32],
                 [25, 26, 35],
                 [29, 30, 40],
                 [33, 34, 45]], dtype=np.float32)

y_values = ['Healthcare Budget($B)','Education Budget($B)','Infrastructure Budget($B)']

x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']

for i in range(data.shape[1]):  # for each column of data
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.4, 1, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Government Spending on Key Public Policy Areas 2019-2023')

ax.view_init(elev=10, azim=150)  # adjust viewing angles
ax.grid(True)  # add background grid for better clarity

plt.tight_layout()  # to fit all contents
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/185_202312302235.png')

plt.clf()  # clear the current image
