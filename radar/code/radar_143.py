import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Laser Technology', 'Rocket Science', 'Nanotechnology', 'Artificial Intelligence', 'Geological Engineering']
line_labels = ['Accuracy (%)', 'Precision (%)', 'Reproducibility (%)', 'Correctness (%)', 'Efficiency (%)']

data = np.array([[90, 85, 80, 95, 80],
                 [88, 84, 82, 94, 85],
                 [92, 87, 85, 98, 86],
                 [94, 89, 84, 100, 90],
                 [96, 91, 88, 102, 92]])

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_theta_offset(np.pi/2)
ax.set_rlabel_position(0)

max_value = np.amax(data)
ax.set_rlim(0, max_value + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower right')

plt.title('Performance Comparison Of Different Science And Engineering Fields')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/178_202312310100.png')
plt.clf()
