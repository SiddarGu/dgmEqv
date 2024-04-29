import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import matplotlib.colors as mcolors
from matplotlib.colorbar import ColorbarBase

data = np.array([
    [500, 1500, 60, 15],
    [200, 800, 50, 10],
    [100, 300, 70, 20],
    [50, 500, 100, 5],
    [1000, 100, 15, 0]
])
data_labels = ['Number of Vehicles', 'Total Distance Traveled (Million Kilometers)','Average Speed (km/h)',
 'Fuel Efficiency (km per liter)']
line_labels = ['Car', 'Truck', 'Motorcycle', 'Train','Bicycle']

cmap = get_cmap("viridis")
norm = Normalize(vmin=0, vmax=20)
fig, ax = plt.subplots(figsize=(16, 8))
for i, line_label in enumerate(line_labels):
    scatter = ax.scatter(data[i, 0], data[i, 1], s=600 + 5000 * data[i, 2] / np.max(data[:, 2]), c=[cmap(norm(data[i, 3]))], 
               label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), alpha=0.6, s=20, label=line_label + ' ' + str(data[i, 2]))

ax.legend(title=data_labels[2], scatterpoints=1, loc="upper left")

ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
sm = plt.cm.ScalarMappable(cmap='viridis', norm=mcolors.Normalize(vmin=0, vmax=20))
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

plt.title('Analysis of Transportation Modes in Terms of Efficiency and Distance')

plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/367_202312311429.png')
plt.clf()
