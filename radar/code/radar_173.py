import matplotlib.pyplot as plt
import numpy as np

# Transforming the given data into variables
data_labels = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Reddit']
line_labels = ['User Engagement (Hours/Week)', 'Ad Reach (Million)', 'Mobile App Usage (%)', 'Data Security (Score)', 'Innovation Capacity (Score)']
data = np.array([[20, 25, 30, 35, 30], [80, 70, 90, 75, 65], [70, 80, 85, 65, 50],[85, 80, 70, 80, 75],[90, 85, 80, 90, 75]])

# Creating the figure and polar plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Adding the data line for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Setting the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting the data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Adding the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjusting the radial limits based on the maximum data value
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Adding the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Setting the title
plt.title('Digital Platform Performance Analysis')

# Adjusting the layout and saving the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/85_202312302350.png')

# Clearing the plot
plt.clf()