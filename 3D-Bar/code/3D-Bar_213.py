
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ["Revenue from Sports ($ Billion)", "Revenue from Entertainment ($ Billion)", "Total Revenue ($ Billion)"]
data = np.array([[200, 250, 450], [215, 270, 485], [235, 290, 525], [250, 310, 560], [275, 335, 610]])
x_values = ["2019", "2020", "2021", "2022", "2023"]

# Plot the data with the type of 3D bar chart.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data.
for i in range(len(y_values)):
    x = np.arange(len(x_values))
    y = [i] * len(x_values)
    ax.bar3d(x, y, np.zeros(len(x_values)), 1, 1, data[:, i], alpha=0.5, color=['pink', 'yellow', 'red', 'blue', 'green'])

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization.
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values, ha='left')

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be Sports and Entertainment Industry Performance - 2019 to 2023.
plt.title("Sports and Entertainment Industry Performance - 2019 to 2023")

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/24_202312270030.png")

# Clear the current image state at the end of the code.
plt.close()