import numpy as np
import matplotlib.pyplot as plt

data_labels = np.array(['Healthy Foods', 'Snack Foods', 'Beverages', 'Alcohol', 'Confectionery'])
data = np.array([[50, 55, 60, 45, 70], [15, 20, 25, 20, 15], [7, 8, 9, 10, 6], [80, 85, 75, 70, 90], [90, 85, 80, 75, 70]])
line_labels = np.array(['Profit Margin (%)', 'Market Share (%)', 'Inventory Turnover', 'Customer Satisfaction (Score)', 'Supplier Reliability (Score)'])

# Create figure and subplot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Concatenate first element to close the loop
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each line
for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

# Set labels for each angle
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Set title
fig.suptitle('Radar Chart for Food and Beverage Industry Performance Analysis')

# Adjust layout and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/106_202312302350.png')

# Clear current image state
plt.clf()