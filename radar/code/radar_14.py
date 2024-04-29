
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Facebook', 'Twitter', 'Instagram', 'YouTube', 'LinkedIn']
line_labels = ['User Engagement (Score)', 'User Satisfaction (Score)', 'Advertising Effectiveness (Score)', 'Content Quality (Score)', 'Data Privacy (Score)']
data = np.array([[85, 80, 75, 70, 65],
                 [90, 85, 80, 75, 70],
                 [75, 80, 85, 90, 95],
                 [80, 85, 90, 95, 95],
                 [70, 65, 60, 55, 60]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
ax.set_title('Social Media and the Web Performance Evaluation')

for i in range(len(data)):
    ax.plot(angles, data[i], label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0, 100)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1))

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/34_202312262320.png')
plt.clf()