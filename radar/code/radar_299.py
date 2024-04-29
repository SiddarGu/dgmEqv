import numpy as np
import matplotlib.pyplot as plt


# Data preprocessing
data_labels = ['Design Efficiency', 'Quality Assurance', 'Project Management', 'Technical Skills', 'Problem Solving']
data = np.array([
    [85, 80, 90, 75, 85],
    [90, 85, 80, 95, 90],
    [75, 80, 85, 90, 75],
    [80, 90, 85, 95, 80]
])
line_labels = ['Engineer A', 'Engineer B', 'Engineer C', 'Engineer D']

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Evenly spaced angles for each axis
angles = np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False).tolist()
angles += angles[:1]  # complete the loop

# Iterate over each row in data
for i, row in enumerate(data):
    values = np.concatenate((row, [row[0]]))  # repeat the first value to close the loop
    ax.plot(angles, values, label=line_labels[i], linestyle='solid', linewidth=2)  # plot
    ax.fill(angles, values, alpha=0.25)  # fill
    radius = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, radius, color='silver', linestyle='dashed')

# plot the labels
ax.set_thetagrids([a * 180 / np.pi for a in angles[:-1]], data_labels)
ax.set_rlim(0,100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-150)

# handle the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# draw gridlines
ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# set title and save figure
plt.title('Engineer Performance Analysis in Science and Engineering', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/83_2023122292141.png')

# Clearing the current image
plt.clf()
