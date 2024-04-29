import numpy as np
import matplotlib.pyplot as plt

# Parse the raw data
raw_data = 'Evaluation Aspect,Manager A,Manager B,Manager C,Manager D/n Leadership Skills,80,85,90,95/n Team Management,75,80,85,90/n Conflict Resolution,70,75,80,85/n Employee Development,85,90,95,100/n Performance Management,80,85,90,95'
raw_data = raw_data.replace("/n", "\n").split("\n")
data_labels = raw_data[0].split(",")[1:]
data = [list(map(int, line.split(",")[1:])) for line in raw_data[1:]]
line_labels = [line.split(",")[0] for line in raw_data[1:]]

# Set the angles for the axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create a figure and a radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Plot data and gridlines
for idx, line_data in enumerate(data):
    line_data.append(line_data[0])
    ax.plot(angles, line_data, label=line_labels[idx])
    ax.fill(angles, line_data, alpha=0.25)
    radius = np.full_like(angles, (idx + 1) * max([max(sublist) for sublist in data]) / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dashed')

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Adjust radial limits
ax.set_rlim(0, max([max(sublist) for sublist in data]))

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set the title
plt.title('Evaluation of Human Resources and Employee Management Skills')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/107_2023122292141.png')

# Clear the figure
plt.clf()
