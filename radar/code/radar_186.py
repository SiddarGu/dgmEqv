import matplotlib.pyplot as plt
import numpy as np

# Given data
data = "Energy Source,Solar,Hydro,Wind,Nuclear,Gas/n Efficiency,75,82,68,92,85/n Sustainability,90,85,80,95,60/n Cost,85,80,75,70,65/n Maintenance,70,75,80,85,90/n Safety,95,90,85,80,75"
data = data.replace("/n", "\n").split("\n")

# Separate labels from data
data_labels, full_data = data[0].split(",")[1:], [list(map(int, row.split(",")[1:])) for row in data[1:]]
line_labels = [row.split(",")[0] for row in data[1:]]

# Create a circular plot
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(polar=True)

# Generate the angles for the plot
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each of the line data
for i, row in enumerate(full_data):
    values = np.array(row)
    # Append first value to the end
    values = np.append(values, values[0])
    # Plot each individual line
    ax.plot(angles, values, label=line_labels[i])
    # Generate and plot radius vectors
    radius = np.full_like(angles, (i+1) * np.amax(np.array(full_data)) / len(full_data))
    ax.plot(angles, radius, color='lightblue')
    

# Set the grid labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, max([max(row) for row in full_data]))
max_value = np.amax(np.array(full_data))
step_size = max_value / len(full_data)
ax.set_rgrids([step_size * i for i in range(1, len(full_data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(full_data) + 1)], angle=90)

# Generate legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.3, 1.1))

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set chart title
plt.title('Energy and Utilities Performance Analysis', size=20, color='black', y=1.1)

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/35_2023122292141.png")

# Clear the figure
plt.clf()
