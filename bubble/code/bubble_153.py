# Python Code
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.ticker import AutoMinorLocator
import numpy as np

data_string = """City, Average House Price (Thousand $), Rental Yield (%), Mortgage Interest Rate (%), Quality of Life Index (Score)
New York,850,4.2,3.0,83
Los Angeles,750,3.9,3.1,80
San Francisco,1200,2.8,2.9,89
Chicago,250,5.6,3.2,75
Seattle,500,4.5,3.0,82
Miami,400,5.1,3.2,78
Boston,450,3.5,3.0,81"""

formatted_data = [i.split(',') for i in data_string.split('\n')]
data_labels = formatted_data[0]
line_labels = [f'{i[0]} {i[2]}' for i in formatted_data[1:]]

data = np.array([list(map(float, i[1:])) for i in formatted_data[1:]])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

color_map = plt.cm.get_cmap('viridis')
c_norm = mcolors.Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3]))
scalar_map = cm.ScalarMappable(norm=c_norm, cmap=color_map)

s_norm = mcolors.Normalize(vmin=np.min(data[:,2]), vmax=np.max(data[:,2]))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=scalar_map.to_rgba(data[i, 3]), s=600 + 4400*s_norm(data[i, 2]), edgecolors='black', alpha=0.7, label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), s=20, label=line_labels[i])

plt.colorbar(scalar_map, ax=ax).set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')

ax.grid(True)
ax.set_axisbelow(True)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

plt.xlabel(data_labels[1])
plt.ylabel(data_labels[2])
plt.title('The Housing Market and Quality of Life Across Major US Cities')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/227_202312310045.png', dpi=300)
plt.clf()
