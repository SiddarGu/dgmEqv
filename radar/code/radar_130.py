import numpy as np
import matplotlib.pyplot as plt

data = np.array([[500, 400, 300, 200, 150, 100],
                [250, 300, 350, 200, 250, 300],
                [95, 90, 85, 80, 75, 90],
                [85, 90, 85, 80, 80, 95],
                [400, 350, 300, 250, 200, 150]])

data_labels = ['NBA Finals', 'FIFA World Cup', 'Olympic Games', 'Wimbledon', 'UFC Championship', 'Super Bowl']
line_labels = ['Ticket Sales (Thousands)', 'Media Coverage (Hours)', 'Athlete Performance (Score)', 
               'Fan Engagement (Score)', 'Merchandise Sales (Thousands)']

# transform data for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# create figure and subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, polar=True)

# evenly space axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# plot the data lines with different colors
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], label=line_labels[i])

# plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# adjust radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.2, 1))

# set title
plt.title('Sports and Entertainment Events Analysis')

# add grid lines
ax.grid(True)

# resize image
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/94_202312302350.png')

# clear current image state
plt.clf()