import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 70, 90, 75, 65],
                 [10, 5, 15, 8, 3],
                 [95, 85, 97, 90, 80],
                 [120, 50, 160, 100, 40],
                 [85, 65, 95, 70, 60]])

data_labels = ['Popularity (%)', 'Revenue (Billion $)', 'Attendance Rate (%)', 'Player Salaries (Million $)', 'TV Rating (%)']
line_labels = ['NBA', 'MLS', 'NFL', 'NHL', 'NASCAR']

data = np.concatenate((data, data[:, 0:1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.title('Sports and Entertainment Industry Analysis')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/139_202312302350.png')

plt.clf()