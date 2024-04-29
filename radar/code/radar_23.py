
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Donor Satisfaction', 'Volunteer Engagement', 'Resource Allocation', 'Outreach Impact', 'Fundraising Performance']
line_labels = ['Organization A', 'Organization B', 'Organization C', 'Organization D']
data = np.array([[90, 95, 80, 85], [85, 80, 75, 70], [80, 75, 70, 65], [75, 70, 65, 60], [95, 90, 85, 80]])

# Create figure before plotting.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points.
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array, append the first numerical element of that row to its end for close-loop plotting of data lines.
for i in range(len(line_labels)):
    data_row = np.append(data[:, i], data[0, i])
    ax.plot(angles, data_row, linewidth=2, label=line_labels[i])
    ax.fill(angles, data_row, alpha=0.25)
    
    # Generate a angle-like radius vector with constant values
    angle_r = np.full_like(angles, (i+1) * np.max(data) / len(line_labels))
    ax.plot(angles, angle_r, '--', alpha=0.25, color='black')

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels).
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)

# Adjust the radial limits to accommodate the maximum of data.
ax.set_ylim(0, np.max(data))

# Plot the data lines legend.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95), fontsize=14)

# Remove the circular gridlines and background.
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# The title of the figure should be  Nonprofit Performance Evaluatio.
plt.title('Nonprofit Performance Evaluatio', fontsize=18)

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/17.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/17.png')

# Clear the current image state at the end of the code.
plt.clf()