
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data_labels = ['Cost (Billion $)', 'Research Time (Years)', 'Number of Scientists', 'Outcome (Score)']
data = np.array([['Project', 'Cost (Billion $)', 'Research Time (Years)', 'Number of Scientists', 'Outcome (Score)'],
                  ['Fusion Reactor', 30, 10, 400, 7],
                  ['Supercomputer', 20, 7, 300, 9],
                  ['Space Station', 50, 15, 1000, 8],
                  ['Vaccine Development', 15, 5, 200, 10],
                  ['Autonomous Vehicle', 10, 4, 100, 8]])

line_labels = []
for i in range(1, data.shape[0]):
    line_labels.append(data[i, 0] + ' ' + str(data[i, 3]))

fig, ax = plt.subplots()

cmap = cm.get_cmap('Spectral')
norm = plt.Normalize(0, data[1:, 3].astype(float).max())
norm_c = plt.Normalize(0, data[1:, -1].astype(float).max())

for i in range(1, data.shape[0]):
    ax.scatter(data[i, 1].astype(int), data[i, 2].astype(int), s=norm(data[i, 3].astype(float)) * 500 + 60, c=cmap(norm_c(data[i, 4].astype(float))), label=None)
    ax.scatter([], [], s=20, c=cmap(norm_c(data[i, 4].astype(float))), label=line_labels[i - 1])

ax.legend(title=data_labels[3])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm_c)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle='--')
ax.set_title('Impact of Science and Engineering Projects on the World')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/1_2023122270050.png')
plt.clf()