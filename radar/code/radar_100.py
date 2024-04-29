import numpy as np
import matplotlib.pyplot as plt

# Data
data_labels = ['Resort Hotel', 'Boutique Hotel', 'Backpacker Hostel', 'Luxury Cruise', 'Wellness Retreat']
line_labels = ['Guest Satisfaction (Score)', 'Cleanliness (Score)', 'Location (Score)', 'Value for Money (Score)', 'Staff Friendliness (Score)']
data = np.array([[88, 84, 78, 92, 90],
                 [90, 88, 70, 94, 92],
                 [95, 85, 80, 70, 65],
                 [80, 75, 85, 70, 90],
                 [90, 85, 80, 95, 92]])

# Concatenate data for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and set polar plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row of data
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits to accommodate maximum data value
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Tourism and Hospitality Ratings')

# Resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/74_202312302350.png')

# Clear the current image state
plt.clf()