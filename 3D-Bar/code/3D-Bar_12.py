
import numpy as np
import matplotlib.pyplot as plt

# transform data into three variables
y_values = ["Freight Volume (Million Tonnes)", "Passenger Volume (Millions)", "Average Cost per Mile($)"]
data = np.array([[2, 1.2, 0.3], [1.5, 0.8, 0.4], [4, 1.5, 1.5], [2.2, 0.6, 0.2]])
x_values = ["Road", "Rail", "Air", "Sea"]
 
# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.6, data[:,i], shade=True, color='b', alpha=0.8)
 
# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
 
# rotate the X-axis labels for better readability
ax.set_xticklabels(x_values, rotation=30)
 
# Drawing techniques such as background grids can be used
ax.grid(linestyle='-', linewidth='0.5', color='grey')
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=30)
# Set the title of the figure
ax.set_title('Transportation and Logistics Cost Analysis by Mode of Transport')
 
# Automatically resize the image by tight_layout() before savefig
plt.tight_layout()
 
# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/11_202312270030.png')
 
# Clear the current image state at the end of the code
plt.cla()