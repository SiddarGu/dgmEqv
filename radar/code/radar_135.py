import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Facebook', 'Twitter', 'LinkedIn', 'Instagram', 'YouTube']
line_labels = ['Active Users (millions)', 'User Engagement (%)', 'Average Time Spent (mins)', 'Ad Revenue ($m)', 'Content Reach (Score)']
data = np.array([[250, 200, 275, 300, 400],
                 [85, 80, 87, 90, 95],
                 [30, 25, 35, 40, 45],
                 [200, 150, 225, 250, 350],
                 [80, 75, 85, 90, 95]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.title('Social Media and Web Usage Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/204_202312310100.png')
plt.clf()