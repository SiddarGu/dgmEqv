import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Aspect', 'NASA', 'European Space Agency', 'SpaceX', 'Blue Origin/Virgin Galactic']
line_labels = ['Innovation (Score)', 'Research Efficiency (Score)', 'Technology Advancement (Score)',
               'Resource Management (Score)', 'Mission Success (Score)']
data = np.array([[90, 85, 95, 80, 85],
                 [95, 90, 85, 80, 70],
                 [90, 92, 95, 90, 88],
                 [85, 88, 90, 85, 80],
                 [90, 92, 92, 85, 80]])

plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
max_value = np.max(data)
ax.set_ylim(0, max_value + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1))

plt.title('Performance Analysis of Space Agencies')

plt.grid(True)

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/137_202312302350.png')

plt.clf()
