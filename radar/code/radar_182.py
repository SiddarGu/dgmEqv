import numpy as np
import matplotlib.pyplot as plt

# Transform the data
data_labels = ['General Hospital', 'Dental Clinic', 'Eye Care Center', 'Pharmacy Store', 'Physical Rehabilitation Center']
line_labels = ['Patient Care', 'Prescription Accuracy', 'Sanitation Standards', 'Visit Comfort', 'Service Efficiency']

data = np.array([[85, 95, 80, 90, 70],
                 [75, 85, 90, 95, 80],
                 [95, 90, 85, 80, 85],
                 [87, 90, 80, 85, 88],
                 [90, 85, 88, 90, 70]])

# Add the first element to the end of each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Set the angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Plot the data lines
for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], label=line_label)

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

# Adjust the radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='best')

# Add background grids
ax.grid(True)

# Set the title
plt.title("Healthcare Quality Assessment Metrics")

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/77_202312302350.png")

# Clear the current image state
plt.clf()