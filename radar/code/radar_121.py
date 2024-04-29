import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['History', 'Literature', 'Philosophy', 'Anthropology', 'Psychology']
line_labels = ['Research Quality (Score)', 'Teaching Quality (Score)', 'Student Satisfaction (Score)', 'Faculty Expertise (Score)', 'Alumni Success (Score)']
data = np.array([[85, 80, 75, 70, 65],
                 [90, 85, 80, 75, 70],
                 [85, 90, 95, 90, 85],
                 [80, 85, 90, 95, 95],
                 [75, 80, 85, 90, 95]])

# Create figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row of data
for i, row in enumerate(data):
    row = np.concatenate((row, [row[0]]))
    ax.plot(angles, row, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
ax.set_title('Academic Field Performance in Social Sciences and Humanities')

# Set grid
ax.grid(True)

# Auto resizing and savefig
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/198_202312310100.png')

# Clear current image state
plt.clf()