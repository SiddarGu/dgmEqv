import matplotlib.pyplot as plt
import numpy as np

# Transform data into variables
data_labels = ['Football', 'Basketball', 'Tennis', 'Bowling', 'Cinema Attendance (thousands)']
line_labels = ['Fan Engagement (Score)', 'Revenue (million $)', 'Player/Actor Satisfaction (Score)', 'Media Coverage (hrs/week)']
data = np.array([[90, 85, 95, 80, 70],
                [75, 80, 85, 90, 90],
                [80, 85, 70, 75, 95],
                [95, 85, 70, 65, 55]])

# Create figure and axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first numerical element of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Iterate over each row and plot data lines using different colors
for i, row in enumerate(data):
    ax.plot(angles, row, linewidth=2, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)

# Adjust radial limits to accommodate maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
ax.set_title('Sports and Entertainment Activity Overview')

# Add background grid
ax.grid(True)

# Auto resize image
fig.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/107_202312302350.png')
plt.close()