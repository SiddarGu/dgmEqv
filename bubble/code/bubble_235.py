import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# data
data_labels = ["Revenue (Million $)", "Patronage (Millions)", "Cultural Importance (Score)", "Innovation (Score)"]
data = np.array([
    [200, 15, 85, 70],
    [150, 12, 80, 75],
    [3000, 500, 85, 90],
    [500, 50, 80, 85],
    [300, 30, 82, 80],
    [2000, 200, 88, 85],
    [90, 8, 70, 75],
    [80, 5, 75, 80]
])
line_labels = ["Painting", "Sculpture", "Film", "Literature", "Theatre", "Music", "Photography", "Dance"]

# Create the figure object
fig = plt.figure(figsize=(16, 10))

ax = fig.add_subplot(111)

# color normalization
colors = data[:, 3]
normalize = mcolors.Normalize(vmin=np.min(colors), vmax=np.max(colors))

# size normalization
sizes = 600 + (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * 4400

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=plt.cm.jet(normalize(colors[i])),
               s=sizes[i], label=None)
    ax.scatter([], [], c=plt.cm.jet(normalize(colors[i])), s=20, label="{0}: {1}".format(line_label, data[i, 2]))

ax.legend(title=data_labels[2], loc="best", bbox_to_anchor=(1, 0, 0.5, 1))

# Color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=normalize)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

ax.grid(True)

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title("Relationship of Revenue, Patronage, and Cultural Importance in Different Art Forms")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/260_202312310045.png')
plt.clf()
