import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
import numpy as np

# Data.
data_str = [
    "Van Gogh,2100,62,0,98",
    "Pablo Picasso,50000,120,28,100",
    "Monet,2000,50,12,91",
    "Rembrandt,600,40,7,92",
    "Michelangelo,6000,80,20,94",
    "Frida Kahlo,143,30,15,89",
    "Leonardo da Vinci,30,70,19,99",
    "Salvador Dali,1500,100,22,90",
    "Gustav Klimt,231,54,9,88",
    "Henri Matisse,800,65,16,92"
]

# Parse data.
data = np.array([list(map(float, i.split(",")[1:])) for i in data_str])
line_labels = [data_str[i].split(",")[0]+" "+str(int(data[i, 2])) for i in range(len(data_str))]
data_labels = ["Total Works", "Public Exhibitions (Number)", "Award Wins (Number)", "Influence Score (0-100)"]

# Normalize color.
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

# Normalize size.
sizes = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))

# Create figure and axes.
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Scatter plot.
for i in range(len(data)):
    line_label = line_labels[i]
    ax.scatter(data[i, 0], data[i, 1], s=sizes(data[i, 2]) * (5000-600) + 600, c=cm.jet(norm(data[i, 3])), alpha=0.6, label=None)
    ax.scatter([], [], c=cm.jet(norm(data[i, 3])), alpha=0.6, s=20, label=line_label)

# Legend.
ax.legend(title=data_labels[2], loc='lower right')

# Color bar.
sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Labels, title and grid.
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Influence and Recognition of Notable Artists, Analysis of Art and Culture")
ax.grid(True)

# Save and show.
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/221_202312310045.png")
plt.clf()
