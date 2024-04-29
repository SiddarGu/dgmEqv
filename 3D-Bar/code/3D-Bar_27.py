
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ['R&D Expenditure (Billion USD)', 'High-Tech Exports (Billion USD)', 'Patents Issued (Number of Patents)'] 
data = np.array([[365, 1120, 2200], [375, 1150, 2500], [395, 1200, 1800], [405, 1250, 2100], [415, 1280, 1400]]) 
x_values = ['2019', '2020', '2021', '2022', '2023']

# Create figure with 3D projection
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values) - 1, -1, -1):
    X = np.arange(len(x_values))
    Y = [i] * len(x_values)
    # Set the dimensions of the bars (width, depth, colors, alpha, etc)
    ax.bar3d(X, Y, np.zeros(len(x_values)), 0.6, 0.6, data[:, i], alpha = 0.6, color=np.random.rand(3,))

# Set the label of x-axis
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left', rotation=-15)

# Set the title of the figure
ax.set_title('Science and Engineering - R&D, High-Tech Exports and Patents Analysis')

# Resize the image by tight_layout() and save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/2_202312251000.png')

# Clear the current image state
plt.cla()