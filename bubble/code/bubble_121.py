import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# data
data_str = """John Smith, 50, 80, 100000, 10
Mary Johnson, 30, 75, 80000, 8
Michael Davis, 40, 85, 90000, 12
Jennifer Wilson, 35, 95, 95000, 11
David Thompson, 25, 70, 75000, 7
Sarah Martinez, 20, 90, 85000, 9
Robert Anderson, 45, 75, 80000, 10
Karen Thomas, 15, 80, 90000, 6
Christopher Garcia, 30, 85, 95000, 8
Amanda Robinson, 40, 90, 100000, 13"""
data_lines = data_str.split("\n")

data_labels = ["Number of Cases Handled", "Success Rate (%)", "Average Settlement ($)", "Years of Experience"]
line_labels = [x.split(",")[0] + "_" + str(x.split(",")[2]) for x in data_lines]
data = np.array([[float(y) for y in x.split(",")[1:]] for x in data_lines])

#normalizing bubble sizes
sizes = (data[:, 2] - np.min(data[:, 2]))/(np.max(data[:, 2]) - np.min(data[:, 2]))
sizes = 600 + sizes * 4400

#normalizing color values
colors = (data[:, 3] - np.min(data[:, 3]))/(np.max(data[:, 3]) - np.min(data[:, 3]))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

cmap = mcolors.LinearSegmentedColormap.from_list("", ["red", "yellow", "green"])
cNorm  = mcolors.Normalize(vmin=0, vmax=1)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)

for i in range(len(sizes)):
    ax.scatter(data[i, 0], data[i, 1], label=None, s=sizes[i], c=scalarMap.to_rgba(colors[i]))
    ax.scatter([], [], c=scalarMap.to_rgba(colors[i]), s=20, label=line_labels[i])

ax.grid(True)

ax.legend(title=data_labels[2], loc='upper left')

ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], rotation=0, wrap=True)

fig.suptitle('Performance of Lawyers in Law and Legal Affairs')

#color bar
cb_ax = fig.add_axes([0.93, 0.1, 0.02, 0.8])
cbar = fig.colorbar(scalarMap, cax=cb_ax)
cbar.set_label(data_labels[3])

# to avoid plot area to be offset
plt.tight_layout()
    
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/385_202312311429.png')

plt.clf()
