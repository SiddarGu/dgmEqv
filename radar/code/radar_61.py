import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_str = "Transport Mode,Trucks,Ships,Planes,Trains,River Barges/n Fuel Efficiency (MPG),8,12,40,500,10/n Speed (MPH),60,30,600,70,10/n Capacity (Tons),20,100,50,120,15/n Reliability (%),92,95,98,95,90/n Cost Efficiency ($/Ton),100,50,80,60,75"
data_list = [row.split(",") for row in data_str.split("/n ")]
data_labels = data_list[0][1:]
line_labels = [data[0] for data in data_list[1:]]
data = np.array([[float(num) for num in data[1:]] for data in data_list[1:]])

# Create figure
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to close-loop the plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the data lines with different colors
for i, row in enumerate(data):
    ax.plot(angles, row, marker='o', label=line_labels[i])

# Plot the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Add background grids
ax.grid(True)

# Set the title of the figure
plt.title("Comparison of Different Modes of Transport in Logistics")

# Automatically resize the image to fit the content
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/56_202312302350.png')

# Clear the current image state
plt.clf()