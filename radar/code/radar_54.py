import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Air Quality Index', 'Carbon Emission Level', 'Water Quality Index', 'Deforestation Rate', 'Waste Recycling Ratio']
line_labels = ['Air', 'Water', 'Soil', 'Noise', 'Light']
data = np.array([[75, 70, 80, 65, 85],
                 [80, 75, 85, 70, 90],
                 [70, 65, 75, 60, 80],
                 [65, 60, 70, 55, 75],
                 [85, 80, 90, 75, 95]])

# Create figure and subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first element to the end of each row
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row of data
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

# Set labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
ax.set_title('Environment and Sustainability Evaluatio')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/166_202312310100.png')

# Clear current image state
plt.clf()
