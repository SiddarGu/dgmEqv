import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['Ocean Health', 'Forest Condition', 'Air Quality', 'Wildlife Diversity', 'Energy Consumption/n Pollution Level (Scale 1-10)']
line_labels = ['Biodiversity (Species Count)', 'Renewable Energy Usage (%)', 'Waste Management (Scale 1-10)', 'Conservation Efforts (Scale 1-10)']

data = np.array([[7, 15, 2, 3, np.nan],
                 [20, 25, 30, 35, 40],
                 [8, 7, 6, 5, 4],
                 [7, 8, 9, 10, 6]])

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set evenly spaced angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each row as a separate line with different colors
colors = ['blue', 'green', 'red', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.nanmax(data))

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.1))

# Add title
plt.title('Environment and Sustainability Assessment')

# Draw background grids
ax.yaxis.grid(True, color='gray', linestyle='dashed')
ax.xaxis.grid(True, color='gray', linestyle='dashed')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/117_202312302350.png')

# Clear the current image state
plt.clf()