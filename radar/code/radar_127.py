import numpy as np
import matplotlib.pyplot as plt

data_labels = ['HR Team', 'Employee Relations Team', 'Talent Acquisition Team', 'Compensation & Benefits Team', 'Learning & Development Team']
line_labels = ['Employee Satisfaction (Score)', 'Employee Retention (Score)', 'Performance Management (Score)', 'Training Effectiveness (Score)', 'Payroll Management (Score)']

# Transform data into numerical ndarray
data = np.array([[82, 85, 80, 79, 84],
                 [80, 85, 82, 83, 81],
                 [85, 80, 78, 88, 85],
                 [78, 80, 82, 85, 88],
                 [85, 90, 88, 87, 85]])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append first numerical element of each row to end for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot data lines
colors = ['r', 'g', 'b', 'y', 'm']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
max_data = np.amax(data)
ax.set_ylim(0, max_data + 5)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Add background grids
ax.grid(True, linestyle='--')

# Set title
fig.suptitle('HR & Employee Management Performance Analysis')

# Resize and save image
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/150_202312310100.png')

# Clear current image state
plt.cla()
plt.clf()
plt.close()