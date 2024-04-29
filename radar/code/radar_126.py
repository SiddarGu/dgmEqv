import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data = np.array([[70, 75, 80, 85, 65, 70, 75, 80],
                 [50, 55, 60, 65, 70, 75, 80, 85],
                 [60, 65, 70, 75, 75, 80, 85, 90],
                 [80, 85, 90, 95, 50, 55, 60, 65],
                 [65, 70, 75, 80, 80, 85, 90, 95]])
line_labels = ['Electronics', 'Clothing', 'Home Goods', 'Books', 'Grocery']
data_labels = ['Online Sales Q1', 'Online Sales Q2', 'Online Sales Q3', 'Online Sales Q4',
               'In-store Sales Q1', 'In-store Sales Q2', 'In-store Sales Q3', 'In-store Sales Q4']

# Create figure and subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set angles for radar axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Iterate over each row to plot data lines with different colors
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

# Set axis labels and adjust radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper left')

# Set title
plt.title('Retail and E-commerce Sales Performance')

# Save and clear the current image state
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/81_202312302350.png')
plt.clf()