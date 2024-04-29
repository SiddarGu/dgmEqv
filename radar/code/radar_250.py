import matplotlib.pyplot as plt
import numpy as np

# transform data into three variables
raw_data = "Area,Criminal Law,Family Law,Corporate Law,Environmental Law/n " \
           "Case Completion,85,80,70,75/n Resolution Rate,70,75,80,85/n " \
           "Client Satisfaction,80,85,90,95/n Public Trust,65,70,75,80/n " \
           "Legal Costs,50,55,60,65"
data_split = [row.split(",") for row in raw_data.split("/n ")]
data_labels = data_split[0][1:]
data = np.array([list(map(int, row[1:])) for row in data_split[1:]])
line_labels = [row[0] for row in data_split[1:]]

# setup radar chart
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# plot data and gridlines
for i, line in enumerate(data):
    line = np.append(line, line[0])  # for closing the polygon
    ax.plot(angles, line, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, radius, color='gray', linestyle=':')
        
# set up legend and titles
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.set_title("Performance Analysis Across Legal Sectors")

# remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# adjust radial limits
ax.set_ylim(0, data.max() * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# prevent content from being displayed and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/162_2023122292141.png')

# clear the current image state
plt.clf()
