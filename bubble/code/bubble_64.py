import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.colorbar as mcolorbar

data = np.array([
    [20000,80000,5000,1200],
    [15000,60000,4000,900],
    [10000,40000,3000,700],
    [5000,20000,2000,400],
    [7000,30000,2500,600],
    [8000,35000,2800,650],
    [9000,40000,3200,750]])

data_labels = ['Revenue (Million $)', 'Production Capacity (Units)', 'Labor Cost (Million $)', 'Energy Consumption (GWh)']
line_labels = ['Automobiles', 'Electronics', 'Pharmaceuticals', 'Textiles', 'Chemicals', 'Machinery', 'Steel']

fig, ax = plt.subplots(figsize=(10, 8))

cmap = plt.cm.get_cmap('viridis')
norm = mc.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

for i in range(len(data)):
    line_label = line_labels[i] + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], c=cmap(norm(data[i, 3])), s=(data[i, 2]-data[:,2].min())/(data[:,2].max()-data[:,2].min())*4400+600, label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)

ax.grid(True, linestyle='-.')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2], loc='upper left')

cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.title('Key Statistics of Manufacturing Industries')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/364_202312311429.png')
plt.clf()
