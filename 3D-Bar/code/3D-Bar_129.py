import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data_string = "Quarter,Online Sales ($M),In-store Sales ($M),Total Sales ($M)/n Q1 2020,250,480,730/n Q2 2020,275,460,735/n Q3 2020,300,450,750/n Q4 2020,400,350,750/n Q1 2021,420,330,750"
data_lines = data_string.split("/n")
y_values = data_lines[0].split(',')[1:]
x_values = [line.split(',')[0] for line in data_lines[1:]]
data = np.float32([line.split(',')[1:] for line in data_lines[1:]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Quarterly Sales Performance in Retail and E-commerce (2020-2021)')
ax.view_init(elev=20., azim=-35)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/3D-Bar/png_train/3D-Bar_129.png', dpi=300)
plt.clf()
