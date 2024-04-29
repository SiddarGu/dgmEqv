import matplotlib.pyplot as plt
import numpy as np

# Data Parsing
raw_data = "Aspect,Museum A,Museum B,Gallery C,Theatre D\n Visitor Satisfaction,80,75,70,90\n Exhibition Quality,85,80,95,75\n Staff Efficiency,75,80,85,90\n Facilities,80,85,70,95\n Cultural Impact,75,80,85,90"
lines = raw_data.replace(" ", "").split('\n')

data_labels = lines[0].split(',')[1:]
data = [list(map(int, line.split(',')[1:])) for line in lines[1:]]
line_labels = [line.split(',')[0] for line in lines[1:]]

# Calculate evenly spaced angles for our data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create a figure
fig = plt.figure(figsize=(8, 8))

# Create a subplot with polar projection
ax = fig.add_subplot(111, polar=True)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Iterate over data to plot
for i, row in enumerate(data):
    row.append(row[0])  # repeat first element to close the polygon
    ax.plot(angles, row, label=line_labels[i], color=plt.cm.viridis(i / len(data)))
    ax.fill(angles, row, color=plt.cm.viridis(i / len(data)), alpha=0.25)
    gridline_radius = np.full_like(angles, (i + 1) * max(max(data)) / len(data))
    ax.plot(angles, gridline_radius, color="black", linestyle="--", linewidth=0.5)

# Set labels, grid, legend and title
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)
ax.grid(True)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, data_labels, loc="upper right", title="Institution")
ax.set_title("Arts and Culture Institutions Performance Analysis")
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/168_2023122292141.png')

# Clear the current figure
plt.clf()
