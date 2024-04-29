
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values.
y_values = ["Computer Science Research Paper Output (Millions)", "Engineering Research Paper Output (Millions)", "Mathematics Research Paper Output (Millions)"]
data = np.array([[2.2,2.6,1.4], [2.5,3.1,1.6], [2.9,3.5,1.9], [3.2,3.9,2.2], [3.4,4.2,2.5]])
x_values = ["2015","2016","2017","2018","2019"]

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    X = np.arange(len(x_values))
    Y = np.array([i]*len(x_values))
    Z = data[:, i]

    # Set the dimensions of the bars
    dx = 0.5
    dy = 0.5
    dz = data[:, i]

    # Set the color of each bar
    colors = ['b', 'g', 'r', 'c', 'm']

    # Plot the bar
    ax.bar3d(X, Y, np.zeros(len(Z)), dx, dy, dz, color=colors[i])

# Set the labels for x-axis, y-axis and z-axis
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, rotation=15, ha='right')
ax.set_zlabel('Output (Millions)')
ax.view_init(15, -150)
# Set the title of the figure
ax.set_title('Science and Engineering Research Output Trends - 2015 to 2019')

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/49_202312251044.png')

# Clear the current image
plt.clf()