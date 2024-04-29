import numpy as np
import matplotlib.pyplot as plt

# Transform the data into variables
data = np.array([[80, 85, 70, 75, 90],
                 [70, 75, 80, 85, 90],
                 [75, 80, 85, 90, 95],
                 [90, 85, 80, 75, 70],
                 [65, 70, 75, 80, 85]])
data_labels = ['Employee Engagement', 'Training Effectiveness', 'Performance Review', 'Employee Retention', 'Resource Allocation']
line_labels = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

# Create the figure and subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set the angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first element of each row to close the loop
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot the data lines
for row in range(len(data)):
    ax.plot(angles, data[row], linewidth=2, label=line_labels[row])

# Set the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set the radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add background grids
ax.grid(True)

# Create the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Set the title
plt.title('Human Resources and Employee Management Performance Comparison')

# Adjust the layout and save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/161_202312310100.png')

# Clear the current figure
plt.clf()