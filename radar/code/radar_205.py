import numpy as np
import matplotlib.pyplot as plt

# transform given data into variables
data_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
data = [
    [60, 62, 65, 70, 68, 72],  # Recruitment
    [70, 75, 80, 72, 70, 76],  # Training
    [80, 82, 85, 88, 90, 92],  # Performance Evaluation
    [50, 45, 42, 40, 38, 39],  # Employee Turnover
    [85, 87, 88, 90, 92, 94],  # Employee Satisfaction
]
line_labels = [
    'Recruitment',
    'Training',
    'Performance Evaluation',
    'Employee Turnover',
    'Employee Satisfaction',
]

# create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# evenly space axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# iterate over each row in data
for idx, d in enumerate(data):
    d.append(d[0])  # close loop
    ax.plot(angles, d, label=line_labels[idx])
    radius = np.full_like(angles, ((idx+1) * max([max(d) for d in data]) / len(data)))
    ax.plot(angles, radius, color='grey', ls='--')  # plot gridlines

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)  # plot axis labels
ax.set_rlim(0, max([max(d) for d in data]))  # adjust radial limits
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.3, 1.1))

# desired enhancements
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# adding title
plt.title('Employee Management Overview - First Half of the Year')

# resize the figure
fig.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/47_2023122292141.png')

# clear the current image state
plt.clf()
