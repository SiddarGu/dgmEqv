
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ["Productivity (Score)", "Efficiency (Score)", "Cost (Million $)", "Time (Hours)"]
line_labels = ["AI", "Robotics", "Automation", "Cloud Computing", "Big Data", "Quantum Computing"]
data = np.array([[90, 80, 20, 700], [70, 90, 15, 1000], [60, 85, 12, 300], [80, 95, 18, 500], [75, 87, 20, 400], [85, 92, 16, 200]])

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

for i in range(len(line_labels)):
    # normalize the size and color
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 5000 + 600
    color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
    ax.scatter(data[i, 0], data[i, 1], s=size, c=cm.cool(color), label=None)
    ax.scatter([], [], s=20, c=cm.cool(color), label=line_labels[i] + ": " + str(data[i, 2]))

ax.legend(title=data_labels[2], bbox_to_anchor=(1, 1))

norm = cm.colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = cm.ScalarMappable(cmap=cm.cool, norm=norm)
sm.set_array([])

plt.colorbar(sm, ax=ax, shrink=0.5, aspect=10, label=data_labels[3])
ax.set_title("Performance of Science and Engineering Technologies")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/9_2023122261326.png')
plt.clf()