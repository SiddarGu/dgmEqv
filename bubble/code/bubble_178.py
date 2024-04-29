import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_input = 'Transport Type,Annual Freight Volume (Billion Tonnes),Operational Costs (Billion $),Environmental Impact (Score),Safety Ratings (Score)\n Rail,550,150,30,80\n Road,800,250,40,70\n Water,500,100,15,85\n Air,50,300, 60,90\n Pipeline,100,80,25,90'

data_lines = data_input.split('\n')

data_labels = data_lines[0].split(',')[1:]

line_labels = [line.split(',')[0].strip() + ' ' + line.split(',')[2].strip() for line in data_lines[1:]]

data = np.array([list(map(int, line.split(',')[1:])) for line in data_lines[1:]])

min_size = 600
max_size = 5000
min_color = min(data[:,3])
max_color = max(data[:,3])

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot()
cmap = plt.get_cmap("viridis")

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-min(data[:,2]))*(max_size-min_size)/(max(data[:,2])-min(data[:,2]))+min_size, c=cmap((data[i, 3]-min_color)/(max_color-min_color)), edgecolor='black', linewidth=1, alpha=0.75, label=None)
    ax.scatter([], [], c=cmap((data[i, 3]-min_color)/(max_color-min_color)), alpha=0.75, s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')

sm = cm.ScalarMappable(cmap=cmap, norm=Normalize(min_color, max_color))
plt.colorbar(sm, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.title('Comparative Analysis of Different Transport Types - Transportation and Logistics 2023')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/187_202312310045.png')
plt.clf()
