import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# data
raw_data = [
    ["2018", 200, 5000, 25],
    ["2019", 300, 4800, 30],
    ["2020", 400, 4500, 35],
    ["2021", 500, 4100, 40],
    ["2022", 600, 3700, 45]
]

# transform into x_values, y_values, data
x_values = [item[0] for item in raw_data]
y_values = ["Alternative Energy Production (GW)", "CO2 Emissions (Million Tonnes)", "Recycling Rates (%)"]
data = np.array([item[1:] for item in raw_data], dtype=np.float32).T

# create figure and subplot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# plot each column of data
_x = np.arange(len(x_values))
_y = np.arange(len(y_values))
_x, _y = np.meshgrid(_x, _y)
x, y = _x.ravel(), _y.ravel()

for i in range(len(y_values)):
    ax.bar3d(x[i::len(y_values)], y[i::len(y_values)], 0, dx=0.8, dy=0.8, dz=data.ravel()[i::len(y_values)], color=plt.cm.viridis(i/len(y_values)), alpha=0.7)
    

# axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# other configurations
ax.set_title('Trends in Environmental Sustainability Metrics 2018-2022')
plt.grid(True)
ax.view_init(elev=20., azim=-35)
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/90_202312302126.png')

# clear figure
plt.clf()
