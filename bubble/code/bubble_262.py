import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

#Transforming the given data
data_labels = ["Number of Students (Thousands)", "Number of Faculties", "Research Funding (Million $)", "Global Ranking"]
data = np.array([
    [20, 2400, 1000, 3],
    [23, 1700, 860, 1],
    [16, 2100, 920, 2],
    [11, 1000, 850, 4],
    [19, 1800, 800, 5],
    [13, 1300, 700, 6],
    [26, 3200, 780, 7]
])
line_labels = ["Harvard University", "Oxford University", "Stanford University", "Massachusetts Institute of Technology", "Cambridge University", "University of Chicago", "Columbia University"]

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

cmap = cm.get_cmap('Spectral')

# Normalize to the range of cmap values
color_norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
bubble_sizes = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
bubble_sizes = bubble_sizes(data[:, 2]) * 5000 + 600

for i in range(len(line_labels)):
    line_label = f"{line_labels[i]} {data[i, 2]}"
    ax.scatter(data[i, 0], data[i, 1], color=cmap(color_norm(data[i,3])), s=bubble_sizes[i], label=None, alpha=0.5)
    ax.scatter([],[], color=cmap(color_norm(data[i,3])), label=line_label)

ax.legend(title=data_labels[2], loc="upper left")
plt.grid(True)

# Add a color bar
sm = cm.ScalarMappable(cmap=cmap, norm=color_norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Set labels for x and y axis
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set title for the chart
plt.title('Analysis of Top Universities: Student Numbers, Faculty, Research Funding, and Global Ranking')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/181_202312310045.png")
plt.clf()
