
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ["Popularity (Score)", "Participation (Million)", 
               "Revenue (Billion $)", "Income (Score)"]
line_labels = ["Football", "Basketball", "Baseball", "Ice Hockey", 
               "Golf", "Tennis"]
data = np.array([[90, 3.5, 20, 7],
                 [85, 2.8, 25, 8],
                 [75, 2.5, 14, 5],
                 [55, 2.2, 10, 4],
                 [45, 1.8, 8, 3],
                 [40, 1.2, 5, 2]])

cmap = cm.get_cmap("jet")
norm = plt.Normalize(data[:, 2].min(), data[:, 2].max())
norm_c = plt.Normalize(data[:, 3].min(), data[:, 3].max())

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

for i in range(data.shape[0]):
    line_label = line_labels[i] + " " + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], s=2000 * norm(data[i, 2]) + 600, 
               c=cmap(norm_c(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm_c(data[i, 3])), label=line_label, s=20)

ax.legend(title=data_labels[2], fontsize=8)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

ax.grid(linestyle="dashed")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Popularity of Sports and Their Economic Impact")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/28_2023122270050.png")
plt.clf()