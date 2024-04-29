
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values. 
y_values = ['Number of Museums', 'Number of Art Galleries', 'Number of Theatres', 'Number of Concert Halls']
data = np.array([[500, 750, 200, 150],
                 [400, 600, 150, 100],
                 [350, 500, 100, 75],
                 [450, 650, 125, 90]])
x_values = ['USA', 'Canada', 'UK', 'Germany']

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data, i.e., data[:, i]. 
for i in range(len(y_values)):
    # For the plotting of each column in data, use np.arange(len(x_labels)) and [i]*len(x_labels) to represent the X, Y coordinates for each group of data to avoid overlapping of different data groups, and use ax.bar3d to draw a set of bars, in which ensure that each group of bars is correctly aligned on x-axis. 
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    dx = 0.4
    dy = 0.4
    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization.
    dz = data[:, i]
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#00ceaa')

# Rotate the X-axis labels for better readability.
ax.set_xticks(xpos)
ax.set_xticklabels(x_values, rotation=30)

# Y-axis does not need title.
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# The title of the figure should be Arts and Culture Facilities Around the World.
ax.set_title('Arts and Culture Facilities Around the World')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/3_202312251000.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/3_202312251000.png')

# Clear the current image state at the end of the code.
plt.clf()