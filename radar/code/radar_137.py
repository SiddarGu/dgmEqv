import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ["Beach Resort", "Mountain Cabin", "Museum Tour", "Cruise Trip", "Spa Retreat"]
line_labels = ["Customer Satisfaction (Score)", "Location Rating (Score)", "Number of Attractions (Count)", "Price (Score)", "Food Quality (Score)"]
data = np.array([[80, 85, 90, 80, 90],
                 [90, 85, 75, 80, 95],
                 [7, 6, 10, 8, 5],
                 [75, 70, 65, 80, 90],
                 [80, 85, 90, 95, 90]])

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first numerical element to the end of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
max_value = np.amax(data)
ax.set_ylim(0, max_value)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set title
plt.title("Tourism and Hospitality Performance Analysis")

# Save and clear current image state
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/64_202312302350.png")
plt.clf()