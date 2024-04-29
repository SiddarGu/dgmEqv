import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Donations Received (%)', 'Fundraising Efficiency (%)', 'Administrative Expenses (%)', 'Program Expenses (%)', 'Public Support (%)']
data = np.array([[85, 90, 95, 100],
                 [80, 85, 90, 95],
                 [70, 75, 80, 85],
                 [95, 100, 105, 110],
                 [90, 95, 100, 105]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)
ax.set_ylim(0, np.max(data))
ax.set_title('Charity and Nonprofit Organizations Efficiency Analysis')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='lower center')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/120_202312302350.png')
plt.clf()