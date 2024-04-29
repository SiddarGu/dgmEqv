import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Family Law', 'Criminal Law', 'Civil Rights Law', 'Environmental Law', 'Intellectual Property Law', 'Business and Corporate Law']
data = np.array([[75, 80, 85, 70, 65, 90],
                 [80, 85, 90, 75, 70, 95],
                 [85, 90, 70, 75, 80, 95],
                 [70, 75, 80, 65, 60, 85],
                 [75, 80, 85, 90, 95, 85]])

line_labels = ['Case Win Rate (%)', 'Client Satisfaction (Score)', 'Legal Research Efficiency (Score)', 'Cost Efficiency (Score)', 'Staff Capability (Score)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot each row of data as a separate line
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(data)):
    ax.plot(angles, data[i], 'o-', color=colors[i], label=line_labels[i])

# Set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Set radial limits based on maximum value of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left', bbox_to_anchor=(0.9, 0.9))

# Set title
ax.set_title('Law Firms Performance Analysis')

# Set background grid
ax.grid(True)

# Adjust size and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/87_202312302350.png')

# Clear current image state
plt.clf()