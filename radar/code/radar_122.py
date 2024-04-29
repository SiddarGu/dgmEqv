import matplotlib.pyplot as plt
import numpy as np

data = np.array([[85, 80, 75, 90, 70],
                 [90, 85, 80, 95, 70],
                 [70, 80, 90, 85, 75],
                 [80, 90, 85, 95, 80],
                 [75, 70, 65, 80, 70]])

data_labels = ['General Hospital', 'Specialty Clinic', 'Psychiatric Facility', 'Rehabilitation Center', 'Elderly Care Facility']
line_labels = ['Patient Experience (Score)', 'Quality of Care (Score)', 'Staff Responsiveness (Score)', 'Facility Cleanliness (Score)', 'Cost Effectiveness (Score)']

# Plotting settings
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot radar chart
for i, row in enumerate(data):
    ax.plot(angles, row, marker='o', linewidth=2, label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim([0, np.max(data) + 10])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# Title
plt.title('Comparative Healthcare Facility Performance')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/108_202312302350.png')

# Clear the figure
plt.clf()