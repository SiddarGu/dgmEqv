import matplotlib.pyplot as plt
import numpy as np

# Define Labels and Data
data_labels = ['Desktop', 'Mobile', 'Tablet']
line_labels = ['User Experience', 'Data Security', 'Website Speed', 'Content Quality', 'User Engagement']
data = np.array([[85, 75, 65], [90, 80, 70], [70, 80, 90], [80, 85, 90], [75, 85, 95]])

# Create Radar Chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(polar=True)
ax.set_title('Internet Platform Performance Analysis', size=20, color='black', y=1.1)

# Define Colormap and Data Lines
colors = ['b', 'g', 'r', 'c', 'm']
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Plot Data
for i in range(len(data)):
    values = np.concatenate((data[i], [data[i][0]]))  # Close the loop
    ax.plot(angles, values, 'o-', color=colors[i % len(colors)], label=line_labels[i])

    radius = np.full_like(angles, (i + 1) * np.amax(data) / len(data))
    ax.plot(angles, radius, '-', color=colors[i % len(colors)])

ax.set_ylim(0, np.amax(data)*1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.3, 1.1))

# Remove axis
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)

# Save figure and show
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/84_2023122292141.png')
plt.cla()
