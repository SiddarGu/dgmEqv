import numpy as np
import matplotlib.pyplot as plt

data = np.array([[70, 80, 90, 85], [75, 85, 95, 80], [80, 70, 60, 75], [85, 95, 70, 80], [80, 90, 70, 60]])
data_labels = ['Policy A', 'Policy B', 'Policy C', 'Policy D']
line_labels = ['Public Opinion', 'Policy Effectiveness', 'Implementation Efficiency', 'Policy Transparency', 'Public Participation']

num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=45)

for idx, radian in enumerate(data):
    ax.fill(angles, np.append(radian, radian[0]), 'b', alpha=0.25)
    ax.plot(angles, np.append(radian, radian[0]), lw=2, label=line_labels[idx])

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
ax.set_ylim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.spines['polar'].set_visible(False)
plt.title('Government Policy Evaluation', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/99_2023122292141.png')
plt.clf()
