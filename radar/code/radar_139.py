
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Popularity (Score)', 'Quality (Score)', 'Engagement (Score)', 'Diversity (Score)', 'Global Impact (Score)']
line_labels = ['Painting','Dance','Theatre','Music','Literature']
data = np.array([[90,85,80,75,70], [95,90,85,80,75], [85,80,75,70,65], [80,75,70,65,60], [70,75,80,85,90]])

# Close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Iterate over each row in the data array
for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i], linewidth=2, linestyle='solid')

# Adjust the radial limits
ax.set_ylim(0, np.max(data))

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95))

# Set title
ax.set_title('Arts and Culture Impact - 2021', fontsize=18)

# Draw background grids
ax.grid(True)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/24_202312262320.png')

# Clear the current image state
plt.clf()