
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Q1","Q2","Q3","Q4"]
line_labels = ["Sales (%)","Profits (%)","Investments (%)","Customer Satisfaction (%)","Market Share (%)"]
data = np.array([[70,75,80,85],[50,55,60,65],[60,65,70,75],[80,85,90,95],[65,70,75,80]])

# Create figure before plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)

# Iterate over each row in the data array, append the first numerical element of that row to the end of that row for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the data with the type of radar chart
# Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Plot the data lines
for row in range(len(line_labels)):
    ax.plot(angles, data[row], label=line_labels[row], linewidth=2)
    ax.fill(angles, data[row], alpha=0.25)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(0,100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend of data lines
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(0.9, 0.1))

#Drawing techniques such as background grids can be used
ax.grid(True)

# Set title
ax.set_title("Business Performance - 2023", va='bottom')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/32_202312262320.png")

# Clear the current image state
plt.clf()