import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into variables
data_labels = ['Organic Food', 'Processed Food', 'Soft Drinks', 'Wine', 'Coffee', 'Fast Food']
line_labels = ['Quality Score', 'Popularity Score', 'Supply Chain Efficiency (%)', 'Environmental Impact Score', 'Profit Margin (%)']

data = np.array([[80, 75, 70, 85, 90, 65],
                 [85, 80, 75, 70, 65, 95],
                 [90, 85, 80, 75, 70, 60],
                 [70, 65, 60, 75, 80, 55],
                 [75, 80, 85, 70, 65, 60]])

# Create figure and plot radar chart
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each data line with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i % len(colors)], label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.15, 1))

# Set title
plt.title('Food and Beverage Industry Performance Review')

# Add background grid
ax.grid(True)

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/83_202312302350.png')

# Clear current image state
plt.clf()