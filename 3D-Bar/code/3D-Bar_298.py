
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Solar Energy Production (GWh)', 'Wind Energy Production (GWh)', 'Hydropower Generation (GWh)', 'Nuclear Energy Production (GWh)']
data = np.array([[600,1000,2000,1200],[650,1100,2100,1300],[700,1200,2200,1400],[750,1300,2300,1500],[800,1400,2400,1600]])
x_values = ['2019','2020','2021','2022','2023']

# Create a figure before plotting
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    # Use ax.bar3d to draw a set of bars
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, alpha=0.2*(4 - i), color='b')

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization
x_range = np.arange(len(x_values))
ax.set_xticks(x_range)
ax.set_xticklabels(x_values, ha='right')
y_range = np.arange(len(y_values))
ax.set_yticks(y_range)
ax.set_yticklabels(y_values, ha='left')
ax.set_xlabel('Year')
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=-20)

# Drawing techniques such as background grids can be used
ax.grid(True)

# Set the title of the figure
plt.title('Energy Production Trends in the Utilities Sector - 2019 to 2023')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5.png')

# Clear the current image state at the end of the code
plt.cla()