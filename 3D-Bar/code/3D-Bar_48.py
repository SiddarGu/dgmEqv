

import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values
# y_values represents the metric list of each column except the first column
# x_values represents the category list of each row except the first row
# Data represent the numerical ndarray in the data, where each row corresponds to a category and each column corresponds to a metric
y_values = ["Number of Employees", "Average Salary ($)", "Total Cost of Benefits ($)"]
data = np.array([[500, 520, 500], [550, 532, 520], [600, 550, 560], [650, 580, 600], [700, 600, 650]])
x_values = ["2019", "2020", "2021", "2022", "2023"]

# Plot the data with the type of 3D bar chart. use a 3D projection for the subplot. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data, i.e., data[:, i]. 
# For the plotting of each column in data, use np.arange(len(x_labels)) and [i]*len(x_labels) to represent the X, Y coordinates 
# for each group of data to avoid overlapping of different data groups, and use ax.bar3d to draw a set of bars, 
# in which ensure that each group of bars is correctly aligned on x-axis.
for i in range(len(y_values)):
    x_positions = np.arange(len(x_values))
    y_positions = [i]*len(x_values)
    ax.bar3d(x_positions, y_positions, np.zeros(len(x_values)), 0.8, 0.8, data[:,i], shade=True)

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization. Rotate the X-axis labels for better readability. Y-axis does not need title.
ax.set_xlabel('Year')
ax.set_ylabel('Metrics')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# Drawing techniques such as background grids can be used.
ax.grid(False)

# Use ax.set_xticks and ax.set_yticks to align the label position with data position. 
# Use ax.set_xticklabels(x_values) to label x-axis. 
# Use ax.set_yticklabels(y_values) to label y-axis.
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values)

# The title of the figure should be  Human Resources and Employee Management Trends - 2019 to 2023.
ax.set_title("Human Resources and Employee Management Trends - 2019 to 2023")

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/22_202312251044.png.
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/22_202312251044.png")

# Clear the current image state at the end of the code.
plt.clf()