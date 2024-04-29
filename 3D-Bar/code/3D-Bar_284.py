

import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ['Online Sales (Units)', 'Retail Store Sales (Units)', 'Total Sales (Units)', 'Average Price ($)']
data = np.array([[300, 700, 1000, 50], [400, 600, 1000, 60], [450, 550, 1000, 70], [500, 500, 1000, 80]])
x_values = ['North', 'South', 'East', 'West']

# Plot the data with the type of 3D bar chart.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(0, len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
    bottom = np.zeros(len(x_values))
    width = 0.8
    depth = 0.5
    top = data[:,i]
    ax.bar3d(xs, ys, bottom, width, depth, top, shade=True)

# Set title and labels
ax.set_title('Retail & E-Commerce Analysis by Region')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Rotate the X-axis labels for better readability
plt.xticks(rotation=45)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/47_202312251044.png')
# Clear the current image state
plt.clf()