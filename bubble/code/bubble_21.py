
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data_labels = ['Cases Filed (Millions)', 'Judgments (Millions)', 'Time Spent (Hours)', 'Satisfaction Level (Score)']
data = np.array([[1.2, 0.6, 2.3, 6], [0.9, 0.4, 4.5, 5], [0.6, 0.2, 1.5, 7], [0.3, 0.1, 2.5, 8], [0.2, 0.05, 1.0, 9], [0.1, 0.05, 2.0, 7]])
line_labels = ['Civil', 'Criminal', 'Administrative', 'Immigration', 'Constitutional', 'Taxation']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
scalar_map = cm.ScalarMappable(norm=plt.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])))

for i in range(data.shape[0]):
    size = 500 * (data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) + 60
    ax.scatter(data[i, 0], data[i, 1], c=scalar_map.to_rgba(data[i, 3]), s=size, label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), s=20, label=line_labels[i] + ' ' + str(data[i, 2]) + ' hours')

ax.legend(title=data_labels[2], loc='upper left', bbox_to_anchor=(0.0, 1.01))
cbar = fig.colorbar(scalar_map, ax=ax, orientation='horizontal', aspect=50)
cbar.ax.set_title(data_labels[3])
ax.grid()
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Evaluating the Performance of Law and Legal Affairs - 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/9_2023122270050.png')
plt.clf()