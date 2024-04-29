
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
x_values = ['North', 'South', 'East', 'West']
y_values = ['Sales Volume (Units)', 'Average Price ($000)', 'Number of Listings']
data = np.array([[100, 160, 180],
                 [90, 140, 160],
                 [120, 150, 190],
                 [130, 170, 210]])

# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    bottom = 0
    width = 0.6
    depth = 0.6
    top = data[:, i]
    ax.bar3d(xs, ys, bottom, width, depth, top, shade=True, color='#00FF00')

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension
ax.set_xlabel('Region')
ax.set_ylabel('Metrics')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Set the title of the figure
ax.set_title('Real Estate Market Overview by Region')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/35_202312270030.png')

# Clear the current image state at the end of the code
plt.clf()