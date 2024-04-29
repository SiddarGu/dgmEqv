
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

#transform data
data_labels = ['Technology Usage (%)', 'Creativity (Score)', 'Social Connectivity (Score)', 'Education Level (Score)']
data = np.array([[90,80,75,70],
                 [85,75,80,65],
                 [75,90,85,60],
                 [80,70,90,55],
                 [70,65,95,50],
                 [65,60,100,45]])

line_labels = ['Europe', 'North America', 'Asia', 'South America', 'Africa', 'Australia']

#plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

cmap = cm.get_cmap('RdYlGn')
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*50, c=cmap(norm(data[i,3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i,3])), label=line_labels[i] + ' ({})'.format(data[i,2]))

ax.legend(title=data_labels[2])

#colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
ax.figure.colorbar(sm, ax=ax, label=data_labels[3])

#configure
ax.grid(linestyle='--', alpha=0.5)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Social Sciences and Humanities: Technology Usage, Creativity, Social Connectivity, and Education Level')

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/22.png')

plt.clf()