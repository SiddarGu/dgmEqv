import numpy as np
import matplotlib.pyplot as plt

data = np.array([[75, 85, 80, 70, 65],
                 [80, 90, 85, 75, 70],
                 [70, 80, 75, 65, 60],
                 [85, 90, 85, 75, 70],
                 [65, 70, 75, 80, 85]])

data_labels = ['Twitter', 'Facebook', 'Instagram', 'LinkedIn', 'Pinterest']
line_labels = ['User Engagement (%)', 'Ad Reach (%)', 'Traffic Source (%)', 'Content Sharing (%)', 'User Growth Rate (%)']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['b', 'g', 'r', 'c', 'm']

for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], label=line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

ax.set_title('Social Media and Web Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/90_202312302350.png')
plt.close()
