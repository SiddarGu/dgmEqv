import numpy as np
import matplotlib.pyplot as plt

# given data
data_string = "Fields,History,Psychology,Sociology,Philosophy,Literature/n Research Quality,85,80,75,70,90/n Teaching Quality,90,85,80,75,88/n Student Satisfaction,75,80,85,90,82/n Publication Rate,80,85,90,95,92/n Impact Factor,70,65,60,55,72"
data_string = data_string.replace("/n", "\n")
data_list = [row.split(",") for row in data_string.split("\n")]

# transforming the data into data_labels, line_labels and data
data_labels = data_list[0][1:]
line_labels = [row[0] for row in data_list[1:]]
data = np.array([list(map(int, row[1:])) for row in data_list[1:]])

# make the plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

# evenly space the axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for idx, row in enumerate(data):
    # append the first numerical element of that row to its end
    data_line = np.append(row, row[0])
    ax.plot(angles, data_line, label=line_labels[idx])

    # generate a angle-like radius vector
    radius = np.full_like(angles, (idx+1)*data.max() / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dashed')

# plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# adjust the radial limits
ax.set_rlim(0, data.max())
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# set title and save the plot
plt.title("A Comparative Analysis of Different Social Science and Humanities Disciplines")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/82_2023122292141.png')
plt.clf()
