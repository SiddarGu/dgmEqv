

import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Donations (%)', 'Volunteers (%)', 'Charitable Programs (%)', 'Education Programs (%)', 'Fundraising (%)']
line_labels = ['Red Cross', 'Local Church', 'Animal Shelter', 'Homeless Shelter', 'Food Bank']
data = np.array([[75, 70, 65, 60, 55], [50, 55, 60, 65, 70], [80, 85, 90, 95, 100], [65, 70, 75, 80, 85], [60, 65, 70, 75, 80]])
# append the first numerical element of that row to the end of that row for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure before plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles as np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)

# Plot data with different colors
for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1.5, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.1)

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_ylim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot the legend of data lines
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.2),
          shadow=True, ncol=2)

# Drawing techniques such as background grids
ax.grid(True)

# Set the title of the figure
plt.title('Charitable Impact in 2021')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/45_202312262320.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/45_202312262320.png')

# Clear the current image state at the end of the code
plt.clf()