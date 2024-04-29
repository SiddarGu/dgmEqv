import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [85, 80, 75, 70, 65],
    [90, 85, 80, 75, 70],
    [75, 80, 85, 90, 95],
    [80, 85, 90, 95, 100],
    [70, 65, 60, 55, 60]
])

data_labels = ['Criminal Law', 'Familial Law', 'Constitutional Law', 'Intellectual Property Law', 'Environmental Law']
line_labels = ['n/ Case Success Rate (%)', 'Lawyer Efficiency (Score)', 'Client Satisfaction (Score)', 'Legal Research Quality (Score)', 'Cost Management (Score)']

# Extend each row to create a close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row of data
colors = ['red', 'green', 'blue', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=1, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower right')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Set title
plt.title('Law and Legal Affairs Performance Analysis')

# Add background grids
ax.grid(True)

# Automatically resize the image to prevent content from being cut off
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/58_202312302350.png')

# Clear the current image state
plt.clf()