import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import NullFormatter

# Parse the given string data
data_str = "Product,Annual Sales (Billion $),Market Share (%),Profit Margin (%),Health Rating (Out of 10)\n Coffee,100,25,30,7\n Tea,80,20,28,9\n Soft Drinks,120,30,35,4\n Beer,70,17,33,6\n Wine,45,8,40,8\n Spirits,35,7,37,6\n Water,150,40,45,10"
lines = data_str.split("\n")
data_labels = lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=float)
line_labels = [line.split(",")[0] + " " + str(data[i, 2]) for i, line in enumerate(lines[1:])]

fig, ax = plt.subplots(figsize=(12, 8))
colors = data[:, 3]
bubble_size = data[:, 2]
normalize_color = mcolors.Normalize(min(colors), max(colors))
normalize_size = mcolors.Normalize(min(bubble_size) - 10, max(bubble_size))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=plt.cm.viridis(normalize_color(colors[i])),s=1500*np.pi*normalize_size(bubble_size[i])**2,  label=None)
    ax.scatter([], [], c=plt.cm.viridis(normalize_color(colors[i])), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

sm = ScalarMappable(norm=normalize_color, cmap=plt.cm.viridis)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

plt.title("Profit, Market Share, and Health Impact of Various Beverage Products")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/277_202312310045.png")
plt.clf()
