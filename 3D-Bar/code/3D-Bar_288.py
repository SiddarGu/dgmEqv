
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values
y_values = ["GDP ($ Hundred billion)", "Unemployment Rate (%)", "Population (million)"]
data = np.array([[5, 4.5, 20], [6, 5.5, 30], [4.5, 3.5, 25], [5.5, 6.5, 15]])
x_values = ["North", "South", "East", "West"]

# Plot the data with the type of 3D bar chart.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use ax.set_xticklabels and ax.set_yticklabels to label x-axis and y-axis
x_range = np.arange(len(x_values))
ax.set_xticks(x_range)
ax.set_xticklabels(x_values)
y_range = np.arange(len(y_values))
ax.set_yticks(y_range)
ax.set_yticklabels(y_values)

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    dx = 0.5
    dy = 0.5
    dz = data[:, i]
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#00ceaa', alpha=0.7)

# Rotate the X-axis labels for better readability
ax.view_init(elev=45, azim=45)

# Add title and background grids
plt.title("Government and Public Policy Analysis by Region")
ax.grid(True)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image as "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/13.png"
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/13.png")

# Clear the current image state at the end of the code
plt.clf()