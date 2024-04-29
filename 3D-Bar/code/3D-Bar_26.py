

import numpy as np
import matplotlib.pyplot as plt

# transform the given data into three variables: y_values, data, x_values
data = np.array([[50, 50, 55, 80], 
                 [30, 30, 33, 60], 
                 [40, 40, 44, 70], 
                 [45, 45, 40, 75]])
y_values = ["Machinery Output (Units)", "Raw Material Usage (Kilograms)", "Finished Products (Units)", "Labour Cost ($000)"]
x_values = ["Plant A", "Plant B", "Plant C", "Plant D"]

# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d") 

# Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:, i], shade=True, alpha=0.5)

# Set the dimensions of the bars (width, depth, colors, alpha, etc)
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.tick_params(axis='x', rotation=45)
ax.set_xlabel("Plant")

# Drawing techniques such as background grids can be used
ax.grid(linestyle='--')

# Automatically resize the image by tight_layout() before savefig()
fig.tight_layout()

# The title of the figure should be  Manufacturing and Production Analysis by Plant
ax.set_title("Manufacturing and Production Analysis by Plant")

# Save the image
fig.savefig(r"/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/21_202312270030.png")

# Clear the current image state at the end of the code
plt.clf()