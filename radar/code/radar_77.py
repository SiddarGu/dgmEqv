import numpy as np
import matplotlib.pyplot as plt

# Given data
data = np.array([[80, 82, 84, 86],
                 [70, 72, 75, 77],
                 [80, 82, 85, 87],
                 [90, 92, 95, 97],
                 [85, 87, 90, 93],
                 [75, 77, 80, 82]])

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Dairy Products', 'Bakery Items', 'Meat and Poultry', 'Beverage', 'Fruits and Vegetables', 'Confectionery']

# Add the last element to each row for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_ylim(0, np.max(data))

# Plot the data lines with different colors
colors = ['r', 'b', 'g', 'm', 'c', 'y']
for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1.5, label=line_labels[i], color=colors[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set title
plt.title('Revenue Performance in the Food and Beverage Industry')

# Save the chart
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/189_202312310100.png')

# Clear the image state
plt.clf()