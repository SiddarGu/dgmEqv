
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values
y_values = ['Donations Amount ($M)', 'Volunteer Hours (Million Hours)', 'Number of Organizations']
x_values = ['California', 'Texas', 'New York', 'Florida', 'Illinois']
data = np.array([[200, 500, 1000], [150, 400, 800], [175, 450, 900], [100, 300, 700], [125, 350, 600]])

# Plot the data with 3D bar chart
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.8, data[:, i], shade=True, color=['limegreen', 'mediumseagreen', 'olivedrab', 'darkkhaki', 'navajowhite'])

# Set the dimensions of the bars (width, depth, colors, alpha, etc)
ax.set_xlim3d(0, len(x_values))
ax.set_ylim3d(0, len(y_values))
ax.set_zlim3d(0, 1100)

# Set labels and title
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.set_title('Charitable Giving and Volunteerism by State', fontsize=16, y=1.05)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/13_202312251044.png')

# Clear the current image state
plt.clf()