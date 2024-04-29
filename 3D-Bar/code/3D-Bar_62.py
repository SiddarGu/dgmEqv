import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Extracting data
data_string = "Region,Number of Schools,Number of Students,Number of Graduates/n Urban,20000,50000,40000/n Rural,10000,30000,20000/n Coastal,15000,40000,32000/n Mountainous,5000,15000,12000"
data_string = data_string.replace("/n", "\n").split("\n")
rows = [row.split(",") for row in data_string]
x_values = [row[0] for row in rows[1:]]
y_values = rows[0][1:]
data = np.array([list(map(int, row[1:])) for row in rows[1:]], dtype=np.float32)

# Creating figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Creating bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.6, data[:, i], color=['b', 'r', 'g', 'y'], alpha=0.7)

# Setting title and labels 
ax.set_title('Education and Academic Scenario: A Comparative Study Across Different Geographical Regions')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Values')

# Adjust view
ax.view_init(elev=20, azim=-35)

# Setting layout to auto
plt.tight_layout()

# Saving figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/251_202312310050.png')

# Clearing current figure
plt.clf()
