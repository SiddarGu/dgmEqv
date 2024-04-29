
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ['Fruit Production (Million Tonnes)', 'Vegetable Production (Million Tonnes)', 'Livestock Production (Million Tonnes)', 'Grain Production (Million Tonnes)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[20, 30, 40, 50], [18, 27, 37, 47], [25, 35, 42, 52], [22, 32, 40, 50], [27, 38, 45, 55]])

#create figure before plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

#iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    # Plot the data with the type of 3D bar chart
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.2, 0.2, data[:,i], shade=True, color='b', alpha=0.7)

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Food Production Trends - 2019 to 2023')
ax.set_xlabel('Year')
#rotate the X-axis labels for better readability
plt.xticks(rotation=20)
# Drawing techniques such as background grids can be used
ax.grid(True)
# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/1_202312251044.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/1_202312251044.png')
# Clear the current image state at the end of the code
plt.clf()