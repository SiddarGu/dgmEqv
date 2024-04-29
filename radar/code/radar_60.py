import numpy as np
import matplotlib.pyplot as plt

data_labels = ['User Engagement (%)', 'Ad Revenue ($M)', 'Average Session Time (min)', 'Monthly Active Users (billions)', 'Content Sharing (%)']
line_labels = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'YouTube']
data = np.array([[80, 75, 70, 85, 90], [200, 180, 220, 170, 230], [20, 15, 23, 18, 30], [1.3, 0.9, 1.1, 0.5, 2], [70, 75, 60, 50, 90]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(data.shape[0]):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')
plt.title('Social Media and Web Analysis')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/152_202312310100.png')
plt.clf()