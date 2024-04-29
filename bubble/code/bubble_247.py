import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# transform the data
raw_data = """Research Area,Number of Researchers,Publication Count,Impact Factor,Public Interest Score
Archaeology,500,1200,2.5,7
Anthropology,600,1500,3.0,6
Linguistics,700,1800,3.5,8
Philosophy,400,1100,2.0,9
Sociology,800,2000,3.7,5
Literature,300,1000,2.3,8"""
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] + ' ' + line.split(',')[2] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

# create figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot()

# normalize size and color
size_scale = 5000 - 600
color_scale = max(data[:, 3]) - min(data[:, 3])
sizes = [(value - min(data[:, 2]))*10000 + 600 for value in data[:, 2]]
colors = [(value - min(data[:, 3]))/color_scale for value in data[:, 3]]
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

# plotting
for i in range(len(data)):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], color=color, alpha=0.5, label=None)
    ax.scatter([], [], color=color, alpha=0.5, s=20, label=line_labels[i])

# set legend
ax.legend(title=data_labels[2], loc="upper left")

# set colorbar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, orientation="vertical", label=data_labels[3])

# draw grid, labels and title
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Publication and Impact Assessment in Various Fields of Social Sciences and Humanities')

# auto layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/112_202312301731.png')

# clear figure
plt.clf()
