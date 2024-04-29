import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [85, 70, 60, 90, 75, 80],
    [80, 65, 55, 85, 70, 90],
    [90, 75, 70, 85, 80, 75],
    [700, 550, 600, 650, 600, 720],
    [80, 85, 90, 85, 80, 95]
])

data_labels = ['Football', 'Basketball', 'Baseball', 'Tennis', 'Golf', 'eSports']
line_labels = ['Popularity Score', 'Audience Engagement', 'Player Satisfaction', 'Revenue (Millions)', 'Media Coverage (%)']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i])

ax.set_theta_zero_location('N')
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45)

ax.set_ylim(0, np.max(data) * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc='upper right')
legend.set_title('')

ax.grid(True)

plt.title('Sports and Entertainment Overview')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/125_202312302350.png')
plt.clf()
