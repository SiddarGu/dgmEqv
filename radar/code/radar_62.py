import numpy as np
import matplotlib.pyplot as plt

# Transform the data
data_labels = ["Yield Q1", "Yield Q2", "Yield Q3", "Yield Q4"]
line_labels = ["Wheat", "Corn", "Rice", "Soybeans", "Cotton"]
data = np.array([[80, 85, 90, 95],
                 [75, 80, 85, 90],
                 [70, 75, 80, 85],
                 [65, 70, 75, 80],
                 [60, 65, 70, 75]])

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first column to each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], color=colors[i], label=line_label)

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim([0, data.max() + 10])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower right')

# Set title
plt.title('Agriculture Production: Crop Yield Analysis')

# Adjust layout
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/191_202312310100.png'
plt.savefig(save_path)

# Clear current state
plt.clf()
