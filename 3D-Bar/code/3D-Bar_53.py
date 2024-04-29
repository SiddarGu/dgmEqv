import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data Preparation
x_values = ['HR', 'Finance', 'IT', 'Sales', 'Production']
y_values = ['Number of Employees', 'Employee Satisfaction Rate (%)', 'Average Monthly Salary ($)']
data = np.array([[120, 90, 50], [150, 85, 60], [200, 88, 70], [180, 90, 55], [220, 86, 45]], np.float32)

# Create figure and 3D projection
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting
for i in range(len(x_values)):
    xpos = [i]*len(y_values)
    ypos = np.arange(len(y_values))
    zpos = np.zeros(len(y_values))
    dx = 0.3
    dy = 0.3
    dz = data[i, :]

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, alpha=0.8)

# Configure the axes
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.set_xlabel('Department')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')

# Set title
ax.set_title('Employee Management Analysis by Department')

# Save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/91_202312302126.png')

# Clear the current image
plt.clf()
