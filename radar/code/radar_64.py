import numpy as np
import matplotlib.pyplot as plt

# Transform data into variables
data_labels = ['Q1', 'Q2', 'Q3', 'Q4/Q1']
line_labels = ['Policy Approval Rating (%)', 'Government Transparency Score (out of 10)',
               'Public Service Access (%)', 'Socioeconomic Development Index (out of 100)',
               'Public Trust in Government (%)']
data = np.array([[65, 70, 75, 80], [7, 8, 8.5, 9], [70, 75, 80, 85], [80, 82, 84, 86], [60, 65, 70, 75]])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first element to each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines
for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o')

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
plt.title('Government and Public Policy Performance Metrics')

# Add background grids
ax.grid(True)

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/200_202312310100.png')

# Clear current image
plt.close()
