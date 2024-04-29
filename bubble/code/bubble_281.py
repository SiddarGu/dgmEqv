import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = '''Legal Subject,Cases Handled (1000s),Convictions Obtained (1000s),Justice Delay Rate (%),Conviction Rate (%),Legal Impact Score
Criminal Law,5000,3300,15,66,85
Civil Rights Law,3000,1700,25,57,75
Corporate Law,4000,2900,20,72,80
Environmental Law,1500,1200,10,80,90
Family Law,3500,2800,20,80,70
Intellectual Property Law,1200,800,15,67,65
Employment Law,2500,2000,18,80,77
Tax Law,2200,1600,12,73,79
Constitution Law,1800,1200,28,67,70'''

lines = data.split('\n')
data_labels = lines[0].split(',')[1:]
data_matrix = [l.split(',')[1:] for l in lines[1:]]
data = np.array(data_matrix, dtype='float')
line_labels = [l.split(',')[0] + ' ' + str(row[2]) for (row,l) in zip(data,lines[1:])]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
size = Normalize(data[:, 2].min(), data[:, 2].max())

for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=600 + 4400 * size(data[i, 2]), cmap='viridis', label=None)
    ax.scatter([], [], color=color, s=20, label=line_labels[i])

plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='viridis'), ax=ax).set_label(data_labels[3])

ax.legend(title=data_labels[2], loc='lower right')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

plt.title("Effectiveness and Impact of Various Legal Subjects")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/80_202312301731.png")
plt.clf()
