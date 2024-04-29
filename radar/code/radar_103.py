import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = np.array(["Paris", "London", "New York", "Tokyo", "Barcelona"])
line_labels = np.array(["Tourist Attraction (Score)", "Accommodation Quality (Score)", "Local Cuisine (Score)", "Safety (Score)", "Customer Service (Score)"])
data = np.array([[90, 85, 80, 95, 88], [85, 80, 95, 90, 85], [80, 85, 90, 75, 90], [95, 90, 85, 100, 80], [90, 95, 85, 90, 85]])

# Create figure and subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the radar chart for each row in data
for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker="o", label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Create legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper left")

# Set title
plt.title("Global Tourism and Hospitality Analysis")

# Adjust layout and save image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/147_202312302350.png")

# Clear current image state
plt.clf()