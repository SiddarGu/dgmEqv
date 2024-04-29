
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
y_values = ["Passenger Volume (Millions)", "Freight Volume (Millions)", "Accidents (No. of Incidences)"]
data = np.array([[220, 750, 625], [120, 400, 550], [700, 1000, 500], [220, 260, 150]])
x_values = ["Air", "Rail", "Road", "Water"]

# Create figure and 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    X = np.arange(len(x_values))
    Y = np.ones(len(x_values)) * i
    # Calculate the X, Y coordinates for each group of data to avoid overlapping of different data groups
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:,i]
    # Use ax.bar3d to draw a set of bars
    # Set the dimensions of the bars (width, depth, colors, alpha, etc) differently on x-dimension or y-dimension to ensure they are distinct and non-overlapping
    ax.bar3d(X, Y, np.zeros(len(x_values)), dx, dy, dz, color=plt.cm.Paired(i/len(y_values)), alpha=0.5)

# Rotate the X-axis labels for better readability
plt.xticks(np.arange(len(x_values)), x_values, rotation=45)
# Y-axis does not need title
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used
ax.grid(False)

# Set the title of the figure
plt.title("Transportation and Logistics Performance - 2019")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/18.png')

# Clear the current image state at the end of the code
plt.clf()