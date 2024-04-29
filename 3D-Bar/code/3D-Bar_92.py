import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Initialize data
data = np.array([
    [79.6, 2000, 159.2], 
    [57.6, 1800, 103.7], 
    [89.4, 1700, 151.9], 
    [82.8, 1500, 124.2], 
    [62.1, 2100, 130.4]], dtype=np.float32)
x_values = ['USA', 'China', 'France', 'Spain', 'Italy']
y_values = ['Number of Tourists (Million)', 
            'Average Spend per Tourist ($)', 
            'Total Revenue from Tourism ($ Billion)']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# bar width and depth
width = depth = 0.6 
alpha = 0.8

colors = ['r', 'g', 'b']
yticks = np.arange(3)

for i in range(3):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros_like(data[:, i]), 
             width, depth, data[:, i], color=colors[i], alpha=alpha)

ax.set_title('Tourism and Hospitality Revenue by Country')
ax.set_xlabel('Country')
ax.set_zlabel('Value')

# set xticks and yticks position
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(yticks)

# set xticks and yticks label
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# adjust layout and save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/209_202312302235.png')
plt.clf()
