import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Preprocessing the data
data_string = "Case Type,Number of Cases Submitted,Number of Cases Settled," \
              "number of Cases Escalated\n Civil Cases,1200,850,1050\n Criminal Cases," \
              "900,500,670\n Family Cases,750,480,600\n Corporate Cases,800,550,720\n Employment Law Cases,350,260,320 "

data_lines = data_string.split('\n')
y_values = data_lines[0].split(',')[1:]
x_values = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([[int(num) for num in line.split(',')[1:]] for line in data_lines[1:]], dtype=np.float32)

# Creating the figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')
width = depth = 0.6

# Plotting data
for i in range(data.shape[1]):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    zs = [0]*len(x_values)
    ax.bar3d(xs, ys, zs, width, depth, data[:, i], alpha=0.5, color=('r', 'b', 'g')[i%3])

# Setting labels and ticks
ax.set_xticks(np.arange(len(x_values)) + width/2)
ax.set_yticks(np.arange(len(y_values)) + width/2)
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Adjusting the view and grid
ax.view_init(azim=-50)
ax.grid(True)

# Setting title
plt.title('Analysis of Case Type vs Case Progress in Legal Affairs')

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/126_202312302126.png')
plt.clf()
