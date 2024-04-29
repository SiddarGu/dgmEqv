import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['January', 'February', 'March', 'April', 'May', 'June']
line_labels = ['Corn', 'Wheat', 'Barley', 'Rice', 'Soybeans']
data = np.array([[1000, 1500, 2000, 2500, 3000, 3500],
                [800, 1300, 1800, 2300, 2800, 3300],
                [900, 1400, 1900, 2400, 2900, 3400],
                [1100, 1600, 2100, 2600, 3100, 3600],
                [700, 1200, 1700, 2200, 2700, 3200]])

# Plot the data with radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Iterate over each row in the data array
colors = ['r', 'g', 'b', 'y', 'm']
data = np.concatenate((data, data[:, 0:1]), axis=1)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Agriculture and Food Production - First Half of 2023')

# Save and clear the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/188_202312310100.png')
plt.clf()