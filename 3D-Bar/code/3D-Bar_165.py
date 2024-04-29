
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: y_values, data, x_values.
y_values = ["Freight Volume (Million Tonnes)", "Passenger Volume (Million)", "Average Price"]
data = np.array([[4.2, 2.3, 1.2, 6.0],
                 [24.5, 12.9, 5.7, 2.3],
                 [10.3, 8.5, 15.2, 17.6]])
x_values = ["Road", "Rail", "Air", "Sea"]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.2, 0.5, data[i],
             color=['b', 'g', 'r', 'c'], alpha=0.5, shade=True)

# Set the dimensions of the bars (width, depth, colors, alpha, etc)
ax.set_xlabel('Mode')
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticklabels(y_values)
ax.set_xticklabels(x_values, rotation=45)

# Title
plt.title('Analysis of Transportation and Logistics Performance by Mode')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/26_202312251036.png')

# Clear the current image state
plt.clf()