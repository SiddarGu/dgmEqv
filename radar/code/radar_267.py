import matplotlib.pyplot as plt
import numpy as np

raw_data = 'Dimension,Q1,Q2,Q3,Q4\nRecruitment,60,65,70,75\nEmployee training,55,60,65,70\nWork-life balance,70,75,80,85\nEmployee Retention,80,85,90,95\nCompensation and Benefits,75,80,85,90'

lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])
data = np.concatenate((data, np.array([data[:, 0]]).T), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, np.amax(data) * 1.1)

for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])
    radii = np.full_like(angles, (i+1) * np.amax(data) / len(data))
    ax.plot(angles, radii, color='grey', linestyle='dashed')

ax.yaxis.grid(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.spines['polar'].set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
plt.title('Human Resources and Employee Management Metrics')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/60_2023122292141.png')
plt.clf()
