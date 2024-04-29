import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# transform the data
data_string = 'Aspect,Green Energy,Non-renewable energy,Biomass,Hydroelectric/n Energy Production,70,65,60,55/n Efficiency,75,70,65,60/n Cost Efficiency,80,75,70,65/n Sustainability,85,80,75,70/n Market Share,90,85,80,75'
data_lines = data_string.split('/n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in data_lines[1:]])

# create a figure and add a subplot with polar projection
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# determine the number of data points and set the angles for each data point
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# plot the data
colors = cm.viridis(np.linspace(0, 1, len(data)))
for i in range(len(data)):
    stats = np.concatenate((data[i], [data[i][0]]))  # close the loop
    ax.plot(angles, stats, 'o-', color=colors[i], label=line_labels[i])
    radius = np.full_like(angles, (i+1)*np.amax(data)/len(data))
    ax.plot(angles, radius, '-', color=colors[i])

# adjust axis labels and limits
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)
ax.set_rlim(0, np.amax(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# set the title
ax.set_title('Energy & Utilities Performance Overview', size=20, color='black', y=1.1)

# remove gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# resize the figure and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/92_2023122292141.png')

# clear the current figure
plt.clf()
