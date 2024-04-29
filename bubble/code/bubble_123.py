import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib import gridspec

data_dir = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/"
save_path = data_dir + "png/160_202312310045.png"

data = """Policy Area,Annual Investment (Billion $),Public Support Score(Out of 10),Policy Effectiveness (Out of 10),Economic Impact (Billion $)
Health,250,8,7,400
Education,200,7,8,350
Environment,100,7,6,150
Immigration,50,5,5,80
Infrastructure,150,6,7,200
Defense,300,7,8,450"""

# Represents the labels of each column except the first column
data_labels = data.split('\n')[0].split(',')[1:]

# The labels of each row except the first row
line_labels = [x.split(',')[0] for x in data.split('\n')[1:]]

# Each line_label suffixed with data[i, 2]
line_labels = [line_labels[i] + ': ' + str(int(data.split('\n')[i+1].split(',')[2])) for i in range(len(line_labels))]

# Represents the numerical array in the data
data = np.array([[int(x) for x in row.split(',')[1:]] for row in data.split('\n')[1:]])

# Normalize data for coloring
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
colors = [cmap(norm(value)) for value in data[:, 3]]

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

# Normalizing the data for bubble size
size_scale = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
sizes = [600 + 4400*size_scale(value) for value in data[:, 2]]

for (i, color) in enumerate(colors):
    _ = ax.scatter(data[i, 0], data[i, 1], color=color, s=sizes[i], label=None)
    _ = ax.scatter([], [], color=color, label=line_labels[i])

# Add the legend with the title
_ = ax.legend(title=data_labels[2], loc='upper left', borderaxespad=0.)

# Add color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, label=data_labels[3], pad=0.2)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Evaluating Government Investment and Impact Across Policy Areas')

plt.grid(True)
plt.tight_layout()
plt.savefig(save_path, bbox_inches='tight')
plt.clf()
