import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

# input data
input_data = """Research,Publication Count,Number of Citations,Research Funding (Millions $),Collaboration Score
Psychology,1500,50000,100,8
Sociology,1000,30000,80,6
Anthropology,800,20000,70,7
History,1200,25000,90,5
Linguistics,900,15000,60,9
Literature,1100,18000,75,4
Philosophy,700,12000,50,7"""

lines = input_data.split("\n")
data_labels = lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=int)
line_labels = [f'{line.split(",")[0]} {data[i, 2]}' for i, line in enumerate(lines[1:])]

# setup scatter plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

# plot data
cmap = cm.get_cmap('Spectral')  # Colour map (there are many others)
colors = np.array([data[i, 3]/max(data[:, 3]) for i in range(data.shape[0])])
sizes = np.array([600+data[i, 2]/max(data[:, 2])*4400 for i in range(data.shape[0])])

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=[cmap(colors[i])], label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], c=cmap(colors[i]), s=20, label=line_labels[i])  # Add a scatter with label but size of 0 for legend

# legend and labels
ax.legend(title=data_labels[2])
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Impact of Research and Collaboration in Social Sciences and Humanities')

# Add a colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, aspect=30, label=data_labels[3], pad=0).set_label(data_labels[3])

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/340_202312311429.png')
plt.clf()
