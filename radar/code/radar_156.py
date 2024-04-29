import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data = np.array([[85, 90, 88, 83, 80],
                 [87, 91, 89, 85, 84],
                 [88, 92, 89, 84, 83],
                 [78, 85, 83, 70, 75],
                 [90, 94, 88, 85, 84]])

data_labels = ['Student Satisfaction (%)', 'Graduation Rate (%)', 'Faculty Quality Score',
               'Extracurricular Activities Score', 'Infrastructure Score']
line_labels = ['Public School', 'Private School', 'Charter School', 'Online Education', 'Community College']

# Create figure and plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row and append the first numerical element to the end
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plot each line
colors = ['r', 'g', 'b', 'c', 'm']
for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], label=line_label, color=colors[i])

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
ax.set_ylim(0, np.max(data))

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Set title
plt.title('Comparative Analysis of Educational Institutes')

# Add background grids
ax.grid(True)

# Automatically resize image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/59_202312302350.png')

# Clear current image state
plt.clf()