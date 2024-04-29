import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Education', 'Healthcare', 'Transportation', 'Environment', 'Defense', 'National Security']
line_labels = ['Public Satisfaction', 'Expenditure', 'Policy Impact', 'Staff Efficiency', 'Implementation Rate']
data = np.array([[75, 78, 81, 70, 82, 90],
                 [20, 25, 15, 18, 24, 28],
                 [70, 79, 75, 69, 82, 88],
                 [80, 82, 76, 81, 85, 90],
                 [75, 78, 81, 70, 82, 90]])

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first element of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines using different colors
colors = ['r', 'g', 'b', 'y', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, linestyle='solid', label=line_labels[i])

# Set axis label
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust radial limits
ax.set_ylim([0, np.max(data) + 10])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='best')

# Set title
ax.set_title('Analysis of Government Policy Sectors Performance')

# Add background grid
ax.xaxis.grid(True, color='gray', linestyle='dashed', alpha=0.5)
ax.yaxis.grid(True, color='gray', linestyle='dashed', alpha=0.5)

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/173_202312310100.png')

# Clear current image state
plt.clf()
