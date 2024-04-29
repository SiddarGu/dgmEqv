import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Nano Engineering', 'Bioengineering', 'Robotics', 'Astronomy', 'Quantum Physics']
line_labels = ['Research Quality (Score)', 'Labs Condition (Score)', 'Staff Capability (Score)', 'Publications (Number)', 'Grants Received ($ Million)']

data = np.array([[85, 90, 95, 80, 85],
                 [90, 85, 95, 80, 85],
                 [85, 90, 85, 90, 95],
                 [8, 9, 10, 7, 8],
                 [15, 16, 17, 18, 19]])

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
ax.set_title("Science and Engineering Research Performance")
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/68_202312302350.png")
plt.clf()