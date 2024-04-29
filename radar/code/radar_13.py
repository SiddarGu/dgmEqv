

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Group A', 'Group B', 'Group C', 'Group D']
line_labels = ['Music', 'Visual Art', 'Dance', 'Theatre', 'Literature']
data = [[90, 85, 80, 75], [80, 85, 90, 95], [65, 70, 75, 80], [70, 75, 80, 85], [75, 80, 85, 90]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(12, 10))
ax = plt.subplot(111, polar=True)

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2)
    ax.fill(angles, data[i], alpha=0.25)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14, rotation=45, wrap=True)
ax.set_rlim(0, max(max(data)))

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc=(0.9, 0.95), labelspacing=0.1, fontsize=14)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.title('Arts and Culture Performance Comparison', fontsize=18)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/19.png', bbox_inches='tight')
plt.clf()