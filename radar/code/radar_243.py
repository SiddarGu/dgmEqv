import matplotlib.pyplot as plt
import numpy as np

# Raw data
raw_data = [
    ["Subject", "Term 1", "Term 2", "Term 3", "Term 4"],
    ["Math Scores", 80, 85, 90, 95],
    ["Science Scores", 75, 80, 85, 90],
    ["Reading Scores", 85, 90, 95, 100],
    ["Art Scores", 70, 75, 80, 85],
    ["Physical Education Scores", 65, 70, 75, 80],
]

# Data transformation
data_labels = raw_data[0][1:]
data = [row[1:] for row in raw_data[1:]]
line_labels = [row[0] for row in raw_data[1:]]

# Create figure and polar axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Compute angles for radial gridlines
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data and gridlines
for idx, row in enumerate(data):
    row.append(row[0])  # Close loop
    ax.plot(angles, row, label=line_labels[idx])
    radius = np.full_like(angles, ((idx+1) * max([max(row) for row in data]) / len(data)))
    ax.plot(angles, radius, color='gray', linestyle='--')

# Set axis labels 
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)  

# Adjust radial limits and remove circular gridlines and background
ax.set_rlim(0, max([max(row) for row in data]))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title('Term-based Subject Performance in Education')

# Auto resize
fig.tight_layout()

# Save and clear figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/117_2023122292141.png')
plt.clf()
