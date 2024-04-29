
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values. 
y_values = ['Violent Crime (Cases)', 'Property Crime (Cases)', 'Fraud (Cases)']
data = np.array([[20000, 18000, 3000], 
                 [12000, 15000, 2000], 
                 [7000, 9000, 1000],
                 [14000, 16000, 2500]])
x_values = ['USA', 'Canada', 'UK', 'Australia']

# Plot the data with the type of 3D bar chart. 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i, y in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:,i], alpha=0.7, color=plt.cm.get_cmap('Spectral')(i/3))

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
ax.set_xlim3d(0, len(x_values))
ax.set_ylim3d(-1, len(y_values))
ax.set_zlim3d(0, max(data.flatten()))

# Rotate the X-axis labels for better readability
ax.view_init(azim=145)

# Y-axis does not need title
ax.set_yticks([])

# Set ax.set_xticks and ax.set_yticks to align the label position with data position
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used
ax.grid(True)

# The title of the figure
ax.set_title('Global Legal Affairs and Crime Statistics')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/10_202312251036.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/10_202312251036.png')

# Clear the current image state at the end of the code
plt.cla()