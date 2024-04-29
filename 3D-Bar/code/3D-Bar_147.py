import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

original_data = "Department,Number of Employees,Number of Training Sessions,Staff Retention Rate (%)\n Sales,120,50,85\n Marketing,150,40,82\n Finance,80,30,80\n HR,50,60,90\n IT,70,50,75"
data = [[item for item in row.split(",")] for row in original_data.replace(" ", "").split("\n")[1:]]
data = np.array(data)

x_values = list(data[:, 0])
y_values = ["Number of Employees", "Number of Training Sessions", "Staff Retention Rate (%)"]
data = np.float32(data[:, 1:])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i, y in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
            0.55, 0.45, data[:, i], color=["b", "g", "r"][i], alpha=0.6)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.view_init(elev=30, azim=-60)
ax.set_title("HR Management Analysis by Department")
plt.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/120_202312302126.png")
plt.close()
