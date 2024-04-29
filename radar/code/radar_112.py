import numpy as np
import matplotlib.pyplot as plt

# Transform data
data = np.array([[75, 80, 85, 90],
                 [65, 70, 75, 80],
                 [55, 60, 65, 70],
                 [50, 55, 60, 65],
                 [70, 75, 80, 85]])
data_labels = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
line_labels = ['Overall Sales', 'Beverage Sales', 'Food Sales', 'Production Costs', 'Market Share']

# Create figure and subplot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# Space the axes evenly
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first element of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i, line_data in enumerate(data):
    ax.plot(angles, line_data, color=colors[i], marker='o')

# Set axis labels
ax.set_thetagrids(np.degrees(angles[:-1]), data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Add title
plt.suptitle("Food and Beverage Industry Performance Overview")

# Add gridlines
ax.grid(True)

# Save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/202_202312310100.png")

# Clear current image state
plt.clf()
