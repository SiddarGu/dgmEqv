import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = np.array(["Student Achievement (Score)", "Curriculum Quality (Score)", "Staff Qualification (Score)",
                       "Learning Environment (Score)", "Resource Availability (Score)"])
line_labels = np.array(["Public School", "Private School", "Home Schooling", "Online Learning", "Adult Education"])
data = np.array([[85, 90, 78, 88, 80],
                 [90, 88, 75, 80, 85],
                 [88, 90, 80, 85, 82],
                 [80, 85, 75, 77, 85],
                 [80, 85, 70, 80, 75]])

# Append the first numerical element of each row to the end for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set up the figure and axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Set angles for evenly space the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row as a separate data line with different colors
colors = ['r', 'g', 'b', 'm', 'y']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, labels, loc='best')

# Add title
plt.title("Comparative Analysis of Various Education Models")

# Adjust image layout and save the image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/167_202312310100.png")

# Clear the current image state
plt.clf()