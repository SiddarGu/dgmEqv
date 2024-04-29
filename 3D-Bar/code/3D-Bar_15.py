
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values.
y_values = ["Renewable Energy Production (kWh)", "Non-Renewable Energy Production (kWh)", "CO2 Emissions (tones)"]
data = np.array([[4500,4800,5100,5400,5600],
                 [6000,6300,6700,7000,7400],
                 [7000,7300,7600,8000,8700]])
x_values = ["2015","2016","2017","2018","2019"]

# Plot the data with the type of 3D bar chart.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data, i.e., data[:, i].
for i in range(len(y_values)):
    # For the plotting of each column in data, use np.arange(len(x_labels)) and [i]*len(x_labels) to represent the X, Y coordinates for each group of data to avoid overlapping of different data groups, and use ax.bar3d to draw a set of bars, in which ensure that each group of bars is correctly aligned on x-axis.
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    dx = 0.5
    dy = 0.5
    dz = data[i,:]

    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping, providing clear visualization.
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#0fc2f2', alpha=0.7)

# Rotate the X-axis labels for better readability.
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)

# Y-axis does not need title.
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used.
ax.grid(b=True, which='major', axis='both', linestyle='--', color='gray', alpha=0.3)

# The title of the figure should be Global Energy Production and Emissions Trends - 2015 to 2019.
ax.set_title("Global Energy Production and Emissions Trends - 2015 to 2019")

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/11_202312251044.png.
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/11_202312251044.png')

# Clear the current image state at the end of the code.
plt.close()