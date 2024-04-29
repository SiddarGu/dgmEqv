
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Elementary","Middle School","High School","University"]
line_labels = ["Math Scores","Science Scores","English Scores","Arts Scores","Technology Scores"]
data = [[75,85,90,93],
        [70,80,85,90],
        [85,90,95,97],
        [65,75,80,90],
        [80,85,90,95]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='polar')

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], 'o-', label=line_labels[i], linewidth=2)
    ax.fill(angles, data[i], alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
    ax.set_ylim(0, max(map(max,data))+5)

for i in range(len(data)):
    ax.plot(angles, np.full_like(angles, (i+1) * max(map(max,data)) / len(data)), '--', color='black', linewidth=2)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(0.1, 0.1))
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.title('Academic Achievements - 2021', fontsize=15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/14.png')
plt.close()