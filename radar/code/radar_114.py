import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['Math', 'Biology', 'Chemistry', 'Physics', 'English', 'History']
line_labels = ['Midterm Score (%)', 'Final Score (%)', 'Classroom Participation (%)', 'Homework Completion (%)', 'Extra Curriculum Activity Participation (%)']
data = np.array([[85, 80, 75, 70, 65, 90],
                 [90, 85, 80, 75, 70, 95],
                 [75, 80, 85, 90, 95, 80],
                 [80, 85, 90, 88, 82, 80],
                 [70, 75, 80, 85, 90, 65]])

# Add the first numerical element of each row to the end of that row
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array and plot data lines
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(data.shape[0]):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim([0, np.max(data)])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Student Performance in Different Subjects')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/118_202312302350.png')

# Clear current image state
plt.clf()