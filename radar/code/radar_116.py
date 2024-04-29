import numpy as np
import matplotlib.pyplot as plt

data = np.array([[85, 90, 80, 85, 90],
                [78, 82, 79, 76, 83],
                [95, 92, 90, 89, 92],
                [97, 95, 93, 91, 98],
                [99, 97, 98, 96, 99]])

data_labels = ['Factory A', 'Factory B', 'Factory C', 'Factory D', 'Factory E']
line_labels = ['Process', 'Production Capacity (%)', 'Production Efficiency (%)', 'Quality Control (%)', 'Supply Chain Management (%)', 'Safety Measures (%)']

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Plot data lines
for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1, label=line_labels[i])

# Adjust radial limits
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='lower right')

# Set title
plt.title('Manufacturing and Production Performance Comparison')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/104_202312302350.png')

# Clear the current image state
plt.clf()