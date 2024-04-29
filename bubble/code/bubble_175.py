import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

raw_data = 'Sport,Number of Fans (Millions),Ticket Sales (Millions),TV Ratings,Revenue (Billions)\n Football,4000,600,15,10\n Basketball,2500,400,10,8\n Baseball,2000,300,8,7\n Soccer,3500,550,12,9\n Tennis,1000,200,5,4\n Golf,1500,250,6,5'
lines = raw_data.split('\n')

data_labels = lines[0].split(',')[1:]
lines = lines[1:]

line_labels = [line.split(',')[0] + str(line.split(',')[2]) for line in lines]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines])

fig, ax = plt.subplots()

cmap = get_cmap('viridis')
norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
for i, line_label in enumerate(line_labels):
  ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]/np.max(data[:, 2]))*4400+600, c=cmap(norm(data[i, 3])), label=None)
  ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)

ax.legend(title=data_labels[2])
fig.colorbar(sm, ax=ax, label=data_labels[3])

plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Analysis of Sports and Entertainment Industry', fontsize=14)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/332_202312311429.png')
plt.clf()
