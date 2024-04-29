import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Unemployment Rate (%)', 'Crime Rate (%)', 'Education Investment (% GDP)', 'Healthcare Investment (% GDP)', 'Infrastructure Investment (% GDP)']
line_labels = ['Defense Policy', 'Social Policy', 'Economic Policy', 'Foreign Policy', 'Environmental Policy']

data = np.array([[5, 30, 4, 6, 10],
                 [6, 25, 5, 7, 9],
                 [4, 20, 6, 8, 11],
                 [6, 15, 7, 9, 8],
                 [5, 10, 8, 10, 12]])

# Close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data lines
colors = ['b', 'g', 'r', 'c', 'm']
for i in range(len(data)):
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i], color=colors[i])

# Axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Title
plt.title('Government Policy Impact on Public Sectors')

# Background grid
ax.yaxis.grid(True)

# Resize and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/54_202312302350.png')

# Clear current figure
plt.clf()