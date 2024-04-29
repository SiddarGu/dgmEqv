

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Country A','Country B','Country C','Country D']
data = np.array([[90, 85, 80, 75],
                 [75, 80, 85, 90],
                 [85, 80, 75, 70],
                 [80, 85, 90, 95],
                 [70, 65, 60, 55]])
line_labels = ['Social Welfare','Infrastructure','Economic Development','Political Stability','Education']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, line_label in enumerate(line_labels):
    line_data = np.append(data[i], data[i][0])
    ax.plot(angles, line_data, linewidth=3, label=line_label)
    ax.fill(angles, line_data, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
    ax.set_ylim(0, np.max(data))

for i in range(len(line_labels)):
    ax.plot(angles, np.full_like(angles, (i+1) * np.max(data) / len(line_labels)), '--', color='black', alpha=0.5)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.set_title("Government and Public Policy Performance Comparison", fontsize=16)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right", bbox_to_anchor=(1.25, 1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/21.png')
plt.clf()