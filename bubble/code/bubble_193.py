import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np
from matplotlib.cm import get_cmap


# Given data 
data_string = "Genre,Box Office Revenue (Million $),Number of Theaters,Rating (Out of 10),Cultural Impact (Score)\n Action,1500,500,7.5,8\n Comedy,800,300,6.5,6\n Drama,600,200,8.5,9\n Romance,450,150,7,7.5\n Thriller,700,250,7,7\n Animation,1200,400,8,9"

# Parse the string data into a numpy array and separate labels
data_lines = data_string.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] + line.split(",")[2] for line in data_lines[1:]]
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)

# Normalize the colors
c_norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

# Begin figure and set the size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
cmap = get_cmap("viridis")
# Iterate on the data and plot
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1],  c=cmap(c_norm(data[i, 3])),
               s=600 + 4400 * (data[i, 2] / max(data[:, 2])), label=None)
    ax.scatter([], [], color=cmap(c_norm(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2], loc='center left')
ax.grid(True)

# Add a color bar
sm = ScalarMappable(norm=c_norm, cmap='viridis')
plt.colorbar(sm, label=data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title("Box Office Revenue and Cultural Impact by Film Genre")

fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/349_202312311429.png")

plt.clf()
