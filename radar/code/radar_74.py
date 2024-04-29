import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into variables
data_labels = ['Customer Satisfaction', 'Facility Quality', 'Service Quality', 'Location Rating', 'Value for Money']
line_labels = ['Beach Resort', 'Mountain Lodge', 'City Hotel', 'Spa Resort', 'Cruise']
data = np.array([[90, 85, 80, 75, 70],
                 [85, 90, 75, 95, 80],
                 [80, 85, 70, 95, 85],
                 [95, 90, 95, 75, 100],
                 [70, 75, 85, 80, 90]])

# Create figure and set polar=True
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Space axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plotting different data lines with different colors
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25, color=colors[i])

# Set axis label and adjust radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend and title
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')
plt.title('Evaluation of Tourism and Hospitality Services')

# Add background grids
ax.xaxis.grid(True, color='gray', linestyle='dashed', alpha=0.5)
ax.yaxis.grid(True, color='gray', linestyle='dashed', alpha=0.5)

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/93_202312302350.png')

# Clear the current image state
plt.clf()
