import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data
data_str = """Field,Number of Research Papers,Number of Patents Granted,Number of New Projects
Electrical Engineering,600,700,800
Aeronautics,450,500,600
Biotechnology,550,650,700
Artificial Intelligence,650,750,800
Nanotechnology,400,450,550"""
data_str = data_str.split('\n')

header = data_str[0].split(',')
data = np.array([line.split(',')[1:] for line in data_str[1:]], dtype=np.float32)
x_values = [line.split(',')[0] for line in data_str[1:]]
y_values = header[1:]

# Create 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
colors = ['r', 'g', 'b']

# Plot data
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.4, 0.5, data[:, i], color=colors[i], alpha=0.6)

# Configure x and y ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, va='center')

# Configure other plot attributes
ax.set_title('Science and Engineering Contributions in Different Fields')
ax.set_zlabel('Contributions')
ax.grid(True)
ax.view_init(elev=20., azim=-35)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/236_202312310050.png', dpi=300)

# Clear figure
plt.clf()
