import numpy as np
import matplotlib.pyplot as plt

data = np.array([[70, 80, 85, 65, 70, 75],
                [60, 70, 80, 50, 60, 65],
                [80, 90, 85, 75, 80, 75],
                [60, 70, 75, 60, 65, 70],
                [50, 40, 35, 55, 50, 45]])

data_labels = ['Twitter', 'Facebook', 'Instagram', 'LinkedIn', 'Pinterest', 'Snapchat']
line_labels = ['User Engagement (%)', 'Content Share (%)', 'Advertising Reach (%)', 'User Growth (%)', 'Bounce Rate (%)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, marker='o', label=line_labels[i])
    ax.fill(angles, row, alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.title('Social Media and Web Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/171_202312310100.png')

plt.clf()