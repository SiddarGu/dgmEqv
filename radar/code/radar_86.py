import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Electronics', 'Fashion', 'Sports', 'Books', 'Furniture', 'Jewelry']
line_labels = ['Website Traffic (in thousands)', 'Sales (in 1000 USD)', 'Return Rate (%)', 'Customer Satisfaction (%)', 'Market Share (%)']
data = np.array([[350, 300, 280, 260, 240, 220],
                 [70, 60, 50, 40, 35, 30],
                 [5, 7, 6, 4, 3, 2],
                 [90, 85, 80, 75, 70, 65],
                 [25, 20, 15, 12, 10, 8]])

# Create figure and subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end of that row
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row in the data array with different colors
colors = ['b', 'g', 'r', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i % len(colors)], linewidth=2, label=line_labels[i])

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust the radial limits
ax.set_ylim(0, np.max(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Create legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, bbox_to_anchor=(1.1, 1))

# Add background grid
ax.grid(True)

# Set title
plt.title('E-commerce Performance Overview for Various Product Categories')

# Adjust image size and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/124_202312302350.png')

# Clear current image state
plt.clf()