import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Criminal Court', 'Civil Court', 'Environmental Court', 'Tax Court', 'Family Court']
line_labels = ['Case Completion Rate (%)', 'Client Satisfaction (Score)', 'Rule of Law (Score)', 'Efficiency (Score)', 'Legal Aid Availability (%)']
data = np.array([[70, 75, 80, 85, 90],
                 [85, 80, 85, 90, 75],
                 [90, 85, 80, 75, 70],
                 [75, 80, 85, 90, 95],
                 [80, 85, 70, 80, 75]])

# Close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create a figure and plot the radar chart
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    
# Set axis labels and limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='lower right')

# Set title
plt.title('Legal Affairs Evaluation')

# Add background grids
ax.grid(True)

# Automatically resize the image
fig.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/138_202312302350.png')

# Clear the current image state
plt.clf()