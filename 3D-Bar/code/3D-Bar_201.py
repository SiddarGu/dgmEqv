import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data
table = [['USA', 63, 180, 113], ['UK', 75, 165, 123], ['France', 68, 200, 136], ['China', 70, 150, 105], ['Canada', 60, 130, 78]]
table = np.array(table)
x_values = table[:, 0]
y_values = ["Hotel Occupancy Rate (%)", "Average Daily Rate ($)", "Revenue Per Available Room ($)"]
data = np.float32(table[:, 1:])

# Create 3D figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
for i in range(data.shape[1]):
    x = np.arange(len(x_values))
    y = [i]*len(x_values)
    z = np.zeros(len(x_values))
    dx = np.ones(len(x_values))*0.3  # bar width
    dy = np.ones(len(x_values))*0.7  # depth
    dz = data[:, i]  # data
    ax.bar3d(x, y, z, dx, dy, dz, color=plt.cm.viridis(i/data.shape[1]), alpha=0.6)

# Customize the axes
ax.set_title('Global Analysis of Hospitality Industry Metrics by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Adjust the viewing angle for better readability
ax.view_init(elev=30, azim=220)

# Save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/198_202312302235.png', dpi=300)

# Clear the current figure
plt.clf()
