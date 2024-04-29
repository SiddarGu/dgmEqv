
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ['Electricity Usage (Billion kWh)', 'Natural Gas Consumption (Billion m3)', 'Oil Production (Million bbl/day)']
data = np.array([[5, 50, 30], [10, 51, 35], [20, 52, 40], [30, 53, 45], [40, 55, 50]])
x_values = ['2019', '2020', '2021', '2022', '2023']

# Plot the data with the type of 3D bar chart. use a 3D projection for the subplot. Create figure before plotting.
fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Iterate over y_values to plot each column of data, i.e., data[:, i]
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    # Use ax.bar3d to draw a set of bars, in which ensure that each group of bars is correctly aligned on x-axis. 
    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization.
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], color=['red','orange','yellow'][i], alpha=0.9)

# Rotate the X-axis labels for better readability.
ax.view_init(elev=30, azim=-90)

# Set xticks and yticks to align the label position with data position.
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# Use ax.set_xticklabels(x_values) to label x-axis. Use ax.set_yticklabels(y_values) to label y-axis.
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)

# Y-axis does not need title.
ax.set_ylabel('')

# Drawing techniques such as background grids can be used.
ax.grid(False)

# The title of the figure should be  Energy and Utilities - A Comprehensive Overview.
ax.set_title('Energy and Utilities - A Comprehensive Overview')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/42_202312251044.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/42_202312251044.png')

# Clear the current image state at the end of the code.
plt.clf()