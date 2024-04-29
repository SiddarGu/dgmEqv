import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.cm import get_cmap

# prepare data
raw_data = """LeBron James,92,95,90,53
Cristiano Ronaldo,105,100,90,45
Lionel Messi,104,98,85,33
Neymar,95,93,80,25
Roger Federer,106,100,90,60
Serena Williams,88,92,85,40
Tiger Woods,80,90,80,50
Steph Curry,85,94,87,42"""
data_labels = ["Salary (Million $)", "Brand Value (score)", "Social Impact (Score)", "Endorsements (Million $)"]
lines = raw_data.split('\n')
data = np.zeros((len(lines), len(data_labels)))
line_labels = []
for i, line in enumerate(lines):
    split_line = line.split(',')
    line_labels.append(split_line[0] + ' ' + str(data[i, 2]))
    data[i, :] = list(map(float, split_line[1:]))

# create figure
fig, ax = plt.subplots(figsize=(12, 8))

# plot data
cmap = get_cmap('viridis')
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=600 + 4400 * (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()),
               c=cmap((data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())),
               label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], c=cmap((data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())),
               label=line_labels[i])

# legend
leg = ax.legend(title=data_labels[2], loc='upper left')

# color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical', aspect=40, label=data_labels[3])

# decoration
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Sports and Entertainment: Athlete\'s Salary, Brand value and Social Impact', fontsize=14, fontweight='bold')

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/229_202312310045.png')

# clear the current figure
plt.clf()
