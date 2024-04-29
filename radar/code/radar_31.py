
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Network Security', 'AI Development', 'Mobile Computing', 'Cloud Computing', 'Web Development']
data = np.array([[70, 75, 80, 85],
                 [60, 65, 70, 75],
                 [50, 55, 60, 65],
                 [80, 85, 90, 95],
                 [65, 70, 75, 80]]).T

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, [data[0]])).T

for i in range(len(data)):
    ax.plot(angles, data[i], linewidth=1, linestyle='solid', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.1)

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
ax.set_title('Technology and Internet Advancement in 2023', y=1.08)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/1.png')
plt.clf()