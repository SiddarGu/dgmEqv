import matplotlib.pyplot as plt
import numpy as np

# data
data_labels = ["Finished Goods Quality", "Production Speed", "Machine Efficiency", "Workforce Productivity", "Cost Management"]
data = np.array([[85,75,75,80,70],[90,75,80,85,65],[80,80,75,90,60],[85,85,90,95,70]])
line_labels = ["Factory A", "Factory B", "Factory C", "Factory D"]

# Create figure and add subplot.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points.
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array.
for i, row_data in enumerate(data):
    # Append first element of the row to its end.
    row_data = np.append(row_data, row_data[0])

    # Generate angle-like vector.
    radius = np.full_like(angles, (i+1) * np.max(data) / len(data))

    # Plot data lines.
    ax.plot(angles, row_data, label=line_labels[i])

    # Draw straight lines as gridlines.
    ax.plot(angles, radius, color='gray', linestyle='--')

# Set x-axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Adjust the radial limits to accommodate the data.
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-75)

# Plot legend.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove the circular gridlines and background.
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title
plt.title('Manufacturing and Production Performance Analysis')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/110_2023122292141.png')

# Clear figure
plt.clf()
