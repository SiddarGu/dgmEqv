import numpy as np
import matplotlib.pyplot as plt

# Transform the given data
data_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
line_labels = ["Movie Ticket Sales ($)", "Sports Event Tickets ($)", "Arcade Revenue ($)", "Streaming Subscriptions ($)", "Concert Ticket Sales ($)"]
data = np.array([[1000, 1200, 1500, 1400, 1800, 2000, 2200],
                 [800, 1000, 1200, 1500, 1700, 2000, 2300],
                 [500, 600, 700, 800, 1000, 1200, 1400],
                 [2000, 2100, 2200, 2300, 2400, 2500, 2600],
                 [1500, 1800, 2200, 2500, 2800, 3100, 3400]])

# Create figure and polar subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines
colors = ['r', 'g', 'b', 'y', 'm']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])

# Adjust radial limits
ax.set_ylim(0, np.max(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Set axis label
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left')

# Set title
plt.title('Weekly Entertainment and Sports Revenue Analysis')

# Set background grids
ax.grid(True, linestyle='--')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/78_202312302350.png', dpi=300)

# Clear current image
plt.clf()