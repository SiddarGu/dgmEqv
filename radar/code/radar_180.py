import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data = np.array([[75, 65, 50, 70, 60, 45],
                 [65, 85, 55, 90, 70, 40],
                 [55, 60, 85, 70, 65, 55],
                 [85, 70, 60, 80, 70, 45],
                 [60, 70, 55, 65, 85, 50],
                 [50, 55, 70, 65, 60, 85]])

data_labels = ['Education Focus', 'Health Focus', 'Environment Focus', 'Disaster Relief Focus',
               'Human Rights Focus', 'Animal Welfare Focus']

line_labels = ['Children\'s Aid', 'Red Cross', 'Greenpeace', 'Save the Children',
               'Amnesty International', 'PETA']

# Create figure before plotting
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles for radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first numerical element of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot different data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm', 'y']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate maximum data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='center', bbox_to_anchor=(0.5, -0.1))

# Add background grids
ax.xaxis.grid(True)
ax.yaxis.grid(True)

# Set title
plt.title('Nonprofit Organizations Focus Areas')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/151_202312310100.png')

# Clear current image state
plt.clf()