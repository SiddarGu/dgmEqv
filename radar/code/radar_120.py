import matplotlib.pyplot as plt
import numpy as np

data = np.array([[85, 88, 91, 94],
                 [70, 73, 76, 79],
                 [80, 83, 86, 89],
                 [90, 93, 96, 99],
                 [75, 78, 81, 84]])

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Fuel Efficiency (%)', 'Renewable Energy Usage (%)', 'Waste Management (%)', 'Energy Production (%)', 'Grid Stability (%)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_rlabel_position(0)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title("Energy and Utilities Performance Report")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/158_202312310100.png')
plt.close()