import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Whole Foods", "Starbucks", "KFC", "Chipotle", "McDonalds"]
line_labels = ["Quality Rating (/10)", "Price ($)", "Variety (/10)", "Service (/10)", "Ambience (/10)"]
data = np.array([[8, 7, 7, 8, 7],
                 [10, 5, 8, 9, 6],
                 [9, 10, 7, 8, 8],
                 [8, 9, 7, 8, 8],
                 [9, 8, 7, 8, 7]])

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row as a separate data line with different colors
colors = ['r', 'g', 'b', 'y', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
plt.title("Food and Beverage Industry - Product Evaluation")

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/155_202312310100.png')

# Clear image state
plt.clf()