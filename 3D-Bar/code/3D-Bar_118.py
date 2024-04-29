import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
data_str = """Country,Meat Production (Million Tonnes),Dairy Production (Million Tonnes),Fruit Production (Million Tonnes),Vegetable Production (Million Tonnes)
USA,120,60,65,80
China,130,45,70,103
Brazil,100,30,60,70
Australia,50,25,37,58
UK,40,28,26,45"""

data_array = np.array([item.split(',') for item in data_str.split('\n')])
x_values = data_array[1:, 0]
y_values = data_array[0, 1:]
data = np.float32(data_array[1:, 1:])

# Create figure and 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Prepare bar dimensions as per data length
colors = ['r', 'g', 'b', 'y']
xticks_locs = np.arange(len(x_values))
yticks_locs = np.arange(len(y_values))
x_mat, y_mat = np.meshgrid(xticks_locs, yticks_locs)

# Iterate over y_values to plot each column of data
for i, y_val in enumerate(y_values):
    ax.bar3d(x_mat[i], y_mat[i], np.zeros(len(x_values)), 0.4, 0.4, data[:, i], color=colors[i%len(colors)], alpha=0.7)

# Labeling and viewing angles
ax.set_xticks(xticks_locs)
ax.set_yticks(yticks_locs)
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.view_init(elev=30., azim=-45)

# Title
plt.title('Global Food Production Analysis by Country')

# Resize image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/71_202312302126.png', dpi=300)

# Clear figure
plt.clf()
