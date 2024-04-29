
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data
y_values = ['Sports Revenue ($ Billion)', 'Entertainment Revenue ($ Billion)', 'Number of Sports Events', 'Number of Entertainment Events']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[60, 90, 100, 200], [65, 95, 110, 205], [70, 100, 120, 210], [75, 105, 230, 215], [80, 110, 140, 220]])

# Create figure
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    zpos = np.zeros(len(x_values))
    dx = 0.5 * np.ones(len(x_values))
    dy = 0.4 * np.ones(len(x_values))
    dz = data[:, i]

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=plt.cm.jet(i/len(y_values)))

# Customizing axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90, fontsize=10)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=10)

# Setting title and adjusting view
ax.set_title('Sports and Entertainment Industry Revenue Trends - 2019 to 2023', fontsize=16)
ax.view_init(30, -35)

# Drawing techniques such as background grids can be used
ax.grid(True)

# Rotate the X-axis labels for better readability
plt.xticks(rotation=90)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/15.png')

# Clear the current image state at the end of the code
plt.clf()