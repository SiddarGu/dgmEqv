import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_str = "Company,Market Cap (Billion $),Revenue (Billion $),Net Income (Million $),Carbon Footprint (Metric Tons)/n Exxon Mobil,320,280,10000,500000/n Chevron,200,200,8000,250000/n BP,180,250,9000,400000/n Royal Dutch Shell,250,220,9500,350000/n Total,150,180,7000,150000/n Chevron,200,200,8000,250000/n E.ON,100,120,5000,100000/n Duke Energy,80,100,4000,90000/n Engie,90,150,6000,120000/n Enel,120,130,5500,80000"
data_arr = [item.split(',') for item in data_str.split('/n ')]
data_labels = data_arr[0]
line_labels = [f"{item[0]} {item[2]}" for item in data_arr[1:]]
data = np.array([list(map(float, item[1:])) for item in data_arr[1:]])

fig, ax = plt.subplots(figsize=(10, 10))

scatter = ax.scatter(data[:, 0], data[:, 1], c=data[:, 3], s=(data[:, 2]-data[:, 2].min())/(data[:, 2].max()-data[:, 2].min())*(5000-600)+600, alpha=0.6, cmap='viridis', label=None)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], color=cm.viridis(Normalize()(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2])
cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

ax.grid(True)
plt.title('Energy and Utilities Companies by Financial and Environmental Performance')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/394_202312311429.png")
plt.clf()
