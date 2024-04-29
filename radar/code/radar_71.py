import numpy as np
import matplotlib.pyplot as plt

data_labels = np.array(['Family Law', 'Criminal Law', 'Employment Law', 'Property Law', 'International Law'])
line_labels = np.array(['Legal Proficiency(Score)', 'Case Success Rate(%)', 'Client Satisfaction(Score)', 'Effeciency(Score)', 'Dispute Resolution(%)'])

data = np.array([[86, 80, 82, 88, 90],
                 [70, 75, 72, 78, 80],
                 [85, 82, 87, 88, 84],
                 [88, 85, 84, 86, 90],
                 [72, 75, 78, 82, 80]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.set_title('Analysis of Different Aspects in Law Fields')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/112_202312302350.png')
plt.close(fig)