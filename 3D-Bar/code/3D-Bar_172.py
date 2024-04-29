
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values. 
# y_values represents the metric list of each column except the first column. 
# x_values represents the category list of each row except the first row. 
# Data represent the numerical ndarray in the data, where each row corresponds to a category and each column corresponds to a metric.
y_values = ["Number of Donations", "Amount Raised ($)", "Total Donors"]
x_values = ["Educational", "Medical", "Environmental", "Social Services", "Arts"]
data = np.array([[1000, 2500, 1500], [800, 2000, 1200], [500, 1000, 900], [600, 1500, 1100], [400, 500, 700]])

# Create figure and set size
fig = plt.figure(figsize=(10, 6))

# Plot the data with the type of 3D bar chart. 
# use a 3D projection for the subplot. 
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data, i.e., data[:, i]. 
# For the plotting of each column in data, use np.arange(len(x_labels)) 
# and [i]*len(x_labels) to represent the X, Y coordinates for each group of data
# to avoid overlapping of different data groups, 
# and use ax.bar3d to draw a set of bars, in which ensure that each group of bars is correctly aligned on x-axis. 
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    
    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization. 
    dx = 0.5
    dy = 0.5
    dz = data[:,i]
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#00ceaa', alpha=0.9)
    
# Rotate the X-axis labels for better readability. Y-axis does not need title.
ax.set_xticks(xpos)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)

# Drawing techniques such as background grids can be used.
ax.set_xlabel('Type of Organization')
ax.set_ylabel('Metrics')
ax.set_zlabel('Value')
ax.set_title('Impact of Charitable Donations by Type of Organization')
ax.grid(b=True, which='major', color='#666666', linestyle='-')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/29_202312251044.png.
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/29_202312251044.png")

# Clear the current image state at the end of the code.
plt.clf()