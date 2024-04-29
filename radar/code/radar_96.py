import numpy as np
import matplotlib.pyplot as plt

# Transform the given data
data_labels = ['Visitor Satisfaction', 'Exhibition Variety', 'Educational Programs', 'Accessibility', 'Conservation Efforts']
line_labels = ['Museum of Modern Art', 'Smithsonian Institution', 'Metropolitan Museum of Art', 'Saatchi Gallery', 'Louvre Museum']
data = np.array([[85, 80, 95, 90, 98],
                 [90, 85, 88, 94, 97],
                 [87, 86, 83, 88, 96],
                 [80, 85, 90, 95, 93],
                 [90, 92, 93, 94, 96]])

# Create figure and plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)
ax.set_title('Arts and Culture - Museum Performance Analysis')

# Add close-loop data for plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data lines
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1, linestyle='solid', color=colors[i], label=line_labels[i])

# Set thetagrids
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Add grid lines
ax.grid(True)

# Automatically resize image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/57_202312302350.png')

# Clear the current image state
plt.clf()
