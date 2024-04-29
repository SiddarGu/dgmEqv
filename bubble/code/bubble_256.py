import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize 
import numpy as np
 
data_str = 'Company,Revenue (Million $),Market Share (%),Profit Margin (%),Product Innovation (Score)\
            \nCoca-Cola,35000,30,20,8\
            \nPepsiCo,29000,25,18,7\
            \nNestle,27000,20,15,9\
            \nDanone,20000,15,12,6\
            \nKraft Heinz,15000,10,9,5\
            \nUnilever,10000,5,6,7'
 
# Splitting the data and transforming it into the required format
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
line_labels = [line.split(',')[0] + ' ' + line.split(',')[2] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in data_lines[1:]])

# Normalizing color and size arrays for bubble chart
norm = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
cmap = cm.get_cmap("Spectral")
rgba = [cmap(norm(value)) for value in data[:, 3]]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, color=rgba[i], s=bubble_sizes[i])
    ax.scatter([], [], label=line_label, color=rgba[i], s=20)
ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.set_title('Analysis of Top Companies in Food and Beverage Industry')
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/356_202312311429.png')
plt.clf()
