import numpy as np
import matplotlib.pyplot as plt

data_string = "Category,Pre Industrial,1990s,2000s,2010s,2020s/n Air Quality,80,70,60,55,60/n Water Quality,75,65,60,65,70/n Forest Cover,85,70,65,60,65/n Renewable Energy Use,40,50,60,70,75/n Waste Management,50,55,60,65,70"
data_list = [item.split(',') for item in data_string.split('/n')]
data_labels = data_list[0][1:]
line_labels = [item[0] for item in data_list[1:]]
data = np.array([list(map(int, item[1:])) for item in data_list[1:]])

num_vars = len(data_labels)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, [0]]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(polar=True)

for i, row in enumerate(data):
    ax.plot(angles, np.full_like(angles, (i + 1) * np.amax(data) / len(data)), color='silver')
    ax.plot(angles, row, marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=75)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title('Environment and Sustainability Progress Over Time', size=20, color='blue', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/169_2023122292141.png')
plt.clf()
