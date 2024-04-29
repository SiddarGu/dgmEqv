
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
y_values = ['Daily Active Users (Millions)', 'Average Time Spent (Minutes)', 'Ad Revenue ($ Millions)']
x_values = ['YouTube', 'Facebook', 'Instagram', 'Twitter']
data = np.array([[2.5, 20, 10], [4, 25, 15], [1.5, 15, 5], [1, 10, 2]])

# Create the figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.5, 0.5, data[:,i], shade=True, color=['c', 'm', 'y', 'g'])

# Set the dimensions of the bars (width, depth, colors, alpha, etc)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Drawing techniques such as background grids
ax.grid(True)

# Set the title of the figure
ax.set_title('Social Media and Web Performance Metrics')

# Automatically resize the image and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/4.png')

# Clear the current image state
plt.cla()