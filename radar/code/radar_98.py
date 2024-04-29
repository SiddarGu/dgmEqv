import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
line_labels = ['Efficiency', 'Production Volume', 'Operating Costs', 'Profit Margin', 'Quality Score']
data = np.array([[80, 85, 90, 85, 80], [100, 105, 110, 115, 120], [60, 55, 50, 55, 60], [20, 25, 30, 35, 40], [90, 85, 80, 85, 90]])

# Add an extra column to data for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create a figure and plot the data as a radar chart
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set evenly spaced angles for the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array and plot the lines
for i in range(len(line_labels)):
    ax.plot(angles, data[i, :], label=line_labels[i])

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='best')

# Add background grids
ax.grid(True)

# Set the title of the figure
plt.title('Performance comparison among different Products in Manufacturing')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/194_202312310100.png')

# Clear the current image state
plt.clf()