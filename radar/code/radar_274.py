import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Public Education (Score)', 'Health Policy (Score)', 'Environmental Policy (Score)', 'National Defense (Score)', 'Economic Policy (Score)']
data = np.array([[75, 80, 85, 90], [70, 75, 80, 85], [65, 70, 75, 80], [80, 85, 90, 95], [85, 90, 95, 100]])

num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for i in range(len(data)):
    data_row = np.concatenate((data[i], [data[i][0]]))
    ax.plot(angles, data_row, color='C' + str(i), label=line_labels[i])
    ax.fill(angles, data_row, color='C' + str(i), alpha=0.25)

    gridlines = np.full_like(angles, (i+1) * data.max() / len(data))
    ax.plot(angles, gridlines, color='silver', linestyle='--')

ax.set_thetagrids(angles[:-1] * 180/np.pi, labels=data_labels, rotation=90, wrap=True)
ax.set_rlim(0, data.max())
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.title('Government Policy Efficiency Evaluation', size=20, color='blue', y=1.1)
plt.tight_layout()

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/194_2023122292141.png')
plt.clf()
