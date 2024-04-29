import matplotlib.pyplot as plt
import numpy as np

# data representation
y_values = ['Movie Tickets Sold (Million)', 'Music Records Sold (Million)', 'Video Game Sales (Million)']
x_values = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
data = np.array([[100, 85, 120],
                 [80, 95, 110],
                 [90, 88, 100],
                 [70, 75, 85],
                 [110, 92, 128]], dtype=np.float32)

# plot setup
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# heterogeneous properties
_colors = ['r', 'b', 'g', 'y', 'c']
_alphas = [0.1, 0.2, 0.3, 0.4, 0.5]

for i in range(len(y_values)):
    # ensure non-overlapping bars  
    _x = np.arange(len(x_values)) + i * 0.15 
    _y = [i]*len(x_values)
    ax.bar3d(_x, _y, np.zeros(len(x_values)), 0.15, 0.5, data[:, i], 
             color=_colors[i], alpha=_alphas[i])

# labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)) + 0.2)
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# title and grid
ax.set_title('Sales Volume of Sports and Entertainment Items by Genre')
plt.grid()

# view angle
ax.view_init(elev=20, azim=-35)

plt.tight_layout()
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/109_202312302126.png')
plt.clf()
