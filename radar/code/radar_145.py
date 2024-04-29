import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data = np.array([[80, 85, 75, 70, 80], 
                [75, 80, 70, 80, 75], 
                [85, 90, 80, 75, 85], 
                [75, 70, 65, 80, 75], 
                [80, 85, 70, 75, 70]])

data_labels = ['Residential', 'Apartments', 'Industrial', 'Commercial', 'Retail']
line_labels = ['New York', 'Los Angeles', 'San Francisco', 'Chicago', 'Boston']

# Add the first element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and polar subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, polar=True)

# Set evenly spaced angles for the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row as a separate line with different colors
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Real Estate and Housing Market Analysis by City')

# Add background grids
ax.grid(True)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/121_202312302350.png')

# Clear the plot
plt.clf()