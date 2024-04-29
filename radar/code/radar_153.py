
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Complexity (Index)', 'Popularity (Index)', 'Precedent (Index)', 'Resources (Index)', 'Enforcement (Index)']
line_labels = ['Copyright Law', 'Tax Law', 'Contract Law', 'Family Law', 'Employment Law']
data = np.array([[7, 4, 9, 2, 1],
                 [9, 3, 8, 4, 3],
                 [8, 5, 7, 5, 4],
                 [6, 7, 6, 6, 5],
                 [5, 6, 4, 7, 6]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=90)
ax.set_rlim(0, 10)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.2)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.legend(loc='upper right')
plt.title('Legal Framework Evaluation in 2023', fontsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/10_202312262320.png')
plt.clf()