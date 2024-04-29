import numpy as np
import matplotlib.pyplot as plt

# Transform the data into variables
data_labels = ["Detection Range (km)", "Resolution (m)", "Penetration Depth (m)", "Radar Cross Section (m^2)", "Signal-to-Noise Ratio (dB)"]
line_labels = ["X-Band Radar", "L-Band Radar", "S-Band Radar", "C-Band Radar", "Ku-Band Radar"]
data = np.array([[8.5, 9.0, 9.5, 9.0, 8.5],
                 [1.5, 2, 1.5, 1, 1],
                 [2.7, 3, 3.5, 4, 2.5],
                 [0.1, 0.2, 0.25, 0.15, 0.2],
                 [2.0, 2.2, 2.4, 2.6, 2.8]])

# Create figure and subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Plot data lines
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i in range(len(line_labels)):
    line_data = np.concatenate((data[i], [data[i][0]]))
    ax.plot(np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True), line_data, color=colors[i], label=line_labels[i])

# Set axis labels
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set the title
plt.title("Comparing Specifics of Different Radar Bands")

# Adjust the layout and save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/136_202312302350.png')

# Clear the current image state
plt.clf()