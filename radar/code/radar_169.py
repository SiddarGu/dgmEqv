import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Modern Art Museum', 'History Museum', 'Music Festival', 'Theatre', 'Book Fair']
line_labels = ['Visitor Satisfaction (Score)', 'Art Quality (Score)', 'Event Organization (Score)', 'Facility Quality (Score)', 'Cultural Significance (Score)']
data = np.array([[90, 88, 75, 80, 78], [95, 92, 77, 83, 85], [79, 74, 83, 88, 86], [82, 85, 70, 88, 79], [93, 97, 80, 84, 89]])

# Add subplot to the figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the data lines with different colors
colors = ['blue', 'green', 'red', 'orange', 'purple']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

# Set title of the figure
ax.set_title('Arts and Culture Institutions Performance Analysis')

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/174_202312310100.png')

# Clear the current image state
plt.clf()