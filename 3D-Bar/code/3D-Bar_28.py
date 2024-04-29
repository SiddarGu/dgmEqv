
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values
y_values = ["No. of Hospital Beds","No. of Primary Care Providers","No. of Specialists"]
data = np.array([[500,400,200],
                 [300,200,100],
                 [200,100,50]])
x_values = ["Urban", "Suburban", "Rural"]

# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:,i]
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, alpha=0.6, color='#00ceaa')

# Set the dimension of the bars to provide clear visualization
ax.set_xlim3d(0, 3)
ax.set_ylim3d(0, 3)
ax.set_zlim3d(0, 600)

# Rotate the X-axis labels for better readability
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Set grids in the background
ax.grid(True)

# Set title
ax.set_title("Healthcare Capacity Overview by Regio")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/10_202312251000.png")

# Clear the current image state
plt.clf()