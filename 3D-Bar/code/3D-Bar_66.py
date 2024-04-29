import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_str = "Month,Truck Deliveries (000),Rail Deliveries (000),Sea Freight (000),Air Freight (000)/n January,80,95,105,110/n February,90,80,120,130/n March,100,110,130,140/n April,110,115,135,145/n May,125,130,145,155/n June,120,130,150,160"
data_lines = data_str.split("/n")

y_values = data_lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in data_lines[1:]])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

for i in np.arange(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
             0.25, 0.5, data[:, i], shade=True, color=['r','g','b','y'][i], alpha=0.6)

ax.set_title('Comparative Analysis of Different Logistics Modes - 1st Half of The Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values, ha='left')

ax.grid(True)
ax.view_init(30, -40)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/173_202312302235.png')
plt.clf()
