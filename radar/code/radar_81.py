import numpy as np
import matplotlib.pyplot as plt

data = np.array([[85, 80, 75, 70, 65],
                [60, 65, 70, 75, 80],
                [75, 80, 85, 90, 95],
                [70, 75, 80, 85, 90],
                [90, 85, 80, 75, 70]])

data_labels = ['Case Clearance Rate (%)', 'Average Processing Time (Days)', 'Conviction Rate (%)', 'Legal Assistance Availability (%)', 'Rule of Law Compliance (Score)']
line_labels = ['Aspect', 'Local Court', 'State Court', 'Federal Court', 'Supreme Court', 'International Court']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, marker='o', label=line_labels[i+1])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

plt.title('Analysis of Court Efficiency')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/62_202312302350.png')
plt.close()